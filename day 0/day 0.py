from turtle import*

#square

width(8)
speed(30)
color("pink")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


#door

forward(70)
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

#roof

penup()
goto(200, 200)
pendown()
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


exitonclick()