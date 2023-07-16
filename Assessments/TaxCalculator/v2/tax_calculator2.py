#!/usr/bin/python3
"""
Problem:
"""
import argparse
import os
from configparser import ConfigParser

from taxbandmanager import TaxBandManager
from utils import FileAndStreamLogger

logger = FileAndStreamLogger(
    os.path.splitext(os.path.basename(__file__))[0],  # "tax_calculator2"
    os.path.splitext(__file__)[0] + ".log",  # tax_calculator2.log
)


class TaxCalculator:
    @staticmethod
    def input_validator(value):
        try:
            return float(value)
        except ValueError:
            logger.error("Invalid input: salary must be a numerical value.")
            raise argparse.ArgumentTypeError(
                "Invalid input: salary must be a numerical value."
            )

    @staticmethod
    def calculate_tax(band_manager, tax_band_name, salary):
        default_band = band_manager.tax_bands.get("default")
        if tax_band_name:
            band = band_manager.tax_bands.get(tax_band_name)
            if not band:
                logger.error(f"No tax band found with the name '{tax_band_name}'")
                return None
        elif default_band:
            band = band_manager.tax_bands.get(default_band)
        else:
            logger.error("No default tax band set.")
            return None

        if band:
            tax_amount = 0
            for lower_bound, rate in band.items():
                if salary > lower_bound:
                    tax_amount += (salary - lower_bound) * rate
            logger.info(f"For salary {salary}: Tax Amount is {tax_amount}")
            return tax_amount


def main(tax_bands_file):
    parser_obj = argparse.ArgumentParser(
        description="Tax Band Manager and Calculator",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    subparsers = parser_obj.add_subparsers(
        title="Actions", dest="action", required=True
    )

    manager_parser = subparsers.add_parser("taxband", help="Manage tax bands")
    manager_subparsers = manager_parser.add_subparsers(
        title="Action Type", dest="action_type", required=True
    )

    list_parser = manager_subparsers.add_parser("list", help="List all tax bands")
    list_parser.add_argument("bandname", nargs="?", help="Name of the tax band")

    create_parser = manager_subparsers.add_parser("create", help="Create a tax band")
    create_parser.add_argument("bandname", help="Name of the tax band")
    create_parser.add_argument("slabs", nargs="+", help="Tax band slab(s)")

    update_parser = manager_subparsers.add_parser("update", help="Update a tax band")
    update_parser.add_argument("bandname", help="Name of the tax band")
    update_parser.add_argument("slabs", nargs="+", help="Tax band slab(s)")

    delete_parser = manager_subparsers.add_parser("delete", help="Delete a tax band")
    delete_parser.add_argument("bandname", help="Name of the tax band")

    clear_cache_parser = manager_subparsers.add_parser(
        "deleteall", help="To delete all saved tax bands"
    )
    clear_cache_parser.add_argument("bandname", nargs="?", help="Name of the tax band")

    setdefault_parser = manager_subparsers.add_parser(
        "setdefaultband", help="Set default tax band"
    )
    setdefault_parser.add_argument("bandname", help="Name of the tax band")

    calculator_parser = subparsers.add_parser("calculate", help="Calculate tax amount")
    calculator_parser.add_argument("--bandname", help="Name of the tax band")
    calculator_parser.add_argument(
        "--salary", type=TaxCalculator().input_validator, help="Salary amount"
    )

    args = parser_obj.parse_args()

    if args.action == "taxband":
        band_manager = TaxBandManager(logger, tax_bands_file)
        if args.action_type == "list":
            band_manager.list_bands()
        elif args.action_type == "create":
            logger.info(f"args.slabs: {args.slabs}")
            band_manager.create_band(args.bandname, args.slabs)
        elif args.action_type == "update":
            band_manager.update_band(args.bandname, args.slabs)
        elif args.action_type == "delete":
            band_manager.delete_band(args.bandname)
        elif args.action_type == "setdefaultband":
            band_manager.set_default_band(args.bandname)
        elif args.action_type == "deleteall":
            band_manager.delete_band_file()
    elif args.action == "calculate":
        calculator = TaxCalculator()
        band_manager = TaxBandManager(logger, tax_bands_file)
        calculator.calculate_tax(band_manager, args.bandname, args.salary)


if __name__ == "__main__":
    parser = ConfigParser()
    parser.read("config.ini")

    main(parser.get("Project", "TAX_BAND_FILE_NAME"))
