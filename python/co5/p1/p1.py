lines = []
with open("p1.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

print(lines)