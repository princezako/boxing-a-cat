import argparse

from example_package.boxing_cat_solver import boxing_cat_solver


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="The number to add one too", type=float)
    args = parser.parse_args()
    print(f"{args.number} add one is {add_one(args.number)}")
