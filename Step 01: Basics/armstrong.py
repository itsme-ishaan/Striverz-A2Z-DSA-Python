num = int(input("Enter Your Number Here: "))
sum = 0
while num > 0:
  
  last_digit = num%10
  sum = sum + (last_digit * last_digit * last_digit)
  num = num/10
  
if(sum==num):
  return True
else : 
  return False
  




  
  
