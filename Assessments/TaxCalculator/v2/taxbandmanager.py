"""
Purpose: This python script deals with Tax Band Management
"""
import json
import os
import re


class TaxBandManager:
    def __init__(self, logger, file_path):
        self.logger = logger
        self.file_path = file_path
        self.tax_bands = self.load_tax_bands()

    def load_tax_bands(self):
        self.logger.debug(f"Loading tax bands from {self.file_path}")
        try:
            with open(self.file_path) as file:
                return json.load(file).get("TaxBands")
        except FileNotFoundError as ex:
            self.logger.error(f"No such file with name {self.file_path}")
        except Exception as ex:
            self.logger.error(str(ex))
        return {}

    @staticmethod
    def get_band_values():
        """
        Get the tax band values from user input.

        Returns:
            dict: A dictionary representing the tax bands.
        """
        band_details = input(
            rf"""{'-' * 50}
        Enter tax bands, all in the same line, semicolon-separated (e.g., 0-10K:2.4%):
        Ex: 0-10k: 2.5% ;10k - 20k: 5%;20k - 50k: 10%; \> 50k: 20%
            0-10k: 2.5 ;10k - 20k: 5;20k - 50k: 10; > 50k: 20
            0-10k: 2.5 ;10k - 20k: 5;20k - 50m: 10; > 50m: 20
        """
        )
        # input data cleansing
        band_details = re.sub(r"[>\\% ]>", "", band_details).lower()

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

    def save_tax_bands(self):
        self.logger.debug(f"saving tax bands to {self.file_path}")
        with open(self.file_path, "w") as file:
            json.dump({"TaxBands": self.tax_bands}, file, indent=4)

    def delete_band_file(self):
        self.logger.debug(f"Deleting tax bands file(if present): {self.file_path}")
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def list_band(self, band_name):
        self.logger.debug(f"Listing details of band:{band_name}")
        if band_name in self.tax_bands:
            self.logger.info(f"  {band_name}: {self.tax_bands[band_name]}")
        else:
            self.logger.info(f"NO tax band registered with name {band_name}")

    def list_bands(self):
        self.logger.debug("Listing all tax bands:")
        if not self.tax_bands:
            self.logger.info("  No tax bands found")
            return
        for band_name, band_values in self.tax_bands.items():
            self.logger.info(f"  {band_name}: {band_values}")

    def create_band(self, band_name, band_values):
        self.tax_bands[band_name] = self.extra_band_slabs(band_values)
        self.save_tax_bands()
        self.logger.info(f"Tax band '{band_name}' created with values: {band_values}")

    def update_band(self, band_name, band_values):
        if band_name in self.tax_bands:
            self.tax_bands[band_name] = band_values
            self.save_tax_bands()
            self.logger.info(
                f"Tax band '{band_name}' updated with values: {band_values}"
            )
        else:
            self.logger.info(f"No tax band found with the name '{band_name}'")

    def delete_band(self, band_name):
        if band_name in self.tax_bands:
            del self.tax_bands[band_name]
            self.save_tax_bands()
            self.logger.info(f"Tax band '{band_name}' deleted")
        else:
            self.logger.info(f"No tax band found with the name '{band_name}'")

    def set_default_band(self, band_name):
        if band_name in self.tax_bands:
            self.tax_bands["default"] = band_name
            self.save_tax_bands()
            self.logger.info(f"Default tax band set to '{band_name}'")
        else:
            self.logger.info(f"No tax band found with the name '{band_name}'")

    def extra_band_slabs(self, band_details):
        self.logger.info(f"list:{band_details}")
        band_details = "".join(band_details)
        self.logger.info(f"str:{band_details}")

        # input data cleansing
        band_details = re.sub(r"[>%\\ ]", "", band_details).lower()
        self.logger.info(f"clean:{band_details}")

        # Transformations
        band_details = band_details.replace("m", "000000")
        band_details = band_details.replace("k", "000")
        self.logger.info(f"replace:{band_details}")

        # Process each segment and extract the range and percentage
        slabs = {}
        self.logger.info(f"band_details:{band_details.split(';')}")
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
