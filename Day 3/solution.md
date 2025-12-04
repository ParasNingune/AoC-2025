# Day 3: Lobby - Solution

## Problem Summary
Select batteries from banks to maximize joltage output:
- **Part 1**: Select exactly 2 batteries from each bank to form the largest 2-digit number
- **Part 2**: Select exactly 12 batteries from each bank to form the largest 12-digit number

The key constraint is that batteries must maintain their original order (no rearranging).

## Part 1 Solution

### Algorithm Overview
Part 1 uses a brute force approach to find the optimal pair of batteries.

### Strategy
Since we only need 2 batteries, we can check all possible pairs and find the maximum.

```python
def max_joltage(bank):
    best = -1
    digits = bank.strip()

    # Find best pair in order (i < j)
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            val = int(digits[i] + digits[j])
            if val > best:
                best = val

    return best
```

### Algorithm Steps

1. **Initialize**: Set best value to -1
2. **Nested loops**: Check all pairs (i, j) where i < j
3. **Form number**: Concatenate digits[i] + digits[j]
4. **Track maximum**: Keep the largest value found
5. **Return result**: The maximum 2-digit joltage

### Example Walkthrough
For bank `987654321111111`:
- Try all pairs: (9,8), (9,7), (9,6), ..., (1,1)
- Best pair: (9,8) → 98
- This is the maximum possible since 9 is the largest digit and 8 is the largest following digit

### Complexity
- **Time**: O(n²) where n is the length of the bank
- **Space**: O(1) constant space

## Part 2 Solution

### Algorithm Overview
Part 2 requires selecting 12 out of n batteries to form the largest possible number. This is equivalent to removing (n-12) batteries to maximize the remaining sequence.

### Key Insight: Monotonic Stack
The problem becomes: "Remove k digits from a number to make it as large as possible" where k = n - 12.

This is a classic problem solved using a **monotonic decreasing stack**.

### Strategy
Use a greedy approach with a stack:
1. Process digits left to right
2. Remove smaller digits when a larger digit appears (if we still have removals left)
3. Maintain the largest possible prefix at each step

```python
def max_joltage(bank: str) -> int:
    digits = bank.strip()
    TARGET_LENGTH = 12
    N = len(digits)

    if N < TARGET_LENGTH:
        return 0

    K = N - TARGET_LENGTH  # Number of digits to remove

    stack = []

    for digit in digits:
        # Remove smaller digits from the end if we can
        while stack and K > 0 and stack[-1] < digit:
            stack.pop()
            K -= 1
        
        stack.append(digit)

    # If we still need to remove digits, remove from the end
    if K > 0:
        stack = stack[:-K]

    return int("".join(stack))
```

### Algorithm Steps

1. **Calculate removals**: K = total_length - 12
2. **Process each digit**:
   - While the stack has elements AND we can still remove digits AND the top of stack is smaller than current digit:
     - Remove the top element (this makes room for the larger digit)
     - Decrement removal counter
   - Add current digit to stack
3. **Final cleanup**: If we still need to remove digits, remove from the end
4. **Convert to number**: Join the remaining digits

### Example Walkthrough
For bank `234234234234278` (length 15, remove 3):

1. Process '2': stack = ['2'], K = 3
2. Process '3': '2' < '3', remove '2', add '3': stack = ['3'], K = 2  
3. Process '4': '3' < '4', remove '3', add '4': stack = ['4'], K = 1
4. Process '2': '4' > '2', just add: stack = ['4', '2'], K = 1
5. Process '3': '2' < '3', remove '2', add '3': stack = ['4', '3'], K = 0
6. Continue adding remaining digits: stack = ['4', '3', '4', '2', '3', '4', '2', '3', '4', '2', '7', '8']
7. Result: 434234234278

### Why This Works

The greedy approach works because:
- **Positional value**: Earlier positions have exponentially more impact
- **Local optimality**: If we can replace a smaller digit with a larger one in an earlier position, we should
- **Monotonic property**: Once we've made optimal choices for earlier positions, later choices don't affect them

## Key Differences Between Parts

1. **Part 1**: Small search space allows brute force (O(n²))
2. **Part 2**: Large search space requires efficient greedy algorithm (O(n))
3. **Part 1**: Simple pair selection
4. **Part 2**: Complex subsequence optimization using monotonic stack

## Algorithm Choice Rationale

- **Part 1**: Brute force is acceptable due to small result size (2 digits)
- **Part 2**: Greedy approach leverages the structure of number maximization problems
- Both solutions maintain the constraint that battery order cannot be changed