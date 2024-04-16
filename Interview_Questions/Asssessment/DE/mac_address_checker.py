"""
Problem:
    Network devices are identified by its MAC address,
    which is 6 byte / 12 hex characters (1234ABCD5678 for example).

    A RESTful API exists to check the status of a network device (http://localhost:8000/device/check/1234ABCD5678, another example.)

Assume a large dataset exists that contains a large set of device identifiers in the form of MAC addresses (over 10,000+).
The RESTful API can take around 5 seconds to complete a single status check,
so checking device status is a relatively long running task.
Also assume that the device identifiers (MAC addresses) come from a data source / stream that separates each MAC address by a newline.

Write a python solution that processes MAC address with the goal of:
minimizing runtime, minimizing resource usage and generalizing methods and procedures.
"""
import concurrent.futures
import os

import requests
from security import safe_requests


class NetworkDeviceChecker:
    def __init__(self, api_base_url, max_workers=5):
        self.api_base_url = api_base_url
        self.max_workers = max_workers

    def check_mac_address(self, mac_address):
        """Check the status of a single MAC address using the RESTful API."""
        try:
            response = safe_requests.get(self.api_base_url + mac_address)
            response.raise_for_status()

            result = {
                "mac_address": mac_address,
                "status": response.status_code == 200,
                "response": response.json(),
            }
        except requests.exceptions.RequestException as e:
            result = {
                "mac_address": mac_address,
                "status": False,
                "error": f"RequestException: {str(e)}",
            }
        except Exception as e:
            result = {
                "mac_address": mac_address,
                "status": False,
                "error": f"Error: {str(e)}",
            }
        return result

    def process_mac_addresses(self, mac_addresses):
        """Process MAC addresses and check their status using the RESTful API."""
        results = []

        # Use ThreadPoolExecutor to concurrently check the status of multiple MAC addresses
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            futures = [
                executor.submit(self.check_mac_address, mac_address.strip())
                for mac_address in mac_addresses
            ]

            # Collect the results as they become available
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())

        return results


def read_mac_addresses_from_file(file_path):
    if not os.path.exists(file_path):
        raise Exception(f"file {file_path} doesnt exist")
    with open(file_path) as f:
        mac_addresses = f.readlines()
    return mac_addresses


if __name__ == "__main__":
    api_base_url = "http://localhost:8000/device/check/"
    network_device_checker = NetworkDeviceChecker(api_base_url)

    mac_addresses = read_mac_addresses_from_file("mac_addresses.txt")

    # Process MAC addresses and check their status using the RESTful API
    results = network_device_checker.process_mac_addresses(mac_addresses)

    for result in results:
        print(result)
