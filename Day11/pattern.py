import turtle 

chintu = turtle.Turtle()
chintu.shape("turtle")

#for radiusValue  in range(1,10) :
#  chintu.circle(radiusValue*10)

for radiusValue  in range(1,10):
  chintu.circle(radiusValue*10)
  chintu.right(90*radiusValue)
  chintu.forward(radiusValue*10)
  chintu.circle((radiusValue+1)*10)
input()
