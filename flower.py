import turtle
turtle.color('green')
turtle.speed(1)

counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)

    turtle.right(10)
    counter += 1

turtle.hideturtle()
turtle.exitonclick()
print('program terminated!')
