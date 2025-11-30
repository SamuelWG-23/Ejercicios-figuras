totalHeight = 6
height = 6
for i in range(height):
    for j in range(i,height):
        print(" ", end="")
    for j in range(i+1):
        if j == 0 and i == height-1:
            print("*", end="*")
        elif j == 0 or i == j or i == height//2:
            print("*", end=" ")
        elif i == height-1:
            print("*", end="*")
        else:
            print(" ", end=" ")
    print()



