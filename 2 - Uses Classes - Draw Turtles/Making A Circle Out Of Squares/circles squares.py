
import turtle

def draw_square(some_turtle) :
	for i in range(0,4) :
		some_turtle.forward(100)
		some_turtle.right(90)


def draw_art() :

	window = turtle.Screen()
	window.bgcolor("red")

	jp = turtle.Turtle()

	jp.shape("turtle")
	jp.color("yellow")
	jp.speed(6)

	for i in range(0,36) :
		draw_square(jp)
		jp.right(10)

	"""
	jp2 = turtle.Turtle()

	jp2.shape("circle")
	jp2.color("yellow")
	jp2.speed(2)

	jp2.circle(100)
	"""
	window.exitonclick()


draw_art()
