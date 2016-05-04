
import turtle

def draw_square() :

    #generar pantalla

    window = turtle.Screen()
    window.bgcolor("red")

    #generando objeto
    brad = turtle.Turtle()

    # move forwad
    brad.forward(100)

    # turn to right
    brad.right(90)
    brad.forward(100)
    
    brad.right(90) 
    brad.forward(100)

    brad.right(90)
    
    brad.forward(100)   


    window.exitonclick()


draw_square()
