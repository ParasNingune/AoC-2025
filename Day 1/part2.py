pos = 50
count_zero = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        if direction == "R":
            first_k = (100 - pos) % 100
        else:
            first_k = pos % 100

        if first_k == 0:
            first_k = 100

        if first_k <= distance:
            count_zero += 1 + (distance - first_k) // 100

        if direction == "L":
            pos = (pos - distance) % 100
        else:
            pos = (pos + distance) % 100

print(count_zero)
