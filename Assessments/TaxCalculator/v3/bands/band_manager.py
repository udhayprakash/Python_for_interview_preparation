"""
Manages tax bands
"""

import json
from decimal import Decimal


class BandManager:
    def __init__(self):
        self.bands = self.load_bands()

    def load_bands(self):
        try:
            with open("bands.json") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_bands(self):
        with open("bands.json", "w") as f:
            json.dump(self.bands, f, indent=2)

    def create_band(self, logger, name, slabs):
        self.bands[name] = self.parse_slabs(slabs)
        self.save_bands()
        logger.info(f"Created band: {name}")

    def list_bands(self, logger):
        logger.info(f"Tax bands: {self.bands}")

    def delete_band(self, logger, name):
        if name in self.bands:
            del self.bands[name]
            self.save_bands()
            logger.info(f"Deleted band: {name}")
        else:
            logger.error(f"No band with name {name} found")

    def set_default_band(self, logger, name):
        if name in self.bands:
            self.bands["default"] = name
            self.save_bands()
            logger.info(f"Set default band to: {name}")
        else:
            logger.error(f"No band with name {name} found")

    def parse_slabs(self, slab_strings):
        slabs = {}
        for s in slab_strings:
            limits, rate_str = s.split(":")
            lower, upper = (Decimal(x) for x in limits.split("-"))
            rate = Decimal(rate_str.strip("%")) / 100
            slabs[upper] = rate
        return slabs
