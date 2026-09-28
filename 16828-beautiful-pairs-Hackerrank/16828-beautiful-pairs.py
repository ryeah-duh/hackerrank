#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    from collections import Counter

    countA = Counter(A)
    countB = Counter(B)

    pairs = 0

    # Count maximum matching pairs
    for value in countA:
        pairs += min(countA[value], countB[value])

    n = len(A)

    # Exactly one element of B must be changed
    if pairs == n:
        # All elements already matched, so changing one breaks a pair
        return pairs - 1
    else:
        # Otherwise we can change one unmatched element to create a pair
        return pairs + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna