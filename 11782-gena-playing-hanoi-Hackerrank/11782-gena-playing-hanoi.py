#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'hanoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY posts as parameter.
#

def hanoi(posts):
    n = len(posts)
    
    # Encode initial configuration into a bitmask (2 bits per disk)
    start_state = 0
    for i in range(n):
        start_state |= ((posts[i] - 1) << (2 * i))
    
    # Target state is all disks on rod 1 (encoded as 0)
    if start_state == 0:
        return 0
    
    visited = bytearray(1 << (2 * n))
    visited[start_state] = 1
    
    current_level = [start_state]
    moves = 0
    
    while current_level:
        moves += 1
        next_level = []
        
        for state in current_level:
            # Determine the top (smallest) disk on each of the 4 rods
            top = [n] * 4
            for i in range(n):
                rod = (state >> (2 * i)) & 3
                if top[rod] == n:
                    top[rod] = i
            
            # Explore valid moves between rods
            for from_rod in range(4):
                d = top[from_rod]
                if d == n:
                    continue
                for to_rod in range(4):
                    if from_rod != to_rod and top[to_rod] > d:
                        next_state = (state & ~(3 << (2 * d))) | (to_rod << (2 * d))
                        if next_state == 0:
                            return moves
                        if not visited[next_state]:
                            visited[next_state] = 1
                            next_level.append(next_state)
                            
        current_level = next_level
        
    return moves

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    loc = list(map(int, input().rstrip().split()))

    res = hanoi(loc)

    fptr.write(str(res) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna