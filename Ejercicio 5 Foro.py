height = 7
for i in range (height):
    for j in range(height):
        if i == j and j != 0 and i != 0 and i != height-1:
            print("*", end=" ")
        elif i+j == height-1 and i != height-1 and j != height-1:
            print("*", end=" ")
        elif i == height//2 :
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()