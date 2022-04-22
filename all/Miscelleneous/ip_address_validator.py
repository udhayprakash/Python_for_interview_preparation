#!/usr/bin/python
"""
Purpose: Validating Ipv4 and Ipv6 addresses
"""
import re


def zero_preceding_check(given_address):
    for each_byte in given_address.split("."):
        if each_byte.startswith("0") and int(each_byte) >= 8:
            return False
    return True


def validate_addresses(addresses):
    result = []
    for each_address in addresses:
        ipv4_pattern = r"^[0-2]?\d{1,2}\.[0-2]?\d{1,2}\.[0-2]?\d{1,2}\.[0-2]?\d{1,2}$"
        ipv6_pattern = r"^(?:(?:[0-9A-Fa-f]{1,4}:){6}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::(?:[0-9A-Fa-f]{1,4}:){5}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){4}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){3}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,2}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){2}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,4}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(?:(?:[0-9A-Fa-f]{1,4}:){,6}[0-9A-Fa-f]{1,4})?::)$"
        ipv4res = re.findall(ipv4_pattern, each_address)
        ipv6res = re.findall(ipv6_pattern, each_address)
        if ipv4res and zero_preceding_check(each_address):
            result.append("IPv4")
        elif ipv6res:
            result.append("IPv6")
        else:
            result.append("Neither")
    return result


if __name__ == "__main__":
    print(
        validate_addresses(
            [
                "000.012.234.23",
                "666.666.23.23",
                ".213.123.23.32",
                "23.45.22.32.",
                # '272:2624:235e:3bc2:c46d:682:5d46:638g',
                "1:22:333:4444",
            ]
        )
    )
    assert validate_addresses(
        ["121.18.19.20", "0.12.12.34", "121.234.12.12", "23.45.12.56", "0.1.2.3"]
    ) == ["IPv4", "IPv4", "IPv4", "IPv4", "IPv4"]
    assert validate_addresses(
        [
            "2001:0db8:0000:0000:0000:ff00:0042:8329",
            "2001:db8:0:0:0:ff00:42:8329",
            "2001:db8::ff00:42:8329",
            "0000:0000:0000:0000:0000:0000:0000:0001",
            "::1",
        ]
    ) == ["IPv6", "IPv6", "IPv6", "IPv6", "IPv6"]
    assert validate_addresses(
        [
            "000.012.234.23",
            "666.666.23.23",
            ".213.123.23.32",
            "23.45.22.32.",
            "272:2624:235e:3bc2:c46d:682:5d46:638g",
            "1:22:333:4444",
        ]
    ) == ["Neither", "Neither", "Neither", "Neither", "Neither", "Neither"]
