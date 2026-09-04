#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):

    def count_swaps(values, target):
        # Stores: number -> current index in values
        position = {value: index for index, value in enumerate(values)}

        swaps = 0

        for i in range(len(values)):
            # If correct value is already at index i, no swap is needed
            if values[i] == target[i]:
                continue

            correct_value = target[i]
            correct_index = position[correct_value]

            # Value currently at i will be moved to correct_index
            current_value = values[i]

            # Perform the swap
            values[i], values[correct_index] = values[correct_index], values[i]

            # Update positions after swap
            position[current_value] = correct_index
            position[correct_value] = i

            swaps += 1

        return swaps

    ascending = sorted(arr)
    descending = ascending[::-1]

    # Use arr.copy() both times because count_swaps changes the list
    swaps_ascending = count_swaps(arr.copy(), ascending)
    swaps_descending = count_swaps(arr.copy(), descending)

    return min(swaps_ascending, swaps_descending)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna