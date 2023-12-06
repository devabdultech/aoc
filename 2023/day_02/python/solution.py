with open("./input.txt") as f:
    lines = f.read().strip().split("\n")

total = 0

for line in lines:
    game, cubes = line.split(": ")
    gameId = int(game.split(" ")[1])

    possible = True
    for cube in cubes.split("; "):
        for color in cube.split(", "):
            num, c = color.split(" ")
            num = int(num)

            if c == "red" and num > 12:
                possible = False
            if c == "blue" and num > 14:
                possible = False
            if c == "green" and num > 13:
                possible = False

            if not possible:
                break

        if not possible:
            break

    if possible:
        total += gameId

print(total)
