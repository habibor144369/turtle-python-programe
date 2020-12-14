# star art using for loop with turtle....by user input---
import  turtle
num1 = int(input("Enter your first value type 200 : "))
num2 = int(input("Enter your second value type 144 : "))
turtle.color('blue')
turtle.shape('turtle')
turtle.speed(2)

for i in range(5):
    turtle.forward(num1)
    turtle.right(num2)

turtle.hideturtle()
turtle.exitonclick()
print('program terminated!')
