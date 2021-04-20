from invoke import task

@task
def start(ctx):
    ctx.run('python3 src/index.py')
@task
def test(ctx):
    ctx.run('python3 -m pytest src/tests/')
@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest src')
@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage html')
@task(coverage_report)
def report(ctx):
    ctx.run('chromium htmlcov/index.html')
