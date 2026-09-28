#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    delivery = []

    for i in range(len(orders)):
        order_time = orders[i][0]
        prep_time = orders[i][1]

        serve_time = order_time + prep_time

        # Store serve time and customer number
        delivery.append((serve_time, i + 1))

    # Sort by serve time, then customer number
    delivery.sort()

    return [customer for serve_time, customer in delivery]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna