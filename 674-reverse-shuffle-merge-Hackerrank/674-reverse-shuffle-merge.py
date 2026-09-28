#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    total = Counter(s)

    # A contains exactly half of every character in s
    required = {ch: total[ch] // 2 for ch in total}

    used = Counter()
    remaining = Counter(s)

    result = []

    # Read backwards because s contains reverse(A)
    for ch in reversed(s):
        remaining[ch] -= 1

        # Already have enough copies of this character
        if used[ch] >= required[ch]:
            continue

        # Remove larger characters when it is still possible
        # to obtain enough of them later
        while result:
            last = result[-1]

            if (
                last > ch
                and used[last] - 1 + remaining[last] >= required[last]
            ):
                result.pop()
                used[last] -= 1
            else:
                break

        result.append(ch)
        used[ch] += 1

    return ''.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna