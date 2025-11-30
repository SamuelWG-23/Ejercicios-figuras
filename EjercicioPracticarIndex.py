# This is how indexes work to make forms: (i = row)(j = column)(n = height)
# First row: i == 0
# First column: j == 0
# Last row: i == n-1
# Last columns j == n-1
# Cross in the middle: i = j = n//2
# Diagonal from left to right: i == j
# Diagonal from right to left: i+j == n-1



# A square
#height = 5
#for i in range(height):    
#   for j in range (height):
#      print("* ", end="")
# print()



# Just first and last column
#height = 5
#for i in range(height):
#    for j in range(height):
#        if j == 0 or j == height-1:
#            print("*", end="")
#        else:
#            print("'",end="")
#    print()



#Stright cross
#n = 5
#for i in range (n):
#    for j in range (n):
#        if i == n//2 or j == n//2:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()



#Diagonal cross
#height = 5
#for i in range(height):
#    for j in range(height):
#        if i == j or i + j == height-1:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()



#Hollow square
#height = 5
#for i in range(height):
#    for j in range (height):
#        if i == 0 or j == 0 or i == height-1 or j == height-1:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()



#square triangle bottom-left
#height = 5
#for i in range(height):
#    for j in range (i+1):
#        print("*", end=" ")
#    print()
# *
# * *
# * * *
# * * * *


#square triangle upper-left
#height = 5
#for i in range(height):
#    for j in range (height-i):
#        print("*", end=" ")
#    print()
#
#OR
#height = 5
#for i in range(height):
#    for j in range (i,height):
#        print("*", end=" ")
#    print()
# * * * * *
# * * * *
# * * *
# * *
# *
#



# square triangle bottom right
#height = 5
#for i in range (height):
#    for j in range (i,height):
#        print(" ", end=" ")
#    for j in range (i+1):
#        print("*", end=" ")
#    print()



# square triangle upper right
# height = 5
# for i in range(height):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,height):
#         print("*", end=" ")
#     print()



# Hill (empty upper left, star bottom right, star bottom left)
# height = 5
# for i in range (height):
#     for j in range (i,height):
#         print(" ", end=" ")
#     for j in range (i):
#         print("*", end=" ")
#     for j in range (i+1):
#         print("*", end=" ")
#     print()



# Reverse hill
# height = 5
# for i in range (height):
#     for j in range (i+1):
#         print(" ", end=" ")
#     for j in range (i, height-1):
#         print("*", end=" ")
#     for j in range (i, height):
#         print("*", end=" ")
#     print()



# Diamond pattern
#height = 5
#for i in range (height-1):
#    for j in range (i, height):
#        print(" ", end=" ")
#    for j in range (i):
#        print("*", end=" ")
#    for j in range (i+1):
#        print("*", end=" ")
#    print()    
#for i in range (height):
#    for j in range (i+1):
#        print(" ", end=" ")
#    for j in range(i, height):
#        print("*", end=" ")
#    for j in range(i,height-1):
#        print("*", end=" ")
#    print()

# Hollow bottom-left triangle (3 lines: j == 0, i == j, i == n-1)
#height = 5
#for i in range (height):
#    for j in range (height):
#        if j == 0 or i == j or i == height-1:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()



# Hollow upper-left triangle
#height = 5
#for i in range (height):
#    for j in range (height):
#        if j == 0 or (i+j) == (height-1) or i == 0:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()
#
#for i in range (height):
#    for j in range (i, height):
#        if j == i or j == height-1 or i == 0:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()



# Hollow hill pattern
#height = 5
#for i in range (height):
#    for j in range(i,height):
#        print(" ", end=" ")
#    for j in range(i):
#        if i == height-1 or j == 0:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    for j in range(i+1):
#        if i == height-1 or i == j:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()



# hill hollow (again)
#height = 5
#for i in range(height):
#    for j in range(i,height):
#        print(" ", end=" ")
#    for j in range(i):
#        if j == 0 or i == height-1:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    for j in range(i+1):
#        if i == j or i == height-1:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()


height = 6
for i in range(height):
    for j in range(i,height):
        print(" ", end="")
    for j in range(i+1):
        if i == j or j == 0 or i == height-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()





