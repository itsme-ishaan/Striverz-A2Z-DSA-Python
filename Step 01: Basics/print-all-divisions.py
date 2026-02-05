//Approach 1 : O(n)
num = int(input("Enter Your Number: "))

for i in range(1,num+1):
  if (num%i==0):
    print(i, end=" ")



//Approach 2 : O(Log n)
import math
num = int(input("Enter Your Number: "))

for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        print(i, end=" ")
        
        if i != num // i:   # avoid duplicate for perfect square
            print(num // i, end=" ")
