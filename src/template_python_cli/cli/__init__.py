import click

from template_python_cli import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """Opinionated Python template for new CLIs."""
    click.echo("Start here")
