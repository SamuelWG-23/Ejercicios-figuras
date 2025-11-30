height = int(input("Please enter a height to make a hollow diamond: "))
for i in range (height-1):
    for j in range (height-1):
        if i+j == height-1:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(height):
        if i== j:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(height):
    for j in range(height-1):
        if i == j:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range (height):
        if i+j == height-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()