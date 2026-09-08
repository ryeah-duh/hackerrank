#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    if m * w >= n:
        return 1

    passes = 0
    candy = 0
    min_passes = sys.maxsize

    while candy < n:
        # Calculate passes needed to reach target 'n' without any more purchases
        steps_to_n = (n - candy + m * w - 1) // (m * w)
        min_passes = min(min_passes, passes + steps_to_n)

        # Fast-forward if we cannot afford even 1 purchase
        if candy < p:
            needed = p - candy
            skip = (needed + m * w - 1) // (m * w)
            passes += skip
            candy += skip * m * w
            if candy >= n:
                min_passes = min(min_passes, passes)
                break

        # Spend candies to buy assets
        buy = candy // p
        candy %= p

        # Equalize m and w to maximize production (m * w)
        diff = abs(m - w)
        if m < w:
            add_m = min(buy, diff)
            m += add_m
            buy -= add_m
        else:
            add_w = min(buy, diff)
            w += add_w
            buy -= add_w

        # Distribute remaining purchases evenly between m and w
        m += buy // 2
        w += buy - (buy // 2)

        # Run 1 pass with newly upgraded resources
        passes += 1
        candy += m * w

    return min(min_passes, passes)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna