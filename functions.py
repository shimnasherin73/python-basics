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
"""
        
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
    print(f'name:{args[0]} ,age:{args[1]},city:{args[2]}')
sum("shimna",24,"pmna")

