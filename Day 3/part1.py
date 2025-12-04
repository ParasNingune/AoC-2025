def max_joltage(bank):
    best = -1
    digits = bank.strip()

    # Find best pair in order (i < j)
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            val = int(digits[i] + digits[j])
            if val > best:
                best = val

    return best


def solve(filename):
    total = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                total += max_joltage(line)
    return total


if __name__ == "__main__":
    print(solve("input.txt"))
