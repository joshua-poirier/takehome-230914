import click

from takehome.solutions import demo_solution
from takehome.solutions import solution1
from takehome.solutions import solution7


@click.group
def cli() -> None:
    pass


@cli.command(name="demo")
def demo() -> None:
    demo_solution()


@cli.command(name="question1")
def question1() -> None:
    solution1()


@cli.command(name="question7")
def question7() -> None:
    solution7()


if __name__ == "__main__":
    cli()
