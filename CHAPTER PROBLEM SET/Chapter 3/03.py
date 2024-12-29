name = "harry"

print(len(name))
print(name.endswith("y"))#true
print(name.startswith("h"))#true
print(len(name))
print(name.endswith("a"))#false
print(name.startswith("r"))#false
print(name.startswith("H"))#false because case sencetive

print(name.capitalize())#is function na h ko capital banadiya

#---------------------------------------------------
name2 = "harry and jarry"
print(name2.capitalize)#isme sirf first word captial hoga 
print(name2.title())