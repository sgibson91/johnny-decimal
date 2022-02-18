import os
import sys
import argparse


def parse_args(args: list):
    parser = argparse.ArgumentParser(
        description="Remove empty directories from a path's tree"
    )

    parser.add_argument(
        "target_path",
        type=str,
        help="Path under which to delete empty folders",
    )

    return parser.parse_args()


def main():
    args = parse_args(sys.argv[1:])
    target_path = os.path.abspath(args.target_path)

    for dirpath, dirnames, filenames in os.walk(target_path, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)


if __name__ == "__main__":
    main()
