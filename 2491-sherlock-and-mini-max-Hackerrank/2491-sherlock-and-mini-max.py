#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndMinimax' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER p
#  3. INTEGER q
#

def sherlockAndMinimax(arr, p, q):
    arr.sort()

    # Possible optimal values include p, q,
    # and midpoints between adjacent array values.
    candidates = {p, q}

    for i in range(len(arr) - 1):
        mid = (arr[i] + arr[i + 1]) // 2

        if p <= mid <= q:
            candidates.add(mid)

        # Also check mid + 1 because of integer rounding
        if p <= mid + 1 <= q:
            candidates.add(mid + 1)

    best_m = p
    best_distance = -1

    # Find distance to nearest element using binary search
    import bisect

    for m in candidates:
        pos = bisect.bisect_left(arr, m)

        distance = float('inf')

        if pos < len(arr):
            distance = min(distance, abs(arr[pos] - m))

        if pos > 0:
            distance = min(distance, abs(arr[pos - 1] - m))

        # Maximize minimum distance.
        # On a tie, choose the smaller m.
        if distance > best_distance:
            best_distance = distance
            best_m = m
        elif distance == best_distance and m < best_m:
            best_m = m

    return best_m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna