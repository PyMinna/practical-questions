#replace all occurance of a same value
print('example 1')
arr = [10,20,10,40,10,60]

old = 10
new = 100

for i in range(len(arr)):
    if arr[i] == old:
        arr[i] = new
        
print(arr)

print('example 2')
name = "Hima"

oldd = "Hima"
neww = "Minna"

for i in range(len(name)):
    if name == oldd:
        name = neww

print(name)

print("example 3")
c = ['note', 'book']
o = 'note'
n = 'text'
for i in range(len(c)):
    if c[i] == o:
        c[i] = n
print(c)