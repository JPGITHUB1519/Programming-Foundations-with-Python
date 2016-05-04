
import turtle

def draw_square() :

    #generar pantalla

    window = turtle.Screen()
    window.bgcolor("red")


    #generando objeto
    jp = turtle.Turtle()

    #forma
    jp.shape("triangle")

    #color
    jp.color("blue","yellow")

    # speed

    jp.speed(1)

    # move forwad
    jp.forward(100)

    # turn to right
    jp.right(90)
    jp.forward(100)
    
    jp.right(90) 
    jp.forward(100)

    jp.right(90)
    
    jp.forward(100)   

    # another instance

    jp2 = turtle.Turtle()
    jp2.shape("turtle")
    jp2.circle(50)


    window.exitonclick()


draw_square()
