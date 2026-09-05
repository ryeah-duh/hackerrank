#!/bin/python3

import os
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    x.sort()
    n = len(x)
    num_transmitters = 0
    i = 0

    while i < n:
        num_transmitters += 1
        
        # Step 1: Find the rightmost house that can still cover x[i]
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1
            
        # The transmitter is placed at x[i - 1]
        transmitter_loc = x[i - 1]
        
        # Step 2: Skip all houses to the right covered by this transmitter
        coverage_limit = transmitter_loc + k
        while i < n and x[i] <= coverage_limit:
            i += 1

    return num_transmitters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')
    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna