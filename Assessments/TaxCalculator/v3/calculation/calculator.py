"""
Calculates tax amount based on salary and tax band
"""

from decimal import Decimal


class TaxCalculator:
    def calculate_tax(self, logger, band, salary):
        bands = BandManager().bands

        if band in bands:
            tax_band = bands[band]
        elif "default" in bands:
            tax_band = bands["default"]
        else:
            logger.error("No valid tax band provided")
            return

        tax = Decimal(0)
        for upper_limit, rate in tax_band.items():
            if salary > upper_limit:
                tax += (salary - upper_limit) * rate

        logger.info(f"Tax on salary {salary} in band {band} is {tax}")
        return tax
