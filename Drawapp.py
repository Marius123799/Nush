# import turtle library
import turtle  
print("1 - Poligon 2- Patrat in patrat 3-spirale")
Draw = int(input("Desen "))

colorbg = input("Background color: ")
pencol = input("pen color: ")
title = input("Titlu: ")
wn = turtle.Screen()
pen = turtle.Turtle()
pen.color(pencol)
wn.bgcolor(colorbg)
wn.title(title)
if (Draw == 1):
    SIDES = int(input("Laturi "))
    LENGTH = int(input("Lungime "))
    if(LENGTH > 200):
        print("Va recomandam mai valori mai mici de 200 la Lungime")
    if(SIDES == 4):
        print("Nu putem desena un patrat cand cerinta este de poligon")
    else:
  

        polygon = turtle.Turtle()
        num_sides = SIDES
        side_length = LENGTH
        angle = 360.0 / num_sides
        for i in range(num_sides):
            polygon.forward(side_length)           
            polygon.right(angle) 
        turtle.done()
        print("DONE!")

if (Draw == 2):

   
    import turtle             


    # import turtle library
    import turtle             
    wn = turtle.Screen()

    pen = turtle.Turtle()
    pen.color(pencol)
    def sqrfunc(size):
        for i in range(4):
            pen.fd(size)
            pen.left(90)
            size = size - 5
    sqrfunc(146)
    sqrfunc(126)
    sqrfunc(106)
    sqrfunc(86)
    sqrfunc(66)
    sqrfunc(46)
    sqrfunc(26)
    print("DONE!")


if(Draw == 3 ):
    import turtle             
    colors = [ "red","purple","blue","green","orange","yellow"]
    pen = turtle.Pen()

    for x in range(360):
        pen.pencolor(colors[x % 6])
        pen.width(x/100 + 1)
        pen.forward(x)
        pen.left(59)

   
