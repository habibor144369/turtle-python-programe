# tryangle art using for loop with turtle....
import  turtle

turtle.color('blue')
turtle.shape('turtle')
turtle.speed(1)

for i in range(3):
    turtle.forward(200)
    turtle.left(120)

turtle.hideturtle()
turtle.exitonclick()
print('program terminated!')