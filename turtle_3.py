import turtle             
wn = turtle.Screen()      
i = turtle.Turtle() 

times = 8
distance = 50
angle = 45
i.up()
i.shape("square")
i.speed(10)

for _ in range(4):
    i.forward(distance)
    i.right(90)
    for _ in range(times):
        i.stamp()
        i.forward(distance)
        i.left(angle)

wn.exitonclick()