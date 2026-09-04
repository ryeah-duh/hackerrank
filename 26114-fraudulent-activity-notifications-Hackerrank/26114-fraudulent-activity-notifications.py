#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    counts = [0] * 201

    for i in range(d):
        counts[expenditure[i]] += 1

    notifications = 0

    def twice_median():
        count_so_far = 0

        if d % 2 == 1:
            middle = d // 2 + 1

            for value in range(201):
                count_so_far += counts[value]

                if count_so_far >= middle:
                    return 2 * value

        else:
            first_middle = d // 2
            second_middle = first_middle + 1
            first_value = None

            for value in range(201):
                count_so_far += counts[value]

                if first_value is None and count_so_far >= first_middle:
                    first_value = value

                if count_so_far >= second_middle:
                    return first_value + value

    for i in range(d, len(expenditure)):
        if expenditure[i] >= twice_median():
            notifications += 1

        counts[expenditure[i - d]] -= 1
        counts[expenditure[i]] += 1

    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna