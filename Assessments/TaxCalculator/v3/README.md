## TaxCalculator

As each country has separate tax bands, this project will create a tax calculator for calculating tax on salary, for the given taxband.


To calculate the tax owed
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

        0-10k: 2.5% ;10k - 20k: 5%;20k - 50k: 10%; \> 50k: 20%
        0-10k: 2.5 ;10k - 20k: 5;20k - 50k: 10; > 50k: 20
        0-10k: 2.5 ;10k - 20k: 5;20k - 50m: 10; > 50m: 20


### USAGE

    1) To create a new tax band

        python tax_calculator.py band create ukband 0-10k:2.5%;10k-20k:5%;20k-50k:10%; \> 50k:20%

    2) To List all the existing TaxBands

            python tax_calculator.py band list

    2) To List a specific TaxBand

            python tax_calculator.py band list ukband

    3) To delete a specific tax band

            python tax_calculator.py band delete ukband

    4) To delete all the saved tax bands,

            python tax_calculator.py band delete
