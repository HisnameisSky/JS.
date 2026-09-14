function findSignal(grid) {
  const R = grid.length;
  const C = grid[0].length;
  const towers = [];

  for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
      if (grid[r][c] > 0) {
        towers.push({ r, c, v: grid[r][c] });
      }
    }
  }

  const towerCandidates = [];
  const directions = [
    [1, 0], [-1, 0], [0, 1], [0, -1],
    [1, 1], [1, -1], [-1, 1], [-1, -1]
  ];

  for (const { r: tr, c: tc, v } of towers) {
    const candidates = new Set();

    for (const [dr, dc] of directions) {
      const nr = tr + dr * v;
      const nc = tc + dc * v;

      if (0 <= nr && nr < R && 0 <= nc && nc < C) {
        candidates.add(`${nr},${nc}`);
      }
    }
    towerCandidates.push(candidates);
  }

  let solutionSet = towerCandidates[0];
  for (let i = 1; i < towerCandidates.length; i++) {
    const currentCandidates = towerCandidates[i];
    
    solutionSet = solutionSet.intersection(currentCandidates);
  }

  const [resultString] = Array.from(solutionSet);
  return resultString.split(',').map(Number);
}