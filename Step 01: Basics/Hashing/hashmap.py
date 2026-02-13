def frequencyCount(arr):
    hashmap = {}   # empty hash map
    
    for num in arr:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    
    return hashmap


arr = list(map(int, input("Enter numbers: ").split()))
result = frequencyCount(arr)

for key, value in result.items():
    print(key, "->", value)
