## Tax Calculator CLI application

### Problem Statement

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

        0-10k: 2.5% ;10k - 20k: 5%;20k - 50k: 10%; \> 50k: 20%
        0-10k: 2.5 ;10k - 20k: 5;20k - 50k: 10; > 50k: 20
        0-10k: 2.5 ;10k - 20k: 5;20k - 50m: 10; > 50m: 20

### USAGE

    1) To create a new tax band

            python tax_calculator2.py taxband create ukband 0-10k: 2.5% ;10k - 20k: 5%;20k - 50k: 10%; \> 50k: 20%

    1) To List all the existing TaxBands

            python tax_calculator2.py taxband list

    2) To List a specific TaxBand

            python tax_calculator2.py taxband list ukband

    3) To delete a specific tax band

            python tax_calculator2.py taxband delete ukband

    4) To delete all the saved tax bands,

            python tax_calculator2.py taxband deleteall

### Observations

    !) In a financial Organization, Imphasis with me on
            - Concurrency
            - Code Readability
            - documentaion
            - Relying on Core language Libraries, to Avoid Future (deep) dependencies risk
       I ensured to address all these aspects

    2) Design Patterns:
        I used Memoization design pattern to store results, for a given band namme and salary pair; until the tax band slabs were updated/deleted.

    3) Ease-of-Use: Any tool can be success, based on its Ease-of-Use
        I ensured to make it user-friendly, adding all typical options (in usage perspective)
        Tool Usage is self explanatory with -h option to get help at any (or sub) level

    4) Reliability: Unit tests will be the main pillar in ensure code reliability
        ( ensured to add as many unit tests as possible, to maximize the code coverage.

### Future Enhancement

    A web application (Flask/FastAPI) can be created for adding further ease
