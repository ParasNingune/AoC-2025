# Day 2: Gift Shop - Solution

## Problem Summary
Find invalid product IDs in given ranges where:
- **Part 1**: Invalid IDs are sequences repeated exactly twice (e.g., 55, 6464, 123123)
- **Part 2**: Invalid IDs are sequences repeated at least twice (e.g., 123123, 111111, 12121212)

## Part 1 Solution

### Algorithm Overview
The Part 1 solution uses an efficient generation approach rather than checking every number in the ranges.

### Key Functions

```python
def is_double(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]
```

This helper function checks if a number is made of a sequence repeated exactly twice.

### Main Algorithm Steps

1. **Parse Input**: Read ranges from file and split by commas
2. **For each range**:
   - Determine min and max lengths of numbers in the range
   - Generate all possible "double" numbers of appropriate lengths
   - Check if each generated number falls within the range
   - Sum valid numbers

### Generation Strategy
Instead of checking every number, we generate candidates:
- For length 4: generate numbers like 1010, 1111, 1212, etc.
- For length 6: generate numbers like 101101, 111111, 121121, etc.
- Only generate numbers that could possibly be in our ranges

```python
for length in range(min_len, max_len + 1):
    if length % 2 != 0:
        continue  # Skip odd lengths
    
    half = length // 2
    start = 10 ** (half - 1)  # Smallest number with 'half' digits
    end = 10 ** half          # Largest number with 'half' digits
    
    for first_half in range(start, end):
        n = int(str(first_half) + str(first_half))  # Duplicate the pattern
        if a <= n <= b:
            total += n
```

## Part 2 Solution

### Algorithm Overview
Part 2 extends the problem to find sequences repeated 2 or more times. This requires a more sophisticated generation approach.

### Key Concepts

1. **Pattern Parameters**:
   - `L`: Length of the repeating pattern
   - `R`: Number of repetitions (≥ 2)
   - `k`: The actual pattern (as a number)

2. **Number Generation**:
   - For pattern "12" repeated 3 times: L=2, R=3, k=12, result=121212

### Algorithm Steps

1. **Initialize**: Create set to store unique invalid IDs
2. **Parse ranges** and find maximum number to limit search space
3. **Generate candidates systematically**:
   - For each pattern length L (1 to max_len//2)
   - For each repetition count R (2 to max possible)
   - For each pattern k (from 10^(L-1) to 10^L - 1)
   - Generate the number k repeated R times

### Mathematical Formula

For a pattern `k` of length `L` repeated `R` times:
```python
multiplier = sum(10**(L * i) for i in range(R))
N = k * multiplier
```

Example: Pattern "12" (k=12, L=2) repeated 3 times (R=3):
- multiplier = 10^0 + 10^2 + 10^4 = 1 + 100 + 10000 = 10101
- N = 12 × 10101 = 121212
