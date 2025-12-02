import math

invalid_ids = set()

with open("input.txt", "r") as f:
    line = f.read().strip()

range_strings = line.split(",")
ranges = []
for r in range_strings:
    if not r:
        continue
    
    a, b = map(int, r.split("-"))
    ranges.append((a, b))

max_overall_b = max(b for a, b in ranges)
max_len = len(str(max_overall_b))

for L in range(1, max_len // 2 + 1):
    
    k_start = 10**(L - 1)
    k_end = 10**L 
    
    max_R = max_len // L

    for R in range(2, max_R + 1):
        
        multiplier = sum(10**(L * i) for i in range(R))
        
        smallest_N = k_start * multiplier

        if smallest_N > max_overall_b:
            continue

        for k in range(k_start, k_end):
            N = k * multiplier
            
            if N > max_overall_b:
                break 

            for a, b in ranges:
                if a <= N <= b:
                    invalid_ids.add(N)
                    break 

print(sum(invalid_ids))


