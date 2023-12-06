with open("./input.txt") as f:
    lines = f.read().strip().split("\n")

total = 0

for line in lines:
    game, cubes = line.split(": ")
    r, g, b = 0, 0, 0

    for cube in cubes.split("; "):
        for color in cube.split(", "):
            num, c = color.split(" ")
            num = int(num)

            if c == "red":
                r = max(r, num)
            if c == "blue":
                b = max(b, num)
            if c == "green":
                g = max(g, num)

    total += r * g * b

print(total)
