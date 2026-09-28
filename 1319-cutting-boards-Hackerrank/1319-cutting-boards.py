#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'boardCutting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost_y
#  2. INTEGER_ARRAY cost_x
#

def boardCutting(cost_y, cost_x):
    MOD = 10**9 + 7

    # Make expensive cuts first
    cost_y.sort(reverse=True)
    cost_x.sort(reverse=True)

    y_pieces = 1
    x_pieces = 1

    i = 0
    j = 0
    total = 0

    while i < len(cost_y) and j < len(cost_x):

        if cost_y[i] >= cost_x[j]:
            # Horizontal cut crosses all current x pieces
            total += cost_y[i] * x_pieces
            y_pieces += 1
            i += 1
        else:
            # Vertical cut crosses all current y pieces
            total += cost_x[j] * y_pieces
            x_pieces += 1
            j += 1

        total %= MOD

    # Remaining horizontal cuts
    while i < len(cost_y):
        total += cost_y[i] * x_pieces
        total %= MOD
        y_pieces += 1
        i += 1

    # Remaining vertical cuts
    while j < len(cost_x):
        total += cost_x[j] * y_pieces
        total %= MOD
        x_pieces += 1
        j += 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        n = int(first_multiple_input[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna