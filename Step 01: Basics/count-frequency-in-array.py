def countFrequency(arr):
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    return freq


arr = list(map(int, input("Enter numbers separated by space: ").split()))
result = countFrequency(arr)

for key, value in result.items():
    print(key, "->", value)
