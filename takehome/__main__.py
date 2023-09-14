import click

from takehome.solutions import demo_solution
from takehome.solutions import solution2
from takehome.solutions import solution7


@click.group
def cli() -> None:
    pass


@cli.command(name="demo")
def demo() -> None:
    demo_solution()


@cli.command(name="question2")
def question2() -> None:
    solution2()


@cli.command(name="question7")
def question7() -> None:
    solution7()


if __name__ == "__main__":
    cli()
