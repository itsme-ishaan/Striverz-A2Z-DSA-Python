arr = [10, 45, 23, 67, 12]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element:", largest)

#Time Complexity : O(n)
