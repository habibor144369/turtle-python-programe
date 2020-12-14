# Square art using for loop with turtle....
import  turtle

turtle.color('blue')
turtle.shape('turtle')
turtle.speed(1)

for i in range(4):
    turtle.forward(150)
    turtle.left(90)

turtle.hideturtle()
turtle.exitonclick()
print('program terminated!')
