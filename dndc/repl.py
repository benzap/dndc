'''REPL implementation for a good commandline interface
'''
import os.path as path

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
import click

import dndc.environment as environment


DNDC_Completer = WordCompleter(
    [
        "campaign",
        "exit",
        "quit",
    ],
    ignore_case=True)


def start():
    history_file = path.join(environment.get_data_directory(), "dndc_command_history.txt")
    environment.clear(history_file)
    while True:
        user_input = prompt("dndc> ",
                            history=FileHistory(history_file),
                            auto_suggest=AutoSuggestFromHistory(),
                            completer=DNDC_Completer,
                            )
        if user_input == "exit":
            break
        click.echo_via_pager(user_input)
