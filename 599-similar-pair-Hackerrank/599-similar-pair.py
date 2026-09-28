#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'similarPair' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY edges
#

def similarPair(n, k, edges):
    # Build the tree
    children = [[] for _ in range(n + 1)]
    has_parent = [False] * (n + 1)

    for u, v in edges:
        children[u].append(v)
        has_parent[v] = True

    # Find root
    root = next(i for i in range(1, n + 1) if not has_parent[i])

    # Fenwick Tree
    bit = [0] * (n + 2)

    def update(i, delta):
        while i <= n:
            bit[i] += delta
            i += i & -i

    def query(i):
        total = 0
        while i > 0:
            total += bit[i]
            i -= i & -i
        return total

    answer = 0

    # Iterative DFS avoids Python recursion-depth problems.
    # state 0 = entering node, state 1 = leaving node
    stack = [(root, 0)]

    while stack:
        node, state = stack.pop()

        if state == 0:
            # Fenwick tree currently contains exactly the ancestors
            # of this node.
            left = max(1, node - k)
            right = min(n, node + k)

            answer += query(right) - query(left - 1)

            # Add current node while exploring its descendants
            update(node, 1)

            # Remove it after all descendants have been processed
            stack.append((node, 1))

            for child in reversed(children[node]):
                stack.append((child, 0))

        else:
            update(node, -1)

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = similarPair(n, k, edges)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna