import subprocess
import os
from django.conf import settings


def gcc_compile(source_file: str, executable_file: str):
    try:
        subprocess.check_output(['gcc', source_file, '-o', executable_file, '-lm'], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exception:
        print(exception.output)
    else:
        print("Compilation was successful")


def run_and_test(executable_file: str, test_file: str):
    env = os.environ
    if settings.PATH_TO_EASYSANDBOX != '':
        env['LD_PRELOAD'] = settings.PATH_TO_EASYSANDBOX
    subprocess.check_output([os.path.join('.', executable_file)], env=env)
