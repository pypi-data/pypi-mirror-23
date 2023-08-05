"""Module describing the planemo ``conda_search`` command."""
from __future__ import print_function

import click

from planemo import options
from planemo.cli import command_function
from planemo.conda import build_conda_context


@click.command('conda_search')
@options.conda_target_options(include_local=False)
@click.argument(
    "term",
    metavar="TERM",
    type=str,
    nargs=1,
)
@command_function
def cli(ctx, term, **kwds):
    """Perform conda search with Planemo's conda.

    Implicitly adds channels Planemo is configured with.
    """
    conda_context = build_conda_context(ctx, handle_auto_init=True, **kwds)
    conda_context.exec_command("search", [term])
