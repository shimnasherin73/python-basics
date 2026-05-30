#findall:
import re
pattern=r"\d+"#(d+ only if there are more than one digit)
text="there are 35 apples and 567 ornges"
match=re.findall(pattern,text)
print(match)

#match (will give  only if the given word is in the begining of text)
text="HELLO WORLD"
match=re.match(r"HELLO",text)
print(match)

#search:(will get if the word is anywhere in the sentnce)
text="HELLO WORLD"
match=re.search(r"WORLD",text)
print(match)

#replacing(replace )
text="HELLO 123,welcome 456!"
new_text=re.sub(r"\d+","number",text)
print(new_text)

#splitting string:(will split according to the condition given after r)
text="apple,orange;banana,grapes"
fruits=re.split(r"[;,]",text)
print(fruits)

#grouping
text="john:34,alice:45,bob:45"
matches=re.findall(r"(\w+):(\d+)",text)
print(matches)



