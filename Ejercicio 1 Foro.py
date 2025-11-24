n = 5
altura = 2*n-1
for i in range(1,n):
    if i == 1:
        print(" " * (n) + " *" + " " * (n-1))
    print(" "*(n-i) + "*"+ "  "*i+ " *" + " "*(n-i))

for j in range (n-1,0,-1):
    if j == 1:
        print(" " * (n) + " *" + " " * (n-1))
    else:
        print(" "*(n-j+1) + "*" + "  "*(j-1) + " *" + " "*(n-j))
