from invoke import Collection
from tasks import build, lint, test

ns = Collection()

ns.add_task(build.install_deps)
ns.add_task(build.save_deps)
ns.add_task(test.run_all, 'test')
ns.add_task(test.unit)
ns.add_task(lint.flake8, 'lint')
