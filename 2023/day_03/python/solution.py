set = set()
with open('./input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char.isdigit() or char == ".":
                continue

            for x in [row - 1, row, row + 1]:
                for y in [col - 1, col, col + 1]:
                    if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[x]) or not lines[x][y].isdigit():
                        continue
                    while y > 0 and lines[x][y - 1].isdigit():
                        y -= 1
                    set.add((x, y))

nums = []

for x, y in set:
    a = ""
    while y < len(lines[x]) and lines[x][y].isdigit():
        a += lines[x][y]
        y += 1
    nums.append(int(a))

print(sum(nums))
