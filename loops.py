__author__ = 'marlon.gray'
import turtle
# for steps in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#     for moreSteps in range(4):
#         turtle.forward(50)
#         turtle.right(90)


# nbrSides = 4
# for steps in range(nbrSides):
#     turtle.forward(100)
#     turtle.right(360/nbrSides)
#     for moreSteps in range(nbrSides):
#         turtle.forward(50)
#         turtle.right(360/nbrSides)
# turtle.done()
#
#
# for steps in [1,2,3,4,5]:
#     print(steps)

for steps in ["red","blue","green","yellow"]:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)
    turtle.done()