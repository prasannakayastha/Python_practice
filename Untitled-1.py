# create the list with the string object, word is variable name.
'''word=["Aayan","Aarin","Prasanna"]
for i in word[:]:# iterate over the copy of the  list safely modify the original list during the loop
    if len(i)>5:#check if the lenght of the string is greater than 5
        word.append(i)# add the string object at the end of the list
        word.insert(1,i)#add the string object at the index 1.
print(word)#print the modified list'''



x=["a","b",3,5]

y=["e","f",7,9]

z=x+y

for x in z[:]:
    if type(x)==int:
        str_list=str(x)
        z.remove(x)
        
        z.append(str_list)
        
print(z[0])     
  

