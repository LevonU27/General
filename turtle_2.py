import turtle             
wn = turtle.Screen()      
i = turtle.Turtle() 

times = 60
distance = 10
angle = 6
i.speed(0)

for _ in range(3):
    i.right(120)
    for _ in range(times):
        i.forward(distance)
        i.left(angle)

wn.exitonclick()