import os
import sys
import argparse

import pandas as pd


def parse_args(args: list):
    parser = argparse.ArgumentParser(
        description="Move files into a Johnny Decimal folder structure from a list of categorised files"
    )

    parser.add_argument(
        "target_path",
        type=str,
        help="Path under which the Johnny Decimal structure exists",
    )

    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="categorised-files.csv",
        help="Input CSV file of categorised files",
    )

    parser.add_argument(
        "--purge",
        action="store_true",
        help="Delete files marked for removal",
    )

    return parser.parse_args()


def main():
    args = parse_args(sys.argv[1:])
    
    target_path = os.path.abspath(args.target_path)
    df = pd.read_csv(args.input)

    if args.purge:
        purge_df = df[df["delete"] == True]
        
        for i, row in purge_df.iterrows():
            filepath = os.path.join(row["filepath"], row["filename"])
            print(f"Deleting file: {filepath}")


if __name__ == "__main__":
    main()
