import re

cv = 0
numberedDigits = "one two three four five six seven eight nine".split()


def convertToNumber(n):
    if n in numberedDigits:
        return str(numberedDigits.index(n) + 1)
    else:
        return n


with open("./input.txt") as f:
    lines = f.readlines()
    for line in lines:
        digits = list(map(convertToNumber, re.findall(
            r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)))

        cv = cv + int(digits[0] + digits[-1])

print(
    f"Congratulations! You've successfully recovered the calibration values. The sum of all values is: {cv} stars! 🌟✨")
