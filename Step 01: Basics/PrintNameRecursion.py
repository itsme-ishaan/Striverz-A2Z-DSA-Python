def RecurrName(name, n):
    if n == 0:
        return
    print(name)
    RecurrName(name, n - 1)

name = input("Enter your name: ")
n = int(input("Enter how many times: "))

RecurrName(name, n)
