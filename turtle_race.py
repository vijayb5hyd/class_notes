import turtle          			   # Import every object(*) from module 'turtle'
from turtle import *
speed(100)
penup()
# The following code is for writing 0 to 13 numbers on the sheet
# By default, the turtle arrow starts at the middle of the page. goto(x,y) will take it to (x,y).

goto(-120,120) 
for step in range(14):
   write(step, align='center')
   forward(20)      # the turtle arrow is moving 20 pixels with every step. But, it's not drawing since the pen is up.
# The following code is to draw 0 to 13 lines
goto(-120,120)
for step in range(14):
   right(90)
   forward(10)
   pendown()     # Starts drawing
   forward(200)  # 200 pixels line
   penup()       # stops
   left(180)
   forward(210)
   right(90)
   forward(20)
# Import 'randint' object/member from the module 'random'

from random import randint
# Define turtle1 and start the race
tigress=Turtle()          # uppercase T in the function 'Turtle()', lowercase t will lead to NameError.
tigress.color('orange')
tigress.shape('turtle')
tigress.penup()
tigress.goto(-140,70)
tigress.pendown()
for turn in range(100):
   tigress.forward(randint(1,5))   
# randint(x,y) generates random integers between x and y. Forward the turtle with the random number generated.
# Define turtle2 and start the race
viper=Turtle()
viper.color('green')
viper.shape('turtle')
viper.penup()
viper.goto(-140,35)
viper.pendown()
for turn in range(100):
   viper.forward(randint(1,5))
# Define turtle3 and start the race
monkey=Turtle()
monkey.color('yellow')
monkey.shape('turtle')
monkey.penup()
monkey.goto(-140,0)
monkey.pendown()
for turn in range(100):
   monkey.forward(randint(1,5))
# Define turtle4 and start the race
mantis=Turtle()
mantis.color('blue')
mantis.shape('turtle')
mantis.penup()
mantis.goto(-140,-35)
mantis.pendown()
for turn in range(100):
   mantis.forward(randint(1,5))
# Define turtle5 and start the race
crane=Turtle()
crane.color('gray')
crane.shape('turtle')
crane.penup()
crane.goto(-140,-70)
crane.pendown()
for turn in range(100):
   crane.forward(randint(1,5))

turtle.exitonclick()
