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

def add(a,b,c):
    print(a+b+c)
add(2,3)

        
#positional arguments/regular argmnts:
 def sum(a,b,c):
      print(f"name{a},age{b},mark{c}")
 sum("shimna",24,30)

#key word arguments:
def details(**kwargs):
    print(f' name : {kwargs["name"]} age:{kwargs["age"]} city:{kwargs["city"]} ')
details(name="shimna",age=24,city="pmna")    

#arbitrary argumnts:
def sum(*args):
    print(f'name:{args[0]} ,age:{args[1]},city:{args[2]}')+++
sum("shimna",24,"pmna")

#lambda function:
add=lambda a,b:a+b
print(add(3,5))

#map()
numbers=[1,2,3,4,5]
squared=map(lambda x:x**2,numbers)
print(list(squared))

#filter():
numbers=[1,2,3,4,5,6]
even_numbers=filter(lambda x:x%2==0,numbers)
print(list(even_numbers))

#reduce():
from functools import reduce
numbers=[1,2,3,4,]
sum_result=reduce(lambda x,y:x+y,numbers)
print(sum_result)

#hihger order():
def increment(n):
    return lambda x:x+n
bc=increment(5)
print(bc(10))

#
x=10
def outer_function():
 x=5
 def inner_function():
    x=2
    print(x) 
 inner_function()
outer_function()
print(x)

#recursion: (finding the factorial using recursion)
def factorial(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
"""
#fibonacci using recursion :    
def fibonacci(n):
    if n==1 or n==0:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
print(fibonacci(4))
    
