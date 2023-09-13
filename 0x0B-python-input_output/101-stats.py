#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys
import re


p = re.compile('.[2-5]0[0-5] [0-9]+')
count = 0
status_codes_dict = {}
total_file_size = 0
try:
    for line in sys.stdin:
        search_result = p.search(line)
        code_file_size = search_result.group().split()
        status_code = code_file_size[0]
        file_size = code_file_size[1]

        if status_code in status_codes_dict:
            status_codes_dict[status_code] = status_codes_dict[status_code] + 1
        else:
            status_codes_dict[status_code] = 1

        total_file_size += int(file_size)

        count += 1

        if count == 10:
            print(f"File size: {total_file_size}")
            dict_keys = list(status_codes_dict.keys())
            dict_keys.sort()
            for k in dict_keys:
                print(f"{k}: {status_codes_dict[k]}")
            count = 0
except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    dict_keys = list(status_codes_dict.keys())
    dict_keys.sort()
    for k in dict_keys:
        print(f"{k}: {status_codes_dict[k]}")
