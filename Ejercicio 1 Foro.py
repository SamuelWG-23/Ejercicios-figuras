altura = 5
espacio = 0
for i in range (0,altura):
    espacio=altura-i
    if i == 0:
        print(" "*altura+" *")
    else:
        print(" "*espacio+"*"+" "*i+"*")
for j in range (0,altura):
    espacio=altura-j
    if espacio == 0:
        print(" "*j+"*")
    else:
        print(" "*j+"*"+" "*espacio+"*")
print(" "*(altura+1)+"*")