#!/bin/python3

import math
import os
import random
import re
import sys

def cutTheTree(data, edges):
    n = len(data)
    total_sum = sum(data)
    
    # Build 0-indexed adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
        
    # BFS to establish parent-child hierarchy and topological order
    parent = [-1] * n
    order = []
    queue = [0]
    visited = [False] * n
    visited[0] = True
    
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
                
    # Calculate subtree sums bottom-up in reverse BFS order
    subtree_sum = list(data)
    min_diff = float('inf')
    
    for u in reversed(order):
        p = parent[u]
        if p != -1:
            subtree_sum[p] += subtree_sum[u]
            # Absolute difference if the edge between u and p is cut
            diff = abs(total_sum - 2 * subtree_sum[u])
            if diff < min_diff:
                min_diff = diff
                
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna