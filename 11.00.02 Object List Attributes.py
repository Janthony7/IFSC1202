from math import pi

# Step 1 - Define the class object "Ball"
class Ball ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):

# Step 3 - Define the object attributes
		self.BallType = balltype
		self.Diameter = diameter
		self.Pressure = pressure

# Step 4 - Define Actions (Methods) associated with the object
	def Circumference(self):
		circumference =  pi * self.Diameter
		return circumference

# Step 4 - Here is another action
	def ChangePressure(self, pressurechange):
		self.Pressure += pressurechange
		return self.Pressure

# Step 5 - Create instance of ball using the data file and append to a list
def print_balllist(balllist):
	print("{:>14s}{:>14s}{:>14s}{:>14s}".format("Type", "Diameter", "Pressure", "Circumference"))
	for i in range(len(balllist)):
		print ("{:>14s}{:14.2f}{:14.2f}{:14.2f}".format(balllist[i].BallType, balllist[i].Diameter, balllist[i].Pressure, balllist[i].Circumference()))

# Finds the ball in balllist and returns the index of the row where the ball was found
def find_ball(balllist, balltofind):
	for i in range(len(balllist)):
		if balllist[i].BallType == balltofind:
			return i
	return -1		

balllist = []

ballfile = open("11.00.01 Balls.txt")

x = ballfile.readline()

while x != "":
	print(x) # display what was read
	y = x.split(",")
	print(y) # display the result of the split
	myball = Ball()
	myball.BallType = y[0].strip()
	myball.Diameter = float(y[1].strip())
	myball.Pressure = float(y[2].strip())
	balllist.append(myball)
	x = ballfile.readline()

ballfile.close()

print_balllist(balllist)
# Pump up the Basketball
balllist[find_ball(balllist,"Basketball")].ChangePressure(1)

#deflate the vollyball
balllist[find_ball(balllist,"Volleyball")].ChangePressure(-1)

# change the diameter of the soccerball
balllist[find_ball(balllist,"Soccerball")].Diameter = 8.01

print_balllist(balllist)