import  turtle

height = 7
width = 7
turtle.speed(1)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20 * 7)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)

turtle.hideturtle()
turtle.exitonclick()
