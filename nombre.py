from turtle import * 

bgcolor('lightgreen')
shape('turtle')

pensize(15)




left(180)
forward(100)
left(90)
forward(60)
left(90)
forward(80)
left(180)
forward(80)
left(90)
forward(60)
left(90)
forward(100)


up()
forward(50)
left(90)
forward(120)
right(90)
down()



color("red")
right(90)
forward(120)
left(90)
circle(60, 180) 
left(90)

up()
forward(50)
left(90)
forward(120)
right(90)
forward(60)
left(90)
down()

pencolor('yellow')
left(90)
forward(100)
backward(100)
left(270)
forward(100)
left(90)
forward(100)
backward(100)
left(270)


up()
forward(50)
left(90)

right(90)

down()

color("blue")
left(70)
forward(122)
right(140)
forward(122)
left(180)
forward(55)
left(70)
forward(50)
left(180)
forward(50)
right(70)
forward(55)
left(70)


up()
forward(50)
left(90)
forward(100)
right(90)
down()


color("orange")
forward(100)
right(90)
forward(60)
right(90)
forward(100)
right(90)
forward(60)
right(180)
forward(120)
right(180)
forward(60)
right(120)
forward(120)
left(40)


up()
forward(50)
left(90)
forward(100)
right(90)
down()

color("red")
right(90)
forward(120)
left(90)
circle(60, 180) 
left(90)



import turtle


t=turtle.Turtle()
t.speed(0)



colors=['red', 'purple', 'turquoise', 'green', 'yellow', 'orange', 'pink','light blue',]

t.pensize(9)

t.penup()
t.goto(165,120)
t.pendown()
t.pensize(4)
for i in range(300):
  t.color(colors[i%8])
  t.forward(150)
  t.left(150)
  t.speed(100)
