import turtle

#Creates the turtle window and names it and hides the turtle
screen = turtle.getscreen()
screen.title("Langton's Ant")
screen.bgcolor("white")

#Hides the original turtle and disables animation for speed
turtle.ht()
turtle.tracer(False)

#Contains all the coordinates the ant has visited
memory = []

#Creating the ant
def ant():
    ant = turtle.Turtle()
    ant.shape("square")
    ant.shapesize(0.25)
    ant.penup()
    ant.speed(0)
    

    while True:
        move = 5
        #print(memory)
        currentPosition = coord(ant)
        
        #If the ant hasn't been there before colour the pixel black
        if currentPosition not in memory:
            ant.fillcolor("black")
            ant.stamp()

            #Update turtle because animations are disabled
            turtle.update()

            #Adds current coordinate to memory and moves to next coordinate
            memory.append(currentPosition)
            ant.right(90)
            ant.forward(move)
            
        #If the ant has been there before colour the black pixel white
        elif currentPosition in memory:
           ant.fillcolor("white")
           ant.stamp()
           
           #Updates turtle
           turtle.update()

           #Removes current coordinate from memory so it can be turned black if visited again then moves
           memory.remove(currentPosition)
           ant.left(90)
           ant.forward(move)

#Turns the X and Y coordinate into a nicer number because it doesn't like 2D vectors
def coord(ant):
    return (round(ant.xcor()), round(ant.ycor()))
                   
ant()
    

