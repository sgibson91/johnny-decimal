import argparse
import os
import sys

import pandas as pd


def parse_args(args: list):
    parser = argparse.ArgumentParser(
        description="Delete files from a list of categorised files"
    )

    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="categorised-files.csv",
        help="Input CSV file of categorised files",
    )

    return parser.parse_args()


def main():
    args = parse_args(sys.argv[1:])

    df = pd.read_csv(args.input)
    df = df[df["delete"] == True]

    for i, row in df.iterrows():
        filepath = os.path.join(row["filepath"], row["filename"])
        if os.path.exists(filepath):
            os.remove(filepath)


if __name__ == "__main__":
    main()
