import turtle

def draw_myName() :

	window = turtle.Screen()
	window.bgcolor("white")

	# Draw J
	ini = turtle.Turtle()

	ini.shape("turtle")
	ini.color("blue")
	ini.speed(2)
	ini.forward(60)
	ini.left(90)
	ini.forward(100)
	ini.left(90)
	ini.forward(50)
	ini.backward(50)
	ini.right(180)
	ini.forward(50)

	#Draw P
	sec = turtle.Turtle()

	sec.shape("arrow")
	sec.color("blue")
	sec.speed(2)

	# no drawing when moving.
	sec.penup()
	sec.setx(150)
	sec.sety(0)
	sec.left(90)

	# write again!
	sec.pendown()
	sec.forward(100)
	sec.right(90)
	sec.forward(70)
	sec.right(90)
	sec.forward(45)
	sec.right(90)
	sec.forward(70)
	
	window.exitonclick()


draw_myName()


