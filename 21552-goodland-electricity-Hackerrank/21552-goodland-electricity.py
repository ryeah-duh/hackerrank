#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    n = len(arr)
    plants = 0
    current = 0

    while current < n:
        # Furthest possible position for a power plant
        position = min(n - 1, current + k - 1)

        # Leftmost valid position we can still use
        minimum = max(0, current - k + 1)

        # Search backwards for the furthest available plant
        while position >= minimum and arr[position] == 0:
            position -= 1

        # No plant can cover the current city
        if position < minimum:
            return -1

        plants += 1

        # This plant covers through position + k - 1,
        # so the next uncovered city is position + k
        current = position + k

    return plants


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna