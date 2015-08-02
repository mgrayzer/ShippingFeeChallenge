__author__ = 'mmwin8'

for steps in range(1,101):
    if steps % 3 == 0 and steps % 5 != 0:
        print("hello")
    elif steps % 5 == 0 and steps % 3 != 0:
            print("there")
    elif steps % 3 == 0 and steps % 5 == 0:
                print("Hello There")
    else:
        print(steps)


