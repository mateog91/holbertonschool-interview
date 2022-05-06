#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:

    Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C), print these
     statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
        (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesnt appear or is not an integer, dont print
            anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order
"""
import signal
import sys


def statistics(status_counts_dict, total_file_size):
    list_tupples = [(key, value) for key, value in status_counts_dict.items()]
    list_tupples.sort(key=lambda y: y[0])
    print(f"File size: {total_file_size}")
    [print(f"{tup[0]}: {tup[1]}") for tup in list_tupples if tup[1] > 0]


def handler(signum, frame):
    statistics(status_code_counts, total_file_size)
    exit(1)


signal.signal(signal.SIGINT, handler)


# initialize variables
possible_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_counts = {element: 0 for element in possible_status_codes}
total_file_size = 0
count = 0

# catch input line
for line in sys.stdin:
    # print(count)
    # split inputline
    line = line.split()

    # check line has correct format
    if len(line) == 9:
        # print(len(line))
        try:
            status_code, file_size = int(line[7]), int(line[8])
            # print(f"status code: {status_code} file size: {file_size}")
            # print(status_code in possible_status_codes)
            # check if is valid status code
            if status_code in possible_status_codes:
                count += 1
                total_file_size += file_size
                status_code_counts[status_code] += 1
                if count % 10 == 0:
                    statistics(status_code_counts, total_file_size)

        except:
            pass
