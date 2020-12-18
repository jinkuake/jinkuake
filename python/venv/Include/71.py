import turtle

t = turtle.Pen()

color= ("red","green","yellow","black")
t.width(4)
t.speed(10)

for i in range(10):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(color[i%len(color)])
    t.circle(15+i*10)

t.done()