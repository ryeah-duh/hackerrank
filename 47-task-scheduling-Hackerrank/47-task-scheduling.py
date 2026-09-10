#!/bin/python3

import os
import sys

# Increase recursion depth for deep segment tree traversals
sys.setrecursionlimit(300000)

MAX_D = 100000

# Segment Tree arrays
tree = [0] * (4 * (MAX_D + 1))
lazy = [0] * (4 * (MAX_D + 1))

def build(node, l, r):
    if l == r:
        tree[node] = -l
        return
    mid = (l + r) // 2
    build(2 * node, l, mid)
    build(2 * node + 1, mid + 1, r)
    tree[node] = max(tree[2 * node], tree[2 * node + 1])

def push(node):
    if lazy[node] != 0:
        val = lazy[node]
        lazy[2 * node] += val
        tree[2 * node] += val
        lazy[2 * node + 1] += val
        tree[2 * node + 1] += val
        lazy[node] = 0

def update(node, l, r, ql, qr, val):
    if ql <= l and r <= qr:
        tree[node] += val
        lazy[node] += val
        return
    push(node)
    mid = (l + r) // 2
    if ql <= mid:
        update(2 * node, l, mid, ql, qr, val)
    if qr > mid:
        update(2 * node + 1, mid + 1, r, ql, qr, val)
    tree[node] = max(tree[2 * node], tree[2 * node + 1])

# Initialize the Segment Tree once
build(1, 1, MAX_D)

def taskScheduling(d, m):
    # Add duration `m` to all deadlines >= d
    update(1, 1, MAX_D, d, MAX_D, m)
    # The max lateness is at least 0
    return max(0, tree[1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        d = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        result = taskScheduling(d, m)
        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna