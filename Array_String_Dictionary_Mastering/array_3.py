#count how many elements after the n value
arr = [10,15,20,25,30,35,40]
n = 20
count = 0

for i in range(len(arr)):
    if arr[i] > n:
        count += 1
print("Count= ",count)