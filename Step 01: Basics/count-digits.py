num = int(input("Enter Your Number: "))

count = 0

while num != 0:
    num = num // 10   # remove last digit
    count += 1

print("Number of digits:", count)
