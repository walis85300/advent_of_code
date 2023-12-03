const path = import.meta.dir + "/input.txt";
const file = Bun.file(path);
const text = await file.text();
const colors: Record<string, number> = {
  red: 12,
  green: 13,
  blue: 14,
};

const r = text
  .trim()
  .split("\n")
  .reduce((acc, line) => {
    const regex = /Game (\d+):(.*)/g;
    const match = regex.exec(line);
    if (!match) {
      return acc;
    }

    const [, game, players] = match;
    const playersTrim = players.trim();
    const re = /(\d+) (red|green|blue)/g;
    let m;
    while ((m = re.exec(playersTrim)) !== null) {
      const [, points, color] = m;
      if (colors[color] < Number(points)) {
        return acc;
      }
    }

    return acc + Number(game);
  }, 0);

console.log(r);
