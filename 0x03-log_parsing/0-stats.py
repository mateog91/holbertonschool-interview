#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:
"""

if __name__ == '__main__':
    import sys

    def statistics(status_counts_dict, total_file_size):
        """ prints statistics at that moment"""
        print("File size: {:d}".format(total_file_size))
        for code in sorted(status_counts_dict.keys()):
            value = status_counts_dict[code]
            if value != 0:
                print("{}: {}".format(code, value))

    # initialize variables
    status_codes = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    total_file_size = 0
    count = 0
    try:
        # catch input line
        for line in sys.stdin:
            # count and split line
            line = line.split()
            count += 1

            try:
                status_code, file_size = line[-2], int(line[-1])
                total_file_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1

            except Exception:
                pass

            if count % 10 == 0:
                statistics(status_codes, total_file_size)

        statistics(status_codes, total_file_size)

    except (KeyboardInterrupt, SystemExit):
        statistics(status_codes, total_file_size)
        raise
