#!/usr/bin/python3
r"""
Problem:
    write a function (or method) that can calculate the tax owed
    given these 2 inputs: salary and tax band
        salary is an int or float or str, e.g. 10500 10500.00 "10500"
        tax band is whatever you want it to be, as long as it can represent something like:
                0 - 10k: 2.5%
                10k - 20k: 5%
                20k - 50k: 10%
                \> 50k: 20%
    the tax bands given are just an example
    users should be able to pass in whatever tax bands they want

    just make sure to document your code so that it is understood how to use the function
"""
import re
from pprint import pprint


class TaxBandGenerator:
    def __init__(self):
        """Initialize the TaxBandGenerator class."""
        self.tax_bands = {}

    def get_user_input(self):
        """Prompt the user for tax band management options."""
        while True:
            action = (
                input(
                    """
                Enter a choice:
                    C for creating a band
                    U for updating a band
                    Any other key to exit tax band management: """
                )
                .strip()
                .lower()
            )
            if action not in ("c", "u"):
                print("---- Exiting TaxBand Management -----")
                break
            band_name = input("Give the tax band name: ").strip().lower()
            if action == "c":
                self.create_band(band_name)
            elif action == "u":
                self.update_band(band_name)
        return self.tax_bands

    def create_band(self, band_name):
        """
        Create a tax band.

        Args:
            band_name (str): The name of the tax band.
        """
        self.tax_bands[band_name] = self.get_band_values()

    def update_band(self, band_name):
        """
        Update a tax band.

        Args:
            band_name (str): The name of the tax band to update.
        """
        if not self.tax_bands or not (band_name in self.tax_bands):
            print(
                f"No such band with name '{band_name}' exists. Try creating a new band."
            )
            return
        self.tax_bands[band_name] = self.get_band_values()
        pprint(self.tax_bands)

    @staticmethod
    def num_range_to_float_conversion(value):
        """
        Convert a number representation to a float value.

        Args:
            value (str): The number representation to convert.

        Returns:
            float: The converted float value.
        """
        if "k" in value:
            value = float(value.replace("k", "000"))
        elif "m" in value:
            value = float(value.replace("m", "000000"))
        else:
            value = float(value)
        return value

    @staticmethod
    def get_band_values():
        """
        Get the tax band values from user input.

        Returns:
            dict: A dictionary representing the tax bands.
        """
        band_details = input(
            rf"""{'-'* 50}
        Enter tax bands, all in the same line, semicolon-separated (e.g., 0-10K:2.4%):
        Ex: 0-10k: 2.5% ;10k - 20k: 5%;20k - 50k: 10%; \> 50k: 20%
            0-10k: 2.5 ;10k - 20k: 5;20k - 50k: 10; > 50k: 20
            0-10k: 2.5 ;10k - 20k: 5;20k - 50m: 10; > 50m: 20
        """
        )
        # input data cleansing
        band_details = re.sub(r"[>\\% ]", "", band_details).lower()

        # Transformations
        band_details = band_details.replace("m", "000000")
        band_details = band_details.replace("k", "000")

        # Process each segment and extract the range and percentage
        slabs = {}
        for segment in band_details.split(";"):
            range_str, percentage_str = segment.split(":")

            # Extract the lower and upper range values
            if "-" in range_str:
                lower_range, upper_range = map(float, range_str.split("-"))
            else:
                lower_range, upper_range = float(range_str), float("inf")

            # Check for any gaps between slabs
            if slabs and lower_range != max(slabs.keys()):
                print(
                    "Invalid slab range. There is a gap between slabs. Please try again"
                )
                break
            # Add the range and percentage to the dictionary
            slabs[upper_range] = float(percentage_str)
        return slabs


class TaxCalculator(TaxBandGenerator):
    def __init__(self, tax_bands=None) -> None:
        super().__init__()
        print("\nExisting TAX_BANDS:")
        self.tax_bands = tax_bands or self.get_user_input()
        pprint(self.tax_bands)
        print()

    def calculate_tax(self, desired_tax_band, salary_to_check):
        if not desired_tax_band:
            print(f"InVALID TAX_BAND: {desired_tax_band}")
            return
        if salary_to_check < 0:
            print(f"INVALID salary: {salary_to_check}")
            return
        bands = self.tax_bands.get(desired_tax_band)
        if not bands:
            print("Not Such TAX_BAND register")
            return

        total_tax = 0.0
        remaining_income = salary_to_check

        for slab_end, slab_rate in bands.items():
            if remaining_income <= 0:
                break
            slab_income = remaining_income if remaining_income <= slab_end else slab_end
            total_tax += slab_income * (slab_rate / 100)
            remaining_income -= slab_income

        total_tax = round(total_tax, 2)
        print(
            f"For TaxBand:{desired_tax_band:6} & Salary: {salary_to_check:7}, tax owed is {total_tax:7}"
        )
        return total_tax


def main():
    tc = TaxCalculator()

    while True:
        if not tc.tax_bands:
            print("NO TAX BAND IS REGISTERED YET. PLEASE CREATE ONE")
            tc.get_user_input()
        else:
            user_input = (
                input(
                    f"""{'-'* 50}
                Provide  TaxBandName salary (space separated):
                    ex: ukband 23456
                        usband 32334324
                """
                )
                .strip()
                .lower()
            )

            # cleansing and transformations
            user_input = user_input.replace(
                ",", " "
            )  # To handle , separated inputs too
            try:
                band, salary = user_input.split(" ")
                tc.calculate_tax(band, float(salary))
            except Exception as ex:
                print(f"Invalid Input.{ex} Try again")


if __name__ == "__main__":
    main()
