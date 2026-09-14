def find_signal(grid):
    R = len(grid)
    C = len(grid[0])
    towers = []
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0:
                towers.append((r, c, grid[r][c]))
    
    tower_candidates = []
    for tr, tc, v in towers:
        candidates = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        
        for dr, dc in directions:
            nr, nc = tr + dr * v, tc + dc * v
            if 0 <= nr < R and 0 <= nc < C:
                candidates.add((nr, nc))
        tower_candidates.append(candidates)
        
    solution_set = tower_candidates[0]
    for current_candidates in tower_candidates[1:]:
        solution_set = solution_set.intersection(current_candidates)
        
    return list(solution_set.pop())
