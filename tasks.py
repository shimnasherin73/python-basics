#using while loop:
"""x=0
while x<5:
    print(x)
    x+=1
    
x=60
if x>100:
    print(f"{x} is greater than 100")
elif x<50:
    print(f"{x} is lessthan 50")
else:
    print("x is between 50 and 100")
    
x=6
if x>0:
    print(f"{x} is a positive number")
else:
    print(f"{x} is negative number")


x=16
if x%2==0:
    if x%4==0:
        print(f"{x} is a even number")
    else:
        print(f"{x}is not divisible by 4")
else:
    print(f"{x} is a odd number")

    if x%3==0:
        print(f"{x}is  divisible by 3")

m=46
a=80
if m>40 and a>75:
    print("pass")
else:
    print("fail")


x=15
r="adult" if x>=18 else "minor"
print(r)

sum=0
for i in range(1,101):
   sum=sum+i
print(sum)


for i in range(1,4):
    for j in range(i):
        print("*",end=" ")
    print()
    

for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 
    
for i in range(3,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
 

for i in range(6,0,-2):
    for j in range(2,i+1,2):
        print(j,end=" ")
    print()
        
#creating set and assesing using for loop: 
ab={1,2,3,4,5}  
for set in ab:
   print(set)

    
#functions to reverse s string:
name="shimna"
for i in range (len(name)-1,-1,-1):
    print(name[i],end=" ")


#finding cube of a number using lambda():
cube=lambda x:x**3
print(cube(3))
"""
#
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

a = []

for i in range(5):
    a.append(fibonacci(i))

print(a)







        


    








    
