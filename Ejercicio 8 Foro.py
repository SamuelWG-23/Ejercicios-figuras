altura = int(input("Introduce una altura para hacer un rombo sólido de esa altura: "))
for i in range (1,altura+1,2):
    print(" " * (altura-i) + " *" * i)
for i in range (altura-2,0,-2):
    print(" " * (altura-i) + " *" * i)