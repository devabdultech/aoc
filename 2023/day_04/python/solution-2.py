import re

ss = {}

with open("./input.txt") as f:
    lines = f.read().strip().split("\n")

    for i, line in enumerate(lines):
        if i not in ss:
            ss[i] = 1

        (leftNums, rightNums) = line.split("|")
        wNumbers = re.findall(r"\d+", leftNums)[1::]
        aNumbers = re.findall(r"\d+", rightNums)

        common = set(wNumbers).intersection(aNumbers)

        if len(common) == 0:
            continue

        for n in range(i + 1, i + len(common) + 1):
            ss[n] = ss.get(n, 1) + ss[i]

print(sum(ss.values()))
