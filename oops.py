#class and object:
class Dog:
    def __init__(self,name,breed):
      self.name=name
      self.breed=breed
    def bark(self):
       print(f"{self.name}says woof")
    def breath(self):
       print(f"{self.name}breaths")
dog1=Dog("buddy","labrador")
dog2=Dog("max","golden retriever")
print(dog1.name)
print(dog2.breed)
dog1.bark()
dog2.bark() 
dog2.breath()

#inheritance:
class Animals:
   def __init__(self,name):
     self.name=name 
   def speak(self):
      print(f"{self.name}makes a sound")
animal=Animals("cat")

class Dog(Animals):#(child class have same funciton as parent class which is animals) 
    def __init__(self,tail,name):
       self.tail=tail
       self.name=name
    def speak(self):
       print(f"{self.name} says woof!")
    
dog=Dog("buddy","yes")
dog.speak()
print(dog.tail)
print(animal.name)