#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    n = len(price)
    # Map original price to its year index
    indices = {val: i for i, val in enumerate(price)}
    
    # Sort prices in ascending order
    sorted_price = sorted(price)
    
    min_loss = float('inf')
    
    # Check adjacent pairs in sorted order
    for i in range(1, n):
        buy_price = sorted_price[i]
        sell_price = sorted_price[i - 1]
        
        # A valid transaction requires buying before selling (buy index < sell index)
        if indices[buy_price] < indices[sell_price]:
            min_loss = min(min_loss, buy_price - sell_price)
            
    return min_loss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna