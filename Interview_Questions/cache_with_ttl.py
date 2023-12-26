import time
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from functools import update_wrapper, wraps
from typing import Dict, List, Tuple
import secrets


# ttls = {
#     'usd': 10,
#     'INR', 5,
#     ..
# }
def cache(ttl):
    def inner_func(func):
        cache_data = {}

        @wraps(func)
        def inner(*args, **kwargs):
            trans_name = "-".join(args[1:])
            print("ARGS", trans_name, cache_data)

            # to get from cache
            if cache_data.get(trans_name):
                data, ttl_val, start_time = cache_data[trans_name]
                if datetime.now() - start_time < ttl_val:
                    return data

            # run only when no cache
            result = func(*args, **kwargs)
            cache_data[trans_name] = (
                result,
                ttl,
                datetime.now(),
            )  # data, 10s, datetime.now()

        return inner

    return inner_func


@dataclass
class ExchangeRateApiClient:
    def _make_api_call(self, base_currency: str) -> Dict[str, Decimal]:
        response: Dict[str, Decimal] = {
            "EUR": {
                "GBP": Decimal("0.882047"),
                "USD": Decimal("1.233961"),
                "CAD": Decimal("1.472041"),
                "CHF": Decimal("0.933058"),
            }
        }
        time.sleep(2)  # Simulate network delay
        return response.get(base_currency, {})

    @cache(10)  # 10 sec TTL
    def get_rate(self, base_currency: str, target_currency: str) -> Decimal:
        print(f"API called for currency pair {base_currency}/{target_currency}")
        return self._make_api_call(base_currency).get(target_currency)


client = ExchangeRateApiClient()
times = []
currency_conversions: List[Tuple[str, str]] = [
    ("EUR", "GBP"),
    ("EUR", "USD"),
    ("EUR", "CAD"),
    ("EUR", "CHF"),
]

for i in range(4):
    tic = time.perf_counter()
    base_currency, target_currency = secrets.SystemRandom().choice(currency_conversions)
    rate: Decimal = client.get_rate(base_currency, target_currency)
    toc = time.perf_counter()
    times.append(toc - tic)

print(f"Execution times: {times}")
