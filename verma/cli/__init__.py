import click

from verma.cli import bump


@click.group()
def app():
    ...


app.add_command(bump.bump)


if __name__ == '__main__':
    app()