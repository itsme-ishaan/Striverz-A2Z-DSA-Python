arr = [10, 50, 40]

largest = arr[0]
second = float('-inf')

for i in range(1, len(arr)):
    
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    
    elif arr[i] > second and arr[i] != largest:
        second = arr[i]

print("Second largest:", second)
