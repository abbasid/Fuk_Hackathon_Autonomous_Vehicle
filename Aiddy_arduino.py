import pyfirmata
import PID
import time

targetAngle = 0.0
initalAngle = 0.0
currentAngle = 0.0

PORT = ''
arduino = pyfirmata.Arduino(PORT)


motor_left_CW = arduino.get_pin('d:5:p')
motor_left_CCW = arduino.get_pin('d:6:p')

motor_right_CCW = arduino.get_pin('d:9:p')
motor_right_CW = arduino.get_pin('d:10:p')

lastTime = time.time()

while True:
	if lastTime >= 1000:
		stop()
	

def stop():
	motor_right_CW.write(0.0)
	motor_right_CCW.write(0.0)
	motor_left_CW.write(0.0)
	motor_left_CCW.write(0.0)

def move(error):

	# error = (targetAngle - currentAngle)/(targetAngle - initalAngle)
	
	lastTime = time.time()

	if error == 181:
		stop()
	# turn left
	elif error < -0.1:
		currentSpeed = parabola(abs(error))
		motor_left_CW.write(currentSpeed)
		motor_right_CW.write(currentSpeed)

	# turn right
	elif error > 0.1:
		currentSpeed = parabola(abs(error))
		motor_right_CCW.write(currentSpeed)
		motor_left_CCW.write(currentSpeed)
	# move forward
	else:
		motor_right_CW.write(maxSpeed)
		motor_left_CCW.write(maxSpeed)		

def parabola(x):
	if x > 0 and x < 1:
		return -4*x*x + 4*x
	else:
		return 0
