def part1(filename="input.txt"):
    try:
        with open(filename, 'r') as f:
            grid = [line.strip() for line in f if line.strip()]
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
    
print(part1())