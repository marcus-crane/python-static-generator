from invoke import task
from tasks.lint import flake8


@task(post=[flake8])
def run_all(ctx):
    """ Run all unit tests and linting """
    ctx.run("pytest")


@task
def unit(ctx):
    """ Run all unit tests """
    ctx.run("pytest")
