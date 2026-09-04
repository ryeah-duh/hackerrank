#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right


#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    sorted_arr = []
    shifts = 0

    for i, value in enumerate(arr):
        # Position where value should be inserted
        position = bisect_right(sorted_arr, value)

        # Elements after position must shift right
        shifts += i - position

        # Insert value while maintaining sorted_arr in sorted order
        sorted_arr.insert(position, value)

    return shifts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna