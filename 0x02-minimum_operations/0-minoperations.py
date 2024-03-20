#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    '''
    if not isinstance(n, int):
        return 0
    count = 0
    clipboard = 0
    start = 1
    # print('H', end='')
    while start < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = start
            start += clipboard
            count += 2
            # print('-(11)->{}'.format('H' * start), end='')
        elif n - start > 0 and (n - start) % start == 0:
            # copy all and paste
            clipboard = start
            start += clipboard
            count += 2
            # print('-(11)->{}'.format('H' * start), end='')
        elif clipboard > 0:
            # paste
            start += clipboard
            count += 1
            # print('-(01)->{}'.format('H' * start), end='')
    # print('')
    return count
