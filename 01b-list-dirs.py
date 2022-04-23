import argparse
import os
import sys

import pandas as pd


def parse_args(args: list):
    parser = argparse.ArgumentParser(
        description="List the lowest subdirectories in a specified directory and generate a CSV file."
    )

    parser.add_argument(
        "target_path",
        type=str,
        help="Path to the target directory",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="subdirs.csv",
        help="Output CSV file of subdirectory filepaths",
    )

    return parser.parse_args()


def main():
    args = parse_args(sys.argv[1:])

    target_path = os.path.abspath(os.path.expanduser(args.target_path))
    df = pd.DataFrame(columns=["filepath", "dirname", "area", "category", "delete"])

    for dir_name, subdirs, _ in os.walk(target_path):
        if not subdirs:
            tmp = pd.DataFrame(
                {
                    "filepath": os.path.dirname(dir_name),
                    "dirname": os.path.basename(dir_name),
                    "area": "",
                    "category": "",
                    "delete": False,
                },
                index=[0],
            )
            df = pd.concat([df, tmp], ignore_index=True)

    df.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
