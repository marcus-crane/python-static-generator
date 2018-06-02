from invoke import task
from bundler.settings import Constants


@task
def flake8(ctx):
    """ Run the flake8 linter """
    build_dir = Constants.BUILD_DIR
    ctx.run(f"python -m flake8 --exclude=docs,env,{build_dir},venv")
