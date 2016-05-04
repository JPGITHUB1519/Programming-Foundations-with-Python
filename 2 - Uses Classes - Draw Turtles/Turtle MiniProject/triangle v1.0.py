import turtle

def triangle() :

	windows = turtle.Screen()
	windows.bgcolor("white")


	tr = turtle.Turtle()
	tr.color("blue")
	""" normal triangle
	tr.forward(200)
	tr.left(120)
	tr.forward(200)
	tr.left(120)
	tr.forward(200)
	"""
	tr.forward(200)
	tr.left(120)
	tr.forward(200)
	tr.left(120)
	tr.forward(200)
	tr.penup()
	tr.goto(0,0)
	tr.left(120)
	tr.forward(100)
	tr.left(120)
	tr.pendown()
	tr.forward(100)
	tr.right(120)
	tr.forward(100)
	tr.right(120)
	tr.forward(100)

	windows.exitonclick()




triangle()