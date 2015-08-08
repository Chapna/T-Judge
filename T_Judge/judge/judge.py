import subprocess
import os
import io
from django.conf import settings


# By default these functions use settings.BASE_DIR in order to make path from relative into absolute.

def gcc_compile(source_file: str, executable_file: str):
    source_file = os.path.join(settings.BASE_DIR, source_file)
    executable_file = os.path.join(settings.BASE_DIR, executable_file)
    try:
        subprocess.check_output(['gcc', source_file, '-o', executable_file, '-lm'], stderr=subprocess.STDOUT,
                                timeout=10)
    except subprocess.CalledProcessError as exception:
        print(exception.output)
    except subprocess.TimeoutExpired as exception:
        print("Compilation cancelled after {}".format(exception.timeout))
    else:
        print("Compilation was successful")


def run_and_test(executable_file: str, test_file: str, answer_file: str):
    executable_file = os.path.join(settings.BASE_DIR, executable_file)
    test_file = os.path.join(settings.BASE_DIR, test_file)
    answer_file = os.path.join(settings.BASE_DIR, answer_file)

    # use sandbox....
    env = os.environ
    if settings.PATH_TO_EASYSANDBOX != '':
        env['LD_PRELOAD'] = settings.PATH_TO_EASYSANDBOX

    with open(test_file, 'r', 0) as test_fd, open() as output_fd:
        rc = subprocess.call([executable_file], env=env, stdin=test_fd, stdout=output_fd)
        if not rc:
            pass


def diff(result_file: io.TextIOBase, answer_file: io.TextIOBase):
    res = result_file.readlines()
    ans = answer_file.readlines()

    if len(res) != len(ans):
        return False

    for i in range(len(res)):
        if res[i] != ans[i]:
            return False
    return True
