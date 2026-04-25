"#condtion statmnt:
x=1
if x>5: #needed to be true 
    print("x is greater than 5")
else: #if the (if) is false 
    print("x is not grater than 5")    
    
x=7
if x%2==0:
    print(f"{x} is even number") #f=to get number in output
else:
    print(f"{x} is odd number")
     
x=45
if x%3==0:
    print(f"{x} is multiple of 3")
else:
    print(f"{x} is not a multple of 3")
    
x=7#if there is 3 conditions 
if x>10:
    print("x is greater than 10")
elif x<5:
    print("x is less than 5")
else:
    print("x is between 5&10") 
    
#nested if:
x=4
y=11
if x>5:
    if y<10:
     print("x is greater than 5 and y is lessthan 10")
    else:
        print("y is greater than 10")
else:
    print("x is lessthan 5")


x=8
if x<10:#if true will go to next if 
    if x%2==0:
        print(f"{x} is lessthan 10 also the multiple of 2")
    else:
        print(f"{x} is not a multiple of 2")
else:
    print("x is greater than 10")
    
    
    """
#condition statmnt using logic oprtor(and):
"""
x=8
if x<10 and x%2==0:
    print(f"{x} is lessthan 10 also the multiple of 2")
else:
    print(f"{x} is not the multiple of 2") 

#conditional expressions:
x=5
if x>10:
    print("greater than 10")
else:
    print("x is 10 or less")
    
#
x=5
r="greater than 10" if x>10 else"10 or less"
print(r)





