import re

points = 0

with open("./input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

    for line in lines:
        (leftNums, rightNums) = line.split("|")

        wNumbers = re.findall(r"\d+", leftNums)[1::]
        aNumbers = re.findall(r"\d+", rightNums)

        common = set(wNumbers).intersection(aNumbers)

        if len(common) > 0:
            points += 2 ** (len(common) - 1)

print(points)
