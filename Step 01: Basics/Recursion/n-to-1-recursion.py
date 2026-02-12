def printNumbers(n):
    if n == 0:
        return
    print(n)
    printNumbers(n - 1)

n = int(input("Enter value of n: "))
printNumbers(n)
