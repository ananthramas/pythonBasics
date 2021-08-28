import turtle 
import time
import random

chintu = turtle.Turtle()
chintu.shape("turtle")

chintu.forward(200)
chintu.left(90)
chintu.forward(50)


chintu.right(90)

chintu.up()
chintu.goto(0,10)
chintu.down()
  

colours = ["red", "yellow", "blue", "purple", "green", "gold", "aqua"]

for x in range(20) :
  # % means reminder of 7
  chintu.color(colours[x%7])
  stampId = chintu.stamp()
  chintu.up()
  chintu.forward(20)
  chintu.down()
  chintu.clearstamp(stampId)
  time.sleep(2)

chintu.shape("classic")


#time.sleep(5)


turtle.exitonclick()