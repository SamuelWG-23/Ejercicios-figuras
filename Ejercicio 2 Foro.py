n = 9
for i in range (0,3):
    for j in range (0,3):
        print(" "*j+"*"+" "*(2-j),end='')
        if j ==2:
            print("")