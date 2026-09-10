#!/bin/python3

from collections import deque
import os
import sys

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Moves ordered strictly by problem priority: UL, UR, R, LR, LL, L
    moves = [
        ('UL', -2, -1),
        ('UR', -2, 1),
        ('R',   0,  2),
        ('LR',  2,  1),
        ('LL',  2, -1),
        ('L',   0, -2)
    ]
    
    queue = deque([(i_start, j_start)])
    parent = {(i_start, j_start): None}
    
    found = False
    while queue:
        r, c = queue.popleft()
        if (r, c) == (i_end, j_end):
            found = True
            break
            
        for move_name, dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in parent:
                parent[(nr, nc)] = (r, c, move_name)
                queue.append((nr, nc))
                
    if not found:
        print("Impossible")
        return
        
    # Backtrack path from destination to start
    path = []
    curr = (i_end, j_end)
    while parent[curr] is not None:
        pr, pc, move = parent[curr]
        path.append(move)
        curr = (pr, pc)
        
    path.reverse()
    print(len(path))
    print(" ".join(path))

if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])
    j_start = int(first_multiple_input[1])
    i_end = int(first_multiple_input[2])
    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna