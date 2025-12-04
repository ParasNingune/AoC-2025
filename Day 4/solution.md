# Day 4: Printing Department - Solution

## Problem Summary
Optimize forklift operations by identifying accessible paper rolls:
- **Part 1**: Count paper rolls with fewer than 4 adjacent paper rolls
- **Part 2**: Simulate iterative removal process until no more rolls can be accessed

Paper rolls (@) can only be accessed if they have fewer than 4 neighboring rolls in the 8 adjacent positions.

## Part 1 Solution

### Algorithm Overview
Part 1 uses a straightforward grid traversal to count accessible rolls in a single pass.

### Strategy
For each paper roll, count its neighbors and check the accessibility condition.

```python
def part1(filename="input.txt"):
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f if line.strip()]

    R = len(grid)
    C = len(grid[0])
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    
    accessible_rolls = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '@':
                neighbor_roll_count = 0
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == '@':
                            neighbor_roll_count += 1
                
                if neighbor_roll_count < 4:
                    accessible_rolls += 1
                    
    return accessible_rolls
```

### Algorithm Steps

1. **Load grid**: Read the input file into a 2D grid
2. **Define directions**: 8 adjacent positions (including diagonals)
3. **Traverse grid**: Check each cell
4. **Count neighbors**: For each '@', count adjacent '@' symbols
5. **Check accessibility**: If neighbor count < 4, increment counter
6. **Return result**: Total accessible rolls

### Neighbor Counting Logic
- Check all 8 directions: up, down, left, right, and 4 diagonals
- Boundary checking: Ensure coordinates are within grid bounds
- Only count '@' symbols as neighbors

### Example Analysis
For position with '@':
```
@@@
@X@  ← X has 8 neighbors (not accessible)
@@@

.@@
@X.  ← X has 3 neighbors (accessible)
.@.
```

### Complexity
- **Time**: O(R × C) where R and C are grid dimensions
- **Space**: O(R × C) for storing the grid

## Part 2 Solution

### Algorithm Overview
Part 2 simulates an iterative removal process where removing accessible rolls may make other rolls accessible.

### Strategy
Use a simulation approach with multiple iterations:
1. Find all currently accessible rolls
2. Remove them simultaneously 
3. Repeat until no more rolls can be removed

```python
def part2(filename="input.txt"):
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    # ... grid setup ...
    
    total_removed = 0
    removed_in_iteration = -1

    while removed_in_iteration != 0:
        removed_in_iteration = 0
        rolls_to_remove = []
        
        # Find all accessible rolls in current state
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '@':
                    neighbor_roll_count = 0
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        
                        if 0 <= nr < R and 0 <= nc < C:
                            if grid[nr][nc] == '@':
                                neighbor_roll_count += 1
                    
                    if neighbor_roll_count < 4:
                        rolls_to_remove.append((r, c))

        # Remove all accessible rolls simultaneously
        if rolls_to_remove:
            removed_in_iteration = len(rolls_to_remove)
            total_removed += removed_in_iteration
            
            for r, c in rolls_to_remove:
                grid[r][c] = '.'  # Remove the roll
                
        else:
            removed_in_iteration = 0
            
    return total_removed
```

### Algorithm Steps

1. **Initialize**: Set total_removed = 0, prepare for iterations
2. **Main loop**: Continue while rolls were removed in last iteration
3. **Find accessible**: Identify all rolls with < 4 neighbors
4. **Batch removal**: Remove all accessible rolls simultaneously
5. **Update counters**: Track removed rolls and continue
6. **Termination**: Stop when no rolls can be removed

### Key Design Decisions

#### Simultaneous Removal
All accessible rolls are identified first, then removed together. This prevents the removal of one roll from immediately affecting the accessibility of others in the same iteration.

#### Grid Modification
```python
grid = [list(line.strip()) for line in f if line.strip()]  # Mutable grid
# ...
grid[r][c] = '.'  # Replace '@' with '.'
```

The grid is stored as a list of lists (mutable) so we can modify it in place.

#### Iteration Tracking
```python
removed_in_iteration = -1  # Initialize to ensure loop starts
while removed_in_iteration != 0:
    # ...
    removed_in_iteration = len(rolls_to_remove)
```

### Example Walkthrough

Starting grid:
```
..@@.@@@@.
@@@.@.@.@@
...
```

**Iteration 1**: Find 13 accessible rolls, remove them
**Iteration 2**: Some previously inaccessible rolls now become accessible, remove 12
**Iteration 3**: Continue until no more removals possible

### Why Simulation is Necessary

The removal process is **cascading**: 
- Removing rolls reduces neighbor counts for adjacent rolls
- Previously inaccessible rolls may become accessible
- This creates a chain reaction that must be simulated step by step

### Optimization Considerations

1. **Batch processing**: Remove all accessible rolls per iteration (not one-by-one)
2. **Early termination**: Stop when no rolls found in current iteration
3. **In-place modification**: Modify grid directly rather than creating copies


## Key Differences Between Parts

1. **Part 1**: Static analysis - single pass through grid
2. **Part 2**: Dynamic simulation - multiple iterations with grid modification
3. **Part 1**: Read-only grid access
4. **Part 2**: Mutable grid with cascading updates
5. **Part 1**: O(R×C) time complexity
6. **Part 2**: O(I×R×C) time complexity where I = number of iterations

## Problem Classification
This is a **cellular automaton** problem where:
- Each cell has a state (roll or empty)
- State transitions depend on local neighborhood
- System evolves until reaching stable configuration