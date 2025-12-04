def part2(filename="input.txt"):
    try:
        with open(filename, 'r') as f:
            grid = [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return 0

    if not grid:
        return 0

    R = len(grid)
    C = len(grid[0])
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    
    total_removed = 0
    removed_in_iteration = -1

    while removed_in_iteration != 0:
        removed_in_iteration = 0
        rolls_to_remove = []
        
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

        if rolls_to_remove:
            removed_in_iteration = len(rolls_to_remove)
            total_removed += removed_in_iteration
            
            for r, c in rolls_to_remove:
                grid[r][c] = '.' 
                
        else:
            removed_in_iteration = 0
            
    return total_removed

print(part2())