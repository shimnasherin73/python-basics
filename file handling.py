#reading :
''''
file=open ("sample.txt","r")
content=file.readlines()
print(content)

#writing:
file=open("sample.txt","w+")#write amd read w+
file.write("hello world!")
print(file.read())


#
lines=["hello\n","welcome to python handling\n"]
file.writelines(lines)

#appending:adding to the last
file=open("sample.txt","a+")
file.write("append text\n")
print(file.read())

#with statement:will automatically close after coming out of nested block
with open("sample.txt","r") as file:
    contnet=file.read()
    print(content)
'''
#seek and tell( seek will get ouput after index 5) 
file=open("sample.txt","r")
file.seek(5)
print(file.read()) 
position=file.tell()
print(position) 

#opening path of file outside vscode:
#file=open("C:/Users/pc/Desktop/sinan/python_batch1/sherin.txt","r")
#print(file.read())

