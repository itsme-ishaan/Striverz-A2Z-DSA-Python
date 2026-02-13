def sumN(n):
    if n == 0:
        return 0
    return n + sumN(n - 1)

n = int(input("Enter n: "))
print("Sum =", sumN(n))
