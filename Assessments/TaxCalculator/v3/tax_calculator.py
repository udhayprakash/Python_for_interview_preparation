"""
Main entry point for the tax calculator CLI.
"""
import argparse

from bands.band_manager import BandManager
from calculation import TaxCalculator
from utils.logger import Logger


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for band management commands
    band_parser = subparsers.add_parser("band")
    band_subparser = band_parser.add_subparsers(dest="band_command")
    band_manager = BandManager()

    # Create band command
    create_parser = band_subparser.add_parser("create")
    create_parser.add_argument("name")
    create_parser.add_argument("slabs", nargs="+")
    create_parser.set_defaults(func=band_manager.create_band)

    # List bands command
    list_parser = band_subparser.add_parser("list")
    list_parser.set_defaults(func=band_manager.list_bands)

    # Delete band command
    delete_parser = band_subparser.add_parser("delete")
    delete_parser.add_argument("name")
    delete_parser.set_defaults(func=band_manager.delete_band)

    # Set default band command
    default_parser = band_subparser.add_parser("set_default")
    default_parser.add_argument("name")
    default_parser.set_defaults(func=band_manager.set_default_band)

    # Subparser for tax calculation command
    calc_parser = subparsers.add_parser("calc")
    calc_parser.add_argument("band")
    calc_parser.add_argument("salary", type=float)
    calc_parser.set_defaults(func=TaxCalculator().calculate_tax)

    args = parser.parse_args()
    logger = Logger()
    if hasattr(args, "func"):
        args.func(logger, **vars(args))


if __name__ == "__main__":
    main()
