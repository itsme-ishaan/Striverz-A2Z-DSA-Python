arr = [1, 2, 2, 3, 4, 4, 5]

seen = set()
result = []

for num in arr:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)

#Time Complexity : O(n)
#Space Complexity : O(n)
