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
"""

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
    for k in range(2):
        print("*",end=" ")
    print()    

    
    
    
    
    

    
    

    
