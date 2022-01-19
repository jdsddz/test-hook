import sys
import argparse
import os
import subprocess


def run_process(cmd_arg):
    with subprocess.Popen(cmd_arg, stdout=subprocess.PIPE, shell=True) as proc:
        return proc.stdout.read()


def main(argv=None):
    # parser = build_parser()
    # parser = argparse.ArgumentParser()
    # parsed_args, args_rest = parser.parse_known_args(argv)
    # print(f'parsed_args: {parsed_args}')
    # print(f'args_rest: {args_rest}')
    # for file_path in parsed_args.files:
    #   print(f'file_path: {file_path}')
    # stream = os.popen('ls')
    # output = stream.read()
    print(run_process('ls -d pipfile'))
    if run_process('ls -d pipfile') == 'pipfile':
        dependencies = run_process('pip freeze').split('\n')
        print (f'list: {dependencies}')
    # print(f'output: {output}')
    print(f'aaaaadbdd')
    # print(type(output))
    return 1234


if __name__ == "__main__":
    sys.exit(main())
