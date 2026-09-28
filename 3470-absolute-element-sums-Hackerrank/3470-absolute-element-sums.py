#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'playingWithNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#
def playingWithNumbers(arr, queries):
    arr.sort()
    n = len(arr)

    # Prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    result = []
    shift = 0

    import bisect

    for q in queries:
        shift += q

        # We need the first original value where:
        # arr[i] + shift >= 0
        # => arr[i] >= -shift
        idx = bisect.bisect_left(arr, -shift)

        # Elements before idx are negative after shifting
        left_sum = prefix[idx]
        left_count = idx

        # Elements from idx onward are non-negative
        right_sum = prefix[n] - prefix[idx]
        right_count = n - idx

        # Sum of absolute values
        negative_part = -(left_sum + left_count * shift)
        positive_part = right_sum + right_count * shift

        result.append(negative_part + positive_part)

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    queries = list(map(int, input().rstrip().split()))

    result = playingWithNumbers(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna