#!/usr/bin/python3
'''Read stdin line by line and computes metrics'''
import sys


tot_size = 0
line_count = 0
code_count = {
        200: 0, 301: 0, 400: 0, 401: 0, 404: 0, 405: 0, 500: 0
        }

try:
    for line in sys.stdin:
        line = line.strip()
        p_line = line.split()
        if len(p_line) != 7:
            continue
        try:
            f_size = int(p_line[-1])
            s_code = int(p_line[-2])
        except ValueError:
            continue
        tot_size += f_size
        code_count[s_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print(f'Total file size: {tot_size}')
            for i in sorted(code_count.keys()):
                if code_count[i] > 0:
                    print(f'{i}: {code_count[i]}')


except KeyboardInterrupt:
    '''Handle The Interruption Keyboard'''
    print(f'Total file size: {tot_size}')
    for i in sorted(code_count.keys()):
        if code_count[i] > 0:
            print(f'{i}: {code_count[i]}')
