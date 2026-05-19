#destructor:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"{self.name}has been created")
    def __del__(self):
        print(f"{self.name}has been destroyed")
p1=Person("john",30)
del p1 

