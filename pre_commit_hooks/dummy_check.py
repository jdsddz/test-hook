import sys
import argparse
import os

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--full-report",
        default="--full-report",
        const="--full-report",
        action="store_const",
    )
    parser.add_argument(
        "--short-report",
        dest="full_report",
        const="--short-report",
        action="store_const",
    )
    parser.add_argument("--ignore", "-i", action="append")
    parser.add_argument("files", nargs="+")
    return parser


def main(argv=None):
  parser = build_parser()
  # parser = argparse.ArgumentParser()
  parsed_args, args_rest = parser.parse_known_args(argv)
  print(f'parsed_args: {parsed_args}')
  print(f'args_rest: {args_rest}')
  for file_path in parsed_args.files:
    print(f'file_path: {file_path}')
  stream = os.popen('ls')
  output = stream.read()
  print(f'output: {output}')
  print(f'aaaaadbdd')
  print(type(output))
  return 1234


if __name__ == "__main__":
  sys.exit(main())
