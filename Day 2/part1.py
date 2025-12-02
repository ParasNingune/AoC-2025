def is_double(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

total = 0

with open("input.txt", "r") as f:
    line = f.read().strip()

ranges = line.split(",")

for r in ranges:
    if not r:
        continue
    a, b = map(int, r.split("-"))

    min_len = len(str(a))
    max_len = len(str(b))

    for length in range(min_len, max_len + 1):
        if length % 2 != 0:
            continue 
            
        half = length // 2
        start = 10 ** (half - 1)
        end = 10 ** half

        for first_half in range(start, end):
            n = int(str(first_half) + str(first_half))
            if a <= n <= b:
                total += n

print(total)