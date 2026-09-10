#!/bin/python3

import os
import sys
from collections import deque

def bikeRacers(bikers, bikes, k):
    n = len(bikers)
    m = len(bikes)
    
    # Precompute pairwise squared distances
    dist_sq = [[0] * m for _ in range(n)]
    unique_dists = set()
    
    for i in range(n):
        x1, y1 = bikers[i]
        for j in range(m):
            d2 = (x1 - bikes[j][0]) ** 2 + (y1 - bikes[j][1]) ** 2
            dist_sq[i][j] = d2
            unique_dists.add(d2)
            
    sorted_dists = sorted(unique_dists)
    
    # Hopcroft-Karp matching check for a given distance threshold D
    def can_match(max_d2):
        # pair_u stores matched bike for biker u (1-indexed, 0 = unmatched)
        # pair_v stores matched biker for bike v (1-indexed, 0 = unmatched)
        pair_u = [0] * (n + 1)
        pair_v = [0] * (m + 1)
        dist = [0] * (n + 1)
        
        # Build adjacency list for current threshold
        adj = [[] for _ in range(n + 1)]
        for u in range(n):
            for v in range(m):
                if dist_sq[u][v] <= max_d2:
                    adj[u + 1].append(v + 1)

        def bfs():
            q = deque()
            for u in range(1, n + 1):
                if pair_u[u] == 0:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = float('inf')
            dist[0] = float('inf')
            
            while q:
                u = q.popleft()
                if dist[u] < dist[0]:
                    for v in adj[u]:
                        if dist[pair_v[v]] == float('inf'):
                            dist[pair_v[v]] = dist[u] + 1
                            q.append(pair_v[v])
            return dist[0] != float('inf')

        def dfs(u):
            if u != 0:
                for v in adj[u]:
                    if dist[pair_v[v]] == dist[u] + 1:
                        if dfs(pair_v[v]):
                            pair_v[v] = u
                            pair_u[u] = v
                            return True
                dist[u] = float('inf')
                return False
            return True

        matching = 0
        while bfs():
            for u in range(1, n + 1):
                if pair_u[u] == 0 and dfs(u):
                    matching += 1
            if matching >= k:
                return True
                
        return matching >= k

    # Binary search over sorted unique distances
    low = 0
    high = len(sorted_dists) - 1
    ans = sorted_dists[-1]
    
    while low <= high:
        mid = (low + high) // 2
        if can_match(sorted_dists[mid]):
            ans = sorted_dists[mid]
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    bikers = []
    for _ in range(n):
        bikers.append(list(map(int, input().rstrip().split())))

    bikes = []
    for _ in range(m):
        bikes.append(list(map(int, input().rstrip().split())))

    result = bikeRacers(bikers, bikes, k)

    fptr.write(str(result) + '\n')
    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna