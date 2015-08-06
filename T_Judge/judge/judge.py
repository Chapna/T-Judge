import subprocess


def gcc_compile(input_file: str, output_file: str):
    try:
        subprocess.check_output(['gcc', input_file, '-o', output_file, '-lm'], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exception:
        print(exception.output)
    else:
        print("Compilation was successful")
