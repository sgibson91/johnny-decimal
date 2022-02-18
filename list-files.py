import os
import sys
import argparse

import pandas as pd


def parse_args(args: list):
    parser = argparse.ArgumentParser(
        description="List the files in a specified directory and generate a CSV file."
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
        default="files.csv",
        help="Output CSV file of filepaths",
    )

    return parser.parse_args()


def main():
    args = parse_args(sys.argv[1:])

    target_path = os.path.abspath(os.path.expanduser(args.target_path))
    df = pd.DataFrame(columns=["filepath", "filename", "area", "category"])

    for dir_name, _, files in os.walk(target_path):
        for filename in files:
            tmp = pd.DataFrame({
                "filepath": dir_name,
                "filename": filename,
                "area": "",
                "category": "",
            }, index=[0])
            df = pd.concat([df, tmp], ignore_index=True)

    df.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
