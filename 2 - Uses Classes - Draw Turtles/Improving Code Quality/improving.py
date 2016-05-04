
import turtle

def draw_square(shape,color,speed) :

    #generar pantalla

    window = turtle.Screen()
    window.bgcolor("red")


    jp = turtle.Turtle()

    jp.shape(shape)
    jp.color(color)
    jp.speed(speed)

    for i in range(0,4) :
        jp.forward(100)
        jp.right(90)

    window.exitonclick()

def draw_circle(shape,color,speed,radius) :

    window = turtle.Screen()
    window.bgcolor("red")

    jp = turtle.Turtle()

    jp.shape(shape)
    jp.color(color)
    jp.speed(speed)
    
    jp.circle(radius)

    window.exitonclick()



    

draw_circle("circle","yellow",2,100)
