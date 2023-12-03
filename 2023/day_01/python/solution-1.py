import re

cv = 0

with open("./input.txt") as f:
    lines = f.readlines()
    for line in lines:
        digits = re.findall('\d', line)

        cv = cv + int(digits[0] + digits[-1])

print(
    f"Congratulations! You've successfully recovered the calibration values. The sum of all values is: {cv} stars! 🌟✨")
