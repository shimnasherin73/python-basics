


#creating empty set
k=set()
print(type(k)) 

bc={2,3,4,2}
ab=set((9,0,9,5))
print(ab)
print(bc)
print(2 in bc)# assesing elemnt
print(5 in bc)

#adding 
bc.add(9)
print(bc)
bc.update((0,5,7))# adding multiple elemnt
print(bc)

#remove
bc.remove(2)

print(bc)
#bc.remove(11)
print(bc)

bc.discard(11)
print(bc)
#pop
a=bc.pop()
print(a)
print(bc)

#union
set1={1,2,3}
set2={3,4,5}
r=set1.union(set2)
print(r)
 
#update
set1={1,2,3}
set2={3,5,6}
set2.update(set1)
print(set2)

#intersection (&)
set1={1,2,3}#will give common items
set2={2,3,4}
r=set1 & set2
print(r)
r=set1.intersection({4,5,9})
print(r)

#difference 
set1={1,2,3}
set2={2,3,4}
r=set2-set1
print(r)

#symmetric diffence
set1={1,2,3}
set2={2,3,4}
r=set1^set2
print(r)
