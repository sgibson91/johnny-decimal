import os
import sys
import argparse

import pandas as pd


def parse_args(args: list):
    parser = argparse.ArgumentParser(
        description="Create Johnny Decimal folder structure from a list of categorised files"
    )

    parser.add_argument(
        "target_path",
        type=str,
        help="Path under which to create the Johnny Decimal structure",
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

    target_path = os.path.abspath(args.target_path)    
    df = pd.read_csv(args.input)

    areas = sorted(df["area"].dropna().unique().tolist())
    if len(areas) > 10:
        raise ValueError(
            f"Number of areas: {len(areas)}\n\n" +
            "Only 10 areas permitted - please recategorise!\n\n" +
            "\n".join([area for area in areas])
        )

    for i, area in enumerate(areas):
        area_dir = f"{i}0 - {i}9 {area.title()}"
        print(area_dir)

        sub_df = df[df["area"] == area]
        categories = sorted(sub_df["category"].dropna().unique().tolist())
        if len(categories) > 10:
            raise ValueError(
                f"Number of categories: {len(categories)}\n\n" +
                "Only 10 categories per area permitted - please recategorise!\n\n" +
                "\n".join([category for category in categories])
            )

        for j, category in enumerate(categories):
            category_dir = f"{i}{j} {category.title()}"
            print(category_dir)

            folder_path = os.path.join(target_path, area_dir, category_dir)
            print(folder_path)


if __name__ == "__main__":
    main()
