import time

#eDo serial number: 2404096

#joint limits
#j1	-178.90 to 178.90
#j2 -98.92 to 98.92
#j3 -98.92 to 98.92
#j4 -178.91 to 178.91
#j5 -103.41 to 103.41
#j6 -178.91 to 178.91
#j7 0 to 80.53mm

from pyedo import edo
#myedo = edo("10.42.0.49") # lan
myedo = edo("192.168.12.1") # lan

time.sleep(2)

myedo.listen_JointState()
myedo.listen_CartesianPosition()

time.sleep(2)

myedo.move_joint(ovr=100, j1=-178.90, j2=-11.65, j3=98.92, j4=0, j5=0, j6=45, j7=15)

input("Press ENTER to start PATH #1...")

myedo.move_joint(ovr=25, j1=178.90, j2=-11.65, j3=98.92, j4=0, j5=0, j6=45, j7=15)

while True:

	state = myedo.get_JointState()

	print("v ", state['cartesianPosition'][0], state['cartesianPosition'][1], state['cartesianPosition'][2])

	time.sleep(0.5)	

time.sleep(120)

