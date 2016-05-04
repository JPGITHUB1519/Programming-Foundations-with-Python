import turtle

def draw_square(obj) :

	for i in range(0,4) :
		obj.forward(80)
		obj.left(90)
	

def draw_flower() :

	window = turtle.Screen()
	window.bgcolor = "white"

	obj = turtle.Turtle()
	obj.color("blue")
	obj.speed(6)
	obj.shape("turtle")

	for i in range(0,30) :
		obj.left(15)
		draw_square(obj)

	obj.left(180)
	obj.forward(200)







	window.exitonclick()


draw_flower()