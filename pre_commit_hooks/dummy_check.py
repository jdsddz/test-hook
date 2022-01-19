import sys
import argparse
import os
import subprocess
from pipfile import Pipfile


def run_process(cmd_arg):
    with subprocess.Popen(cmd_arg, stdout=subprocess.PIPE, shell=True) as proc:
        return proc.stdout.read().decode('utf-8')


def main(argv=None):
    # p= Pipfile.load('Pipfile')
    # p.
    # parser = build_parser()
    # parser = argparse.ArgumentParser()
    # parsed_args, args_rest = parser.parse_known_args(argv)
    # print(f'parsed_args: {parsed_args}')
    # print(f'args_rest: {args_rest}')
    # for file_path in parsed_args.files:
    #   print(f'file_path: {file_path}')
    # stream = os.popen('ls')
    # output = stream.read()
    # files_str = run_process('pwd')
    # print(f'files_str: {files_str}')

    # p = run_process('pip list --format=json')

    # dependencies = []
    # print(f'p: {p}')
    p = Pipfile.load('Pipfile')
    print(p.contents)
    print(p.lock())

    # if 'Pipfile' in files_str:
    #     dependencies = run_process('pip freeze').split('\n')
    # elif 'pom.xml' in files_str:
    #     dependencies = run_process('pip freeze').split('\n')
    # print(f'list: {dependencies}')
    # print(f'output: {output}')
    # if os.path.exists('Pipfile'):
    #     f = open('Pipfile', 'r')
    #     print(f.read())
    # elif os.path.exists('pom.xml'):
    #     f = open('pom.xml', 'r')
    #     print(f.read())
    print(f'aaaaadbdd')
    # print(type(output))
    return 1234


if __name__ == "__main__":
    sys.exit(main())
