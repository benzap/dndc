""" Main entry point to 'dndc' commandline tool
"""
import sys
import os.path as path

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import click
import click_repl

import dndc.db as db
from dndc.resource import Resource
import dndc.environment as environment
import dndc.repl as repl


_R = Resource()


@click.group()
def cli():
    pass


@cli.command()
def repl():
    history_file = path.join(environment.get_data_directory(), "dndc_command_history.txt")
    environment.clear(history_file)
    prompt_options = {
        "message": "dndc> ",
        "history": FileHistory(history_file),
        "auto_suggest": AutoSuggestFromHistory(),
    }
    click_repl.repl(click.get_current_context(),
                    prompt_kwargs=prompt_options)


def main():
    cli()


if __name__ == "__main__":
    main()
