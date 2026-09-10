import os
import sys

def beautifulQuadruples(a, b, c, d):
    # Step 1: Sort bounds so A <= B <= C <= D to enforce ordered quadruples
    A, B, C, D = sorted([a, b, c, d])
    
    # Step 2: Precompute total (a, b) pairs for b <= x
    cnt_ab = [min(A, b) for b in range(B + 1)]
    pref_ab = [0] * (B + 1)
    for b in range(1, B + 1):
        pref_ab[b] = pref_ab[b - 1] + cnt_ab[b]
        
    # Step 3: Compute total valid quadruples under condition a <= b <= c <= d
    total_quads = 0
    for c_val in range(1, C + 1):
        valid_b = min(B, c_val)
        total_quads += pref_ab[valid_b] * (D - c_val + 1)
        
    # Step 4: Count invalid quadruples where (a ^ b) == (c ^ d)
    cnt_xor = [0] * 4096  # Max XOR value for inputs <= 3000 is < 4096
    invalid_quads = 0
    
    for c_val in range(1, C + 1):
        # Accumulate valid (a, b) pairs as b reaches c_val
        if c_val <= B:
            limit_a = min(A, c_val)
            for a_val in range(1, limit_a + 1):
                cnt_xor[a_val ^ c_val] += 1
        
        # Lookup matching XOR results for current (c_val, d_val) pairs
        for d_val in range(c_val, D + 1):
            invalid_quads += cnt_xor[c_val ^ d_val]
            
    return total_quads - invalid_quads

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    abcd = input().split()

    a = int(abcd[0])
    b = int(abcd[1])
    c = int(abcd[2])
    d = int(abcd[3])

    result = beautifulQuadruples(a, b, c, d)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna