from __future__ import print_function, absolute_import, unicode_literals

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from pygments.style import Style
from pygments.token import Token
from pygments.token import Keyword, Name, Operator, Generic, Literal, Text
from pygments.styles.default import DefaultStyle
from prompt_toolkit.key_binding.defaults import load_key_bindings_for_prompt
from prompt_toolkit.keys import Keys

from kubeshell.style import StyleFactory
from kubeshell.completer import KubectlCompleter
from kubeshell.lexer import KubectlLexer
from kubeshell.toolbar import Toolbar

import os
import click
import sys
import subprocess
import yaml


inline_help=True

registry = load_key_bindings_for_prompt()
completer = KubectlCompleter()


class KubeConfig(object):

    clustername = user = ""
    namespace = "default"
    current_context_index = 0
    current_context_name = ""

    @staticmethod
    def parse_kubeconfig():
        if not os.path.exists(os.path.expanduser("~/.kube/config")):
            return ("", "", "")

        with open(os.path.expanduser("~/.kube/config"), "r") as fd:
            docs = yaml.load_all(fd)
            for doc in docs:
                current_context = ""
                for k,v in doc.items():
                    if k == "current-context":
                        current_context = v
                for k,v in doc.items():
                    if k == "contexts":
                        for index, context in enumerate(v):
                            if context['name'] == current_context:
                                KubeConfig.current_context_index = index
                                KubeConfig.current_context_name = context['name']
                                if 'cluster' in context['context']:
                                    KubeConfig.clustername = context['context']['cluster']
                                if 'namespace' in context['context']:
                                    KubeConfig.namespace = context['context']['namespace']
                                if 'user' in context['context']:
                                    KubeConfig.user = context['context']['user']
                                return (KubeConfig.clustername, KubeConfig.user, KubeConfig.namespace)
        return ("", "", "")

    @staticmethod
    def switch_to_next_cluster():
        if not os.path.exists(os.path.expanduser("~/.kube/config")):
            return

        with open(os.path.expanduser("~/.kube/config"), "r") as fd:
            docs = yaml.load_all(fd)
            for doc in docs:
                for k,v in doc.items():
                    if k == "contexts":
                        KubeConfig.current_context_index = (KubeConfig.current_context_index+1) % len(v)
                        cluster_name = v[KubeConfig.current_context_index]['name']
                        kubectl_config_use_context = "kubectl config use-context " + cluster_name
                        cmd_process = subprocess.Popen(kubectl_config_use_context, shell=True, stdout=subprocess.PIPE)
                        cmd_process.wait()
        return

    @staticmethod
    def switch_to_next_namespace(current_namespace):
        namespace_resources = completer.get_resources("namespace")
        namespaces = []
        for res in namespace_resources:
            namespaces.append(res[0])
        namespaces.sort()
        index = (namespaces.index(current_namespace)+1) % len(namespaces)
        next_namespace = namespaces[index]
        kubectl_config_set_namespace = "kubectl config set-context " + KubeConfig.current_context_name + " --namespace=" + next_namespace
        cmd_process = subprocess.Popen(kubectl_config_set_namespace, shell=True, stdout=subprocess.PIPE)
        cmd_process.wait()

class Kubeshell(object):

    clustername = user = ""
    namespace = "default"

    def __init__(self, refresh_resources=True):
        self.history = FileHistory(os.path.expanduser("~/.kube/shell/history"))
        if not os.path.exists(os.path.expanduser("~/.kube/shell/")):
            os.makedirs(os.path.expanduser("~/.kube/shell/"))
        self.toolbar = Toolbar(self.get_cluster_name, self.get_namespace, self.get_user, self.get_inline_help)

    @registry.add_binding(Keys.F4)
    def _(event):
        try:
            KubeConfig.switch_to_next_cluster()
            Kubeshell.clustername, Kubeshell.user, Kubeshell.namespace = KubeConfig.parse_kubeconfig()
        except  Exception as e:
            # TODO: log errors to log file
            pass

    @registry.add_binding(Keys.F5)
    def _(event):
        try:
            KubeConfig.switch_to_next_namespace(Kubeshell.namespace)
            Kubeshell.clustername, Kubeshell.user, Kubeshell.namespace = KubeConfig.parse_kubeconfig()
        except  Exception as e:
            # TODO: log errors to log file
            pass

    @registry.add_binding(Keys.F9)
    def _(event):
        global inline_help
        if inline_help:
            inline_help = False
        else:
            inline_help = True
        completer.set_inline_help(inline_help)

    @registry.add_binding(Keys.F10)
    def _(event):
        sys.exit()

    def get_cluster_name(self):
        return Kubeshell.clustername

    def get_namespace(self):
        return Kubeshell.namespace

    def get_user(self):
        return Kubeshell.user

    def get_inline_help(self):
        return inline_help

    def run_cli(self):

        def get_title():
            return "kube-shell"

        if not os.path.exists(os.path.expanduser("~/.kube/config")):
            click.secho('Kube-shell uses ~/.kube/config for server side completion. Could not find ~/.kube/config. \
                    Server side completion functionality may not work.', fg='red', blink=True, bold=True)
        while True:
            global inline_help
            try:
                Kubeshell.clustername, Kubeshell.user, Kubeshell.namespace = KubeConfig.parse_kubeconfig()
            except:
                # TODO: log errors to log file
                pass
            completer.set_namespace(self.namespace)
            user_input = prompt('kube-shell> ',
                        history=self.history,
                        auto_suggest=AutoSuggestFromHistory(),
                        style=StyleFactory("vim").style,
                        lexer=KubectlLexer,
                        get_title=get_title,
                        enable_history_search=False,
                        get_bottom_toolbar_tokens=self.toolbar.handler,
                        vi_mode=True,
                        key_bindings_registry=registry,
                        completer=completer)
            if user_input == "clear":
                click.clear()
            elif user_input == "exit":
                sys.exit()

            # if execute shell command then strip "!"
            if user_input.startswith("!"):
                user_input = user_input[1:]

            if user_input:
                if '-o' in user_input and 'json' in user_input:
                    user_input = user_input + ' | pygmentize -l json'
                p = subprocess.Popen(user_input, shell=True)
                p.communicate()
