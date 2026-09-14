n = input()
count = 0

while len(n) > 1:
    total = 0

    for digit in n:
        total += int(digit)

    n = str(total)
    count += 1

print(count)
