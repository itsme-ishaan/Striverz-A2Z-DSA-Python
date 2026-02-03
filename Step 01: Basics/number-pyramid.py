n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    print("  " * (n - i), end="")   # spaces

    for j in range(1, i + 1):       # increasing
        print(j, end=" ")

    for j in range(i - 1, 0, -1):   # decreasing
        print(j, end=" ")

    print()
