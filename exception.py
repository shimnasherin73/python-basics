""" 
try:
 x=10/0
except ZeroDivisionError:
 print("you can't divide by zero!")


try:
 x=10/0
except Exception as e:
 print(e)

abc=int(input("enter a value"))
if abc==0:
    try:
     x=10/abc
    except Exception as e:
     print(e)
else:
    x=10/abc
    print(x) 
"""
#raising exception:
abc=int(input("enter a value "))
if abc==0:
    try:
     x=10/abc
    except Exception as e:
     print(e)

elif abc<0:
    try:
      raise ValueError("negative numbers are not allowed")    
    except  ValueError as e:
        print(e)
else:
    x=10/abc
    print(x) 



#custom exception:
class NegativeNumberError(Exception):
    pass
def check_number(num):
    if num<0:
        raise NegativeNumberError("negative numbers are not allowed!")
try:
    check_number(-10)
except NegativeNumberError as e:
   print(e)

   
