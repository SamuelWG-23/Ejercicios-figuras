totalHeight = 7
height = totalHeight//2
print("*"*totalHeight)
for i in range(height):
    for j in range(height):
        if j == 0:
            print("*", end=" ")
    for j in range(height):
        if j == i:
            print("*", end=" ")
        else:
            print(" ", end="")
    for j in range (height):
        if j == height-1:
            print("*", end=" ")
    print()
for i in range(height-1):
    for j in range(height):
        if j == 0:
            print("*", end=" ")
    for j in range(height):
        if i + j == height - 2:
            print("*", end=" ")
        else:
            print(" ", end="")
    for j in range (height):
            if j == height-1:
                print("*", end=" ")
    print()
print("*"*totalHeight)

