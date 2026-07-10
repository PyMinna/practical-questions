print("Using for loop")

arr = [1,2,3,4,5,6,7,8]
for a in arr:
    print(a ** 2)
    
print("Using while loop")

arr = [1,2,3,4,5,6,7,8]
i = 0
while i < len(arr):
    print(arr[i] ** 2)
    i += 1

print("----------------")

arr = [1,2,3,4,5,6,7,8]
i = len(arr)-1
while i >= 0:
    print(arr[i] ** 2)
    i -= 1

print()

arr = [1,2,3,4,5,6,7,8]
s = [
    arr[0] ** 2,
    arr[1] ** 2,
    arr[2] ** 2,
    arr[3] ** 2,
    arr[4] ** 2,
    arr[5] ** 2,
    arr[6] ** 2,
    arr[7] ** 2,
]
print(s)