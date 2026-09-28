#!/bin/python3

import os
import sys

#
# Complete the acessoryCollection function below.
#
def acessoryCollection(L, A, N, D):

    # Impossible cases
    if D > A or N < D or N > L:
        return "SAD"

    # If only one distinct type is required,
    # buy all accessories of the most expensive type.
    if D == 1:
        return str(L * A)

    maximum = 0

    # Maximum possible repetition count
    a2Max = (N - 1) // (D - 1)

    for a2 in range(a2Max, 0, -1):

        a1 = N + (a2 - 1) - a2 * (D - 1)

        n = (L - a1) // a2
        a3 = (L - a1) % a2

        # Not enough accessory types available
        if n > A - 1 or (n == A - 1 and a3 > 0):
            break

        # Calculate maximum spending for this arrangement
        current = (
            A * a1
            + (A - 1 + A - n) * n // 2 * a2
            + a3 * (A - n - 1)
        )

        if current <= maximum:
            break

        maximum = current

    if maximum:
        return str(maximum)

    return "SAD"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        LAND = input().split()

        L = int(LAND[0])

        A = int(LAND[1])

        N = int(LAND[2])

        D = int(LAND[3])

        result = acessoryCollection(L, A, N, D)

        fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna