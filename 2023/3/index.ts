const path = import.meta.dir + "/input.txt";
const file = Bun.file(path);
const text = await file.text();

function getNumber(
  m: string[][],
  i: number,
  j: number,
  checked: Record<string, boolean>,
): number {
  let limitLeft = j;
  let limitRight = j;

  while (limitLeft >= 0 && /\d/.test(m[i][limitLeft])) {
    checked[`${i},${limitLeft}`] = true;
    limitLeft--;
  }

  while (limitRight < m.length && /\d/.test(m[i][limitRight])) {
    checked[`${i},${limitRight}`] = true;
    limitRight++;
  }

  return Number(m[i].slice(limitLeft + 1, limitRight).join(""));
}

function checkAdjacent(m: string[][], i: number, j: number): number[] {
  let checked: Record<string, boolean> = {};

  const adjacentNumbers = [];

  const u = [-1, 0, 1];
  for (const x of u) {
    for (const y of u) {
      if (/\d/.test(m[i + x][j + y])) {
        if (!checked[`${i + x},${j + y}`]) {
          adjacentNumbers.push(getNumber(m, i + x, j + y, checked));
        }
      }
    }
  }

  return adjacentNumbers;
}

function partOne(m: string[][]): number {
  const w = m[0].length;
  const h = m.length;
  let sum = 0;

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      const c = m[i][j];
      if (c === "." || /\d/.test(c)) {
        continue;
      }
      sum += checkAdjacent(m, i, j).reduce((a, b) => a + b, 0);
    }
  }
  return sum;
}

function partTwo(m: string[][]): number {
  const w = m[0].length;
  const h = m.length;
  let sum = 0;

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      const c = m[i][j];
      if (c !== "*") {
        continue;
      }
      const numbersAround = checkAdjacent(m, i, j);
      if (numbersAround.length < 2) {
        continue;
      }
      sum += numbersAround.reduce((a, b) => a * b, 1);
    }
  }
  return sum;
}

const m = text
  .trim()
  .split("\n")
  .map((line) => Array.from(line.trim()));

console.log(partOne(m));
console.log(partTwo(m));
