# Codeforces 1624B - Make AP

t = int(input())  # number of test cases

for _ in range(t):
    a, b, c = map(int, input().split())
    ok = False

    # Case 1: multiply a so that the new a = 2*b - c
    new_a = 2 * b - c
    if new_a > 0 and new_a % a == 0:
        ok = True

    # Case 2: multiply b so that the new b = (a + c) / 2
    if (a + c) % 2 == 0:          # must be a whole number
        new_b = (a + c) // 2
        if new_b % b == 0:
            ok = True

    # Case 3: multiply c so that the new c = 2*b - a
    new_c = 2 * b - a
    if new_c > 0 and new_c % c == 0:
        ok = True

    print("YES" if ok else "NO")
