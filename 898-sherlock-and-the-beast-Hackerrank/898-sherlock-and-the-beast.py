#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Try to maximize the number of 5s
    for fives in range(n, -1, -1):
        threes = n - fives

        # Number of 5s must be divisible by 3
        # Number of 3s must be divisible by 5
        if fives % 3 == 0 and threes % 5 == 0:
            print('5' * fives + '3' * threes)
            return

    print(-1)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna