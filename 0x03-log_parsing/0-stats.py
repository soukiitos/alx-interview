#!/usr/bin/python3
'''Read stdin line by line and computes metrics'''
import sys


if __name__ == "__main__":
    code_count = {
            200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
            }
    tot_size = [0]

    def check_stat(line):
        '''Define check_stat'''
        try:
            line = line[:-1]
            spl_w = line.split(" ")
            tot_size[0] += int(spl_w[-1])
            code = int(spl_w[-2])
            if code in code_count:
                code_count[code] += 1
        except ValueError:
            pass

    def print_stats():
        '''Define print_stats'''
        print("File size: {}".format(tot_size[0]))
        for i in sorted(code_count.keys()):
            if code_count[i]:
                print("{}: {}".format(i, code_count[i]))
    j = 1
    try:
        for line in sys.stdin:
            check_stat(line)
            if j % 10 == 0:
                print_stats()
            j += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
