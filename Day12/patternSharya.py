import turtle

chintu = turtle.Turtle()
chintu.shape("arrow")

chintu.up()
chintu.forward(90)
chintu.down()

for  counter in range(0, 18) :
  chintu.right(145)
  chintu.forward(60)
  chintu.right(45)
  chintu.forward(60)


input("enter to exit")
