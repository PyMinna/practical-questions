#find index of an array element
arr = [1,3,5,7,8,6,4,2]
print("index[4]= ",arr.index(4))

#check if an element exist in an array

arr = [10,20,30,40,50,60]
print("30 exist? true/false: ",30 in arr)

#find first occurance of an element

text = 'helloo minnaah'
print("find fist position of 'o': ",text.find('o'))


list = [1,2,3,2,5,4,3,1,1,3,6,5]
print("find first position of (list 3):",list.index(3))

#find last occurace of an element

text = 'helloo minnaah'
print("find last position of 'n': ",text.rfind('n'))
print("find count of 'a' in the string: ",text.count('a'))


list = [1,2,3,2,5,4,3,1,1,3,6,5]
element = 3
last = -3
for i in range(len(list)):
    if list[i]==element:
        last = i
print("find last position of(list 3): ",last)

#count how many times an element appears in an array
arr =[1,2,3,2,4,3,1,1,3,6,5]
print("count of 1: ",arr.count(1))
