s=[2,4,"python",2.4,True]
print(s[-1]) #accesing list options
print(s[1:5:3])

a="shimna sherin"
print(a[1:7:2]) #accesing string
#error a[5]="x" #cannot replace in string 
print(a)

s[3]=2
print(s) #replacing one item in list
s[0:3]=[6,9,0]#change multiple item in list
print(s)

#adding items to a list:
b=["apple","banana"]
b.append(6) #insert new item withou index
print(b)
b.insert(0,"mango") #using index numbr
print(b)
b.extend([2])#to combine 2 lists
print(b)
b.extend("cherry")
print(b) 

k=[3,9,"apple"]
o=[6,8,7]
k.extend(o)
print(k)

#removing items from a list:
b=["apple","mango",5]
b.remove("apple")
print(b)
popped_item=b.pop(1) #removing using position 
print(b)
print(popped_item) #to return the removed item
del b[0] #delete using index
print(b)

list=[4,9,"python",7.9]
list.clear() #to clear entire list
print(list)

#list methods:
list=[4,9,4,8,0,0] 
print(list.count(4)) #to count an item
print(list.index(0)) #
list.sort() #to aarange in ascending order
print(list) 

fruits=["apple","banana","cherry","mango"]
g=fruits.replace("banana","orange")
print(g) #to replace 