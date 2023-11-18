# Regular expressions

import re

with open("ips.txt", "r") as ip_addresses:
    all_ips = ip_addresses.readlines()
    all_ips = [ip.rstrip() for ip in all_ips]
    for ip in all_ips:
        if re.fullmatch(r'^((0|1\d{0,2}|2([0-4]\d?|5[0-5]?)|[3-9]\d?|\d)\.){3}(0|1\d{0,2}|2([0-4]\d?|5[0-5]?)|[3-9]\d?|\d)$', ip):
            print(ip, "is correct")
        else:
            print(ip, "is incorrect")
