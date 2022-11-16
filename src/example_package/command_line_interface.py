import argparse

from example_package.boxing_cat_solver import boxing_cat_solver


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help="Your chosen potential", type=string)
    args = parser.parse_args()
    print(f"{args.string} applied to the potential is 


