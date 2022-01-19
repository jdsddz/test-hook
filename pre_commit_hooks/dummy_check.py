import sys
import argparse


def main(argv=None):
  parser = argparse.ArgumentParser()
  parsed_args, args_rest = parser.parse_known_args(argv)
  print(f'parsed_args: {parsed_args}')
  print(f'args_rest: {args_rest}')
  print(f'aaaaadbdd')
  return 1234


if __name__ == "__main__":
  sys.exit(main())
