def max_joltage(bank: str) -> int:
    digits = bank.strip()
    TARGET_LENGTH = 12
    N = len(digits)

    if N < TARGET_LENGTH:
        return 0

    K = N - TARGET_LENGTH

    stack = []

    for digit in digits:
        while stack and K > 0 and stack[-1] < digit:
            stack.pop()
            K -= 1
        
        stack.append(digit)

    if K > 0:
        stack = stack[:-K]

    return int("".join(stack))



total = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            max_val = max_joltage(line)
            total += max_val
    
print(total)