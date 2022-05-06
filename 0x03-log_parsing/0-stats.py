#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:
"""

if __name__ == '__main__':
    import sys

    def statistics(status_counts_dict, total_file_size):
        """ prints statistics at that moment"""
        list_tupples = [(key, value)
                        for key, value in status_counts_dict.items()]
        list_tupples.sort(key=lambda y: y[0])
        print("File size: {}".format(total_file_size))
        [print("{}: {}".format(tup[0], tup[1]))
         for tup in list_tupples if tup[1] > 0]

    # initialize variables
    possible_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    status_code_counts = {element: 0 for element in possible_status_codes}
    total_file_size = 0
    count = 0
    try:
        # catch input line
        for line in sys.stdin:
            # count and split line
            line = line.split()
            count += 1

            # check line has correct format

            if count != 0 and count % 10 == 0:
                statistics(status_code_counts, total_file_size)
            try:
                status_code, file_size = int(line[-2]), int(line[-1])

                if status_code in possible_status_codes:
                    total_file_size += file_size
                    status_code_counts[status_code] += 1

            except Exception:
                pass
    except (KeyboardInterrupt, SystemExit):
        statistics(status_code_counts, total_file_size)
        raise
