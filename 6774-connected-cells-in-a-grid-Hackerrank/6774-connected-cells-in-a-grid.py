#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    # 8 possible directions (horizontal, vertical, and diagonal)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    def dfs(r, c):
        stack = [(r, c)]
        matrix[r][c] = 0  # Mark as visited in-place
        region_size = 1
        
        while stack:
            curr_r, curr_c = stack.pop()
            
            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == 1:
                    matrix[nr][nc] = 0  # Mark visited before pushing to prevent duplicates
                    region_size += 1
                    stack.append((nr, nc))
                    
        return region_size

    max_region = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                max_region = max(max_region, dfs(i, j))
                
    return max_region


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna