"""
a=20
b=5
print(a+b)

c=4
d=9
print(c+d)

#
def add(a,b):
    return a+b
result=add(3,4)
print(result)

re=add(7,10)
print(re)

# sum
def sum(a,b,c):
    print(a+b+c)
sum(5,7,9)

def greet(av):
    print("hello"+av)
greet("shimna")

def even(db):
   print(db%2==0)
even(5)

def even(db):
    if db%2==0:
        print("is even")
    else:
        print("is odd")
even(11)
"""

def add(a,b,c):
    print(a+b+c)
add(2,3)

def print_details(**kwargs):
    for key,value in kwarg,items():
        print(f"{key}:{value}")
        
        
    