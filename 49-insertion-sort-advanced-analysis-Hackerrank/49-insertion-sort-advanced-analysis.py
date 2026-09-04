#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    temp = [0] * len(arr)

    def merge_sort(left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        shifts = merge_sort(left, mid)
        shifts += merge_sort(mid + 1, right)

        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                shifts += mid - i + 1
                j += 1

            k += 1

        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1

        for index in range(left, right + 1):
            arr[index] = temp[index]

        return shifts

    return merge_sort(0, len(arr) - 1)


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