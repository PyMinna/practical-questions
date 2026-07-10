arr = [1,"I",2.5,"He",3]
print(arr)

print("Using For loop")

arr = [1,"I",2.5,"He",3]
for a in arr:
    print(a)

print("------------------")

print("Using While loop")

arr = [1,"I",2.5,"He",3]
i = 0
while i < len(arr):
    print(arr[i])
    i += 1

print("---------------")

arr = [1,"I",2.5,"He",3]
i = len(arr)-1
while i >= 0:
    print(arr[i])
    i -= 1