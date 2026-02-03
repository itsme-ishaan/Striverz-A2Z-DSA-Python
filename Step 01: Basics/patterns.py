// Star Pattern 

n = int(input("Enter the Number of Rows: "))
m = int(input("Enter the Number of Columns: "))

for i in range(n):
    for j in range(m):
        print("*", end=" ")
    print()
