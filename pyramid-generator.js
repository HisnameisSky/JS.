function pyramid(pattern, rows, inverted) {
  const lines = [];

  for (let i = 0; i < rows; i++) {
    const rowNum = inverted ? rows - i : i + 1;

    const spaceCount = rows - rowNum;
    const patternCount = 2 * rowNum - 1;

    const line = " ".repeat(spaceCount) + pattern.repeat(patternCount);
    lines.push(line);
  }

  return "\n" + lines.join("\n") + "\n";
}

//

"".repeat();

console.log("o".repeat(3));
console.log(" ".repeat(4));
console.log("ABC".repeat(2));
console.log("x".repeat(0));
console.log("a".repeat(2.8));