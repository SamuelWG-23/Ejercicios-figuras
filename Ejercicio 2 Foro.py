totalHeight = 9 #Divisible in three
height = totalHeight//3
for i in range(height):
    for j in range (height):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range (height):
        if j == height//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(height):
        if i + j == height - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("* "*totalHeight)
for i in range(height):
    for j in range(height):
        if i + j == height - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(height):
        if j == height//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(height):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
    
    
    