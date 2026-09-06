#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    MOD = 10**9 + 7
    
    # c1[a]: occurrences of character a
    c1 = [0] * 26
    
    # c2[a][b]: occurrences of tuple (a, b)
    c2 = [[0] * 26 for _ in range(26)]
    
    # c3[a]: occurrences of tuple (a, b, b)
    c3 = [0] * 26
    
    ans = 0
    
    for ch in s:
        x = ord(ch) - 97  # 0 to 25 for 'a' through 'z'
        
        # 1. ch acts as the 4th character: completes (x, b, b, x)
        ans = (ans + c3[x]) % MOD
        
        # 2. ch acts as the 3rd character: forms (a, x, x) from (a, x)
        # 3. ch acts as the 2nd character: forms (a, x) from (a)
        for a in range(26):
            c3[a] = (c3[a] + c2[a][x]) % MOD
            c2[a][x] = (c2[a][x] + c1[a]) % MOD
            
        # 4. ch acts as the 1st character
        c1[x] = (c1[x] + 1) % MOD

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna