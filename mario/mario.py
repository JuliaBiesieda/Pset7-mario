from cs50 import get_int

n = get_int("Height: ")
while n < 1 or n > 8:
    n = get_int("Height: ")

for i in range(n):
    for j in range(n - 1):
        print(" ", end="")
    for e in range(i + 1):
        print("#", end="")
    print()
    n -= 1

