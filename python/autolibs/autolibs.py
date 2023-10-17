import importlib.util
import os
import subprocess
import venv
from types import SimpleNamespace


depends = ("requests",)  # The dependencies

if all(importlib.util.find_spec(x) is None for x in depends):
    def call_python(context: SimpleNamespace, *py_args: str):
        """Executes the newly created Python using safe-ish options"""
        args: list[str] = [context.env_exec_cmd, *py_args]
        env = os.environ.copy()
        env['VIRTUAL_ENV'] = context.env_dir
        env.pop('PYTHONHOME', None)
        env.pop('PYTHONPATH', None)
        subprocess.check_output(
            args, env=env, cwd=context.env_dir, executable=context.env_exec_cmd)

    # Make the virtual environment
    env_dir = os.path.abspath('.venv')
    virtualenv = venv.EnvBuilder(with_pip=True)
    virtualenv.create(env_dir)
    context = virtualenv.ensure_directories(env_dir)

    # Install the dependencies
    call_python(context, '-m', 'pip', 'install', *depends)

    # Run this file in the virtual environment
    exit(subprocess.call([context.env_exec_cmd, __file__]))

import requests  # noqa

print(requests.__name__, requests.__version__)

...
