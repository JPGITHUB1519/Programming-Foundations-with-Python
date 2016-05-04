import turtle


	
def triangle(tr,tam) :

	tr.color("blue")
	""" normal triangle
	tr.forward(tam)
	tr.left(120)
	tr.forward(tam)
	tr.left(120)
	tr.forward(tam)
	"""
	tr.forward(tam)
	tr.left(120)
	tr.forward(tam)
	tr.left(120)
	tr.forward(tam)
	tr.penup()
	#tr.goto(0,0)
	tr.left(120)
	tr.forward(tam/2)
	tr.left(120)
	tr.pendown()
	tr.forward(tam/2)
	tr.right(120)
	tr.forward(tam/2)
	tr.right(120)
	tr.forward(tam/2)

def draw() :
	windows = turtle.Screen()
	windows.bgcolor("white")

	tr = turtle.Turtle()
	tr.speed(7)
	triangle(tr,300)
	tr.penup()
	tr.goto(50,87)
	tr.pendown()
	triangle(tr,80)

	windows.exitonclick()


draw()



