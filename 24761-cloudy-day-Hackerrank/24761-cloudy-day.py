#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    n = len(p)
    m = len(y)

    # Sort towns by location
    towns = sorted(zip(x, p))

    # Clouds represented as:
    # (left boundary, right boundary, cloud index)
    clouds = []

    for i in range(m):
        left = y[i] - r[i]
        right = y[i] + r[i]
        clouds.append((left, right, i))

    clouds.sort()

    # Population already sunny without removing any cloud
    sunny_population = 0

    # Population that becomes sunny if a particular cloud is removed
    exclusive = [0] * m

    # Active clouds:
    # heap entries are (right_boundary, cloud_index)
    active = []

    cloud_index = 0

    for town_position, population in towns:

        # Add clouds whose left boundary has reached this town
        while (
            cloud_index < m
            and clouds[cloud_index][0] <= town_position
        ):
            left, right, idx = clouds[cloud_index]
            heapq.heappush(active, (right, idx))
            cloud_index += 1

        # Remove clouds that no longer cover this town
        while active and active[0][0] < town_position:
            heapq.heappop(active)

        # No cloud covers this town
        if len(active) == 0:
            sunny_population += population

        # Exactly one cloud covers this town
        elif len(active) == 1:
            _, idx = active[0]
            exclusive[idx] += population

        # If 2+ clouds cover the town, removing only one
        # cloud cannot make it sunny.

    # Remove the cloud that reveals the largest population
    best_extra = max(exclusive) if exclusive else 0

    return sunny_population + best_extra


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna