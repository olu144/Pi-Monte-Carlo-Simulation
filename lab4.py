
'''
Estimates pi using Monte Carlo simulation
Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if the entire board is filled with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 will return an approx. of pi
'''
import turtle
import random
import time

#Guides turtle to draw a square
def drawSquare(myturtle, width, top_left_x, top_left_y):
        myturtle.up()
        myturtle.goto(top_left_x,top_left_y)
        myturtle.down()
        myturtle.goto(top_left_x+width,top_left_y)
        myturtle.goto(top_left_x+width,top_left_y-width)
        myturtle.goto(top_left_x,top_left_y-width)
        myturtle.goto(top_left_x,top_left_y)
        myturtle.up()
        
#Guides turtle to draw a circle    
def drawCircle(myturtle, radius):
    myturtle.up()
    myturtle.goto(0, -(radius))
    myturtle.down()
    myturtle.circle(radius, steps=360)
    myturtle.up()

#Guides turtle to draw a line segment 
def drawLine(myturtle,x_start, y_start,x_end,y_end):
    myturtle.up()
    myturtle.goto(x_start, y_start)
    myturtle.down()
    myturtle.goto(x_end, y_end)
    myturtle.up()
    
#Guides turtle to draw a dartboard using cirle, square and line.
def setUpDartboard(mywindow, myturtle):
    myturtle.color("black")
    turtle.setworldcoordinates(-2, -2, 2, 2)
    drawCircle(myturtle, 1)
    drawSquare(myturtle, 2, -1, 1)
    drawLine(myturtle, -1, 0, 1, 0)
    drawLine(myturtle,  0, -1, 0, 1)
    
#"throws" random darts onto the darboard and colorcodes dart depedning on where they land
def throwDart(myturtle):
        randx = random.random()
        randy = random.random()
        multiplierx = random.choice((-1, 1))
        multipliery = random.choice((-1, 1))
        x = randx * multiplierx
        y = randy * multipliery
        myturtle.up()
        myturtle.goto(x,y)
        myturtle.dot()
        if isInCircle(myturtle,0,0,1):
                myturtle.color("red")
                myturtle.dot()
                return True
        else:
                myturtle.color("blue")
                myturtle.dot()
                return False
        
#Determines if a dart lands in a circle
def isInCircle(myturtle, circle_center_x, circle_center_y, radius):
    return (myturtle.distance((circle_center_x, circle_center_y)) <= radius)

#Simulation of two players playing darts to test program functions
def playDarts(myturtle):
    score1=0
    score2=0
    for i in range(10):
        if (throwDart(myturtle)):
            score1=score1+1
        if (throwDart(myturtle)):
            score2=score2+1
    if(score1>score2):
        print("PLAYER 1 IS THE WINNER")
    elif(score2>score1):
        print("PLAYER 2 IS THE WINNER")
    else:
        print("DRAW")

#Monte carlo applied to pi. Random darts used to aproximate pi.
def montePi(myturtle, num_darts):
        inside=0
        for i in range(num_darts):
                hit=throwDart(myturtle)
                if(hit):
                        inside=inside+1
        return ((inside/num_darts)*4)

def main():
    # Get number of darts for simulation from user
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0)
    setUpDartboard(window, darty)

    # Loop 10 darts for testing purposes
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    
    # Keep window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)
    
    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    window.exitonclick()

main()
