n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(1, n - i + 1):
        print(j, end=" ")
    print()
