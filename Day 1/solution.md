# Day 1: Secret Entrance - Solution

## Problem Summary
We need to count how many times a dial points to 0 during a sequence of rotations. The dial has numbers 0-99 and starts at position 50.

- Part 1: Count times dial ends at 0 after each rotation
- Part 2: Count all times dial passes through 0 during any rotation

## Part 1 Solution

Part 1 is simpler - we only need to count when the dial ends at position 0 after completing a rotation.

### Part 1 Algorithm
```python
pos = 50
count_zero = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        direction = line[0]
        distance = int(line[1:])
        
        # Update position based on rotation
        if direction == "L":
            pos = (pos - distance) % 100
        else:  # direction == "R"
            pos = (pos + distance) % 100
        
        # Check if we ended at 0
        if pos == 0:
            count_zero += 1

print(count_zero)
```

### Part 1 Explanation
1. Start at position 50
2. For each rotation, update the position using modular arithmetic
3. After each rotation, check if the final position is 0
4. Count each time we end at 0

This gives us the answer for Part 1 (which was 1078 according to the problem).

## Part 2 Solution

The code implements the Part 2 solution (counting all passes through 0).

### Key Insights

1. **Circular Dial**: The dial wraps around (99 → 0, 0 → 99)
2. **Counting Passes**: We need to count how many times the dial crosses 0 during each rotation
3. **Mathematical Approach**: Instead of simulating each click, we calculate crossings mathematically

### Algorithm Steps

1. **Initialize**: Start at position 50, zero counter at 0

2. **For each rotation**:
   - Parse direction (L/R) and distance
   - Calculate how many times we'll cross 0 during this rotation
   - Update the dial position

3. **Crossing Calculation**:
   - **Right rotation (R)**: Calculate distance to first 0 crossing from current position
   - **Left rotation (L)**: Calculate distance to first 0 crossing going backwards
   - If the rotation distance is long enough to reach the first crossing, count it
   - Count additional full circles (every 100 clicks = one more crossing)

### Code Breakdown

```python
# Calculate distance to first zero crossing
if direction == "R":
    first_k = (100 - pos) % 100  # Distance to 0 going right
else:
    first_k = pos % 100          # Distance to 0 going left

# Handle edge case where we're already at 0
if first_k == 0:
    first_k = 100

# Count crossings: first crossing + full circles
if first_k <= distance:
    count_zero += 1 + (distance - first_k) // 100
```

### Example Walkthrough

For rotation `L68` from position 50:
- `first_k = 50` (distance to 0 going left)
- `distance = 68 >= 50`, so we cross 0
- `count_zero += 1 + (68-50)//100 = 1 + 0 = 1`
- New position: `(50 - 68) % 100 = 82`

### Position Update

```python
if direction == "L":
    pos = (pos - distance) % 100  # Move left (counterclockwise)
else:
    pos = (pos + distance) % 100  # Move right (clockwise)
```

The modulo operation handles the circular wrapping automatically.

## Complexity
- **Time**: O(n) where n is the number of rotations
- **Space**: O(1) constant space

This solution efficiently counts all zero crossings without simulating individual clicks.