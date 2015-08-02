__author__ = 'marlon.gray'

area = 0
height = 10
width = 20
# calculate the area of a triangle
area = width * height/2

# printed formatted float value with 2 decimal places
print("The area of the rectangle would be %.2f" % area)

# printing the formatted decimal number with right justified to take up 6 spaces with leading zeros
print("My favourite number is %06d" %14)

# do the same thing with the .format syntax to include numbers in our output
print("the area of the triangle would be {0:.2f}".format(area))
print("MY favorite number is {0:d}".format(14))

#this is an example with multiple numbers
#I have used the \ to indicate line continues
print("Here are three numbers! The first is {0:d}" + \
      "The second is {1:4d} and the third number is {2:d}".format(10,14,78))