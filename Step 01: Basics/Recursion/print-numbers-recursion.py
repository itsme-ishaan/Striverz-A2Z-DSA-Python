def printNumbers(n):
    if n == 0:   # Base condition
        return
    printNumbers(n - 1)   # Recursive call
    print(n)              # Work

n = int(input("Enter value of n: "))
printNumbers(n)


# It will print numbers in Increasing Order 
