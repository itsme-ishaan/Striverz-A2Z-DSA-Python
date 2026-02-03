n = int(input("Enter number of rows: "))

for i in range(n):

    # spaces
    print(" " * (n - i - 1), end="")

    # stars
    print("* " * (2 * i + 1))

