import turtle

turtle.speed(1)
turtle.shape('turtle')
turtle.color('blue')

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.hideturtle()
turtle.exitonclick()
