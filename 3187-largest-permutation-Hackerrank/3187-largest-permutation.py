#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    n = len(arr)

    # Store current position of each value
    position = {value: i for i, value in enumerate(arr)}

    for i in range(n):
        if k == 0:
            break

        # Largest value that should be at index i
        desired = n - i

        if arr[i] != desired:
            desired_index = position[desired]

            # Current value at index i
            current = arr[i]

            # Swap
            arr[i], arr[desired_index] = arr[desired_index], arr[i]

            # Update positions
            position[current] = desired_index
            position[desired] = i

            k -= 1

    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna