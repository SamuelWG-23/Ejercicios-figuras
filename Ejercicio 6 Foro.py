totalHeight = 7
height = totalHeight//2+1
for i in range (height):
    for j in range(i+1):
        if j == 0 or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(i,height-1):
        print(" ", end="")
    for j in range(i, height-1):
        print(" ", end="")
    for j in range (i+1):
        if j == 0 or i == j:
            print("*", end="")
        elif j == 0 and i == height-1:
            print(" ", end="")
        else:
            print(" ", end="")
    print()