#!/bin/python3

import math
import os
import random
import re
import sys

# Set recursion depth limit for larger matrix grids
sys.setrecursionlimit(2000)

def countLuck(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    
    # Convert matrix to mutable 2D list
    g = [list(row) for row in matrix]
    
    # Locate starting position 'M'
    start_r, start_c = 0, 0
    for r in range(m):
        for c in range(n):
            if g[r][c] == 'M':
                start_r, start_c = r, c
                break

    def get_moves(r, c):
        moves = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and g[nr][nc] in ('.', '*'):
                moves.append((nr, nc))
        return moves

    def dfs(r, c, wave_count):
        if g[r][c] == '*':
            return wave_count
        
        # Mark cell as visited
        g[r][c] = 'X'
        moves = get_moves(r, c)
        
        # Increment wand count if there are multiple decision paths
        if len(moves) > 1:
            wave_count += 1
            
        for nr, nc in moves:
            result = dfs(nr, nc, wave_count)
            if result is not None:
                return result
        return None

    actual_waves = dfs(start_r, start_c, 0)
    return "Impressed" if actual_waves == k else "Oops!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna