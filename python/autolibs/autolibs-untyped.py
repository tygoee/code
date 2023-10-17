import importlib.util
import os
import subprocess
import venv

depends = ("requests", "pyyaml")

if all(importlib.util.find_spec(x) is None for x in depends):
    def call_python(context, *py_args, **kwargs):
        """Executes the newly created Python using safe-ish options"""
        args = [context.env_exec_cmd, *py_args]
        kwargs['env'] = env = os.environ.copy()
        env['VIRTUAL_ENV'] = context.env_dir
        env.pop('PYTHONHOME', None)
        env.pop('PYTHONPATH', None)
        kwargs['cwd'] = context.env_dir
        kwargs['executable'] = context.env_exec_cmd
        subprocess.check_output(args, **kwargs)

    # Make the virtual environment
    env_dir = os.path.abspath('.venv')
    virtualenv = venv.EnvBuilder(with_pip=True)
    virtualenv.create(env_dir)
    context = virtualenv.ensure_directories(env_dir)

    # Install the dependencies
    call_python(context, '-m', 'pip', 'install', *depends)

    # Run this file in the virtual environment
    exit(subprocess.call([context.env_exec_cmd, __file__]))

# autopep8: off
import requests
import yaml
# autopep8: on

print(requests.__name__, requests.__version__)
print(yaml.__name__, yaml.__version__)

...
