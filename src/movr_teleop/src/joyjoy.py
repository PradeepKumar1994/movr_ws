#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from ackermann_msgs.msg import AckermannDrive

# ########################################
# RUN INSTRUCTIONS:
# $ roscore // launch roscore
# $ rosrun joy joy_node // start the Joy node in a seprarate window
# $ rosrun movr_teleop_joy joyjoy.py // run the script, make sure to source devel/setup.bash
#
# ########################################
# Logitech Gamepad Joy Node
# Converts joystick inputs into Ackerman messages for the vehicles
#
# Default Logitech Gamepad Mapping
# ########################################
# 	Logitech Button		|	Mapping
# ########################################
#		X					buttons[0]
#		A 					buttons[1]
#		B 					buttons[2]
#		Y 					buttons[3]
#		LB					buttons[4]
#		RB					buttons[5]
# 		LT 					buttons[6]
#		RT 					buttons[7]
#   	BACK 				buttons[8]
#  		START 				buttons[9]
# ########################################
# Left Analogue Stick	|
# 	LEFT 	- RIGHT 		axes[0]
# 	UP 		- DOWN 			axes[1]
#
# Right Analogue Stick	|
# 	LEFT 	- RIGHT 		axes[2]
# 	UP 		- DOWN 			axes[3]
# ########################################
# 	D-Pad Buttons  		| 	Mapping
# 
# 	LEFT 	- RIGHT 		axes[4]
# 	UP		- DOWN			axes[5]
# ########################################

def joy_cb(msg):
	btn_a			= msg.buttons[1]	# Accelerate
	btn_x 			= msg.buttons[0]	# Deceelerate

	# LEFT Analogue Stick
	left_joy_h 		= msg.axes[0]
	left_joy_v 		= msg.axes[1]

	steering_angle 	= transformAnalogToSteerAngle(left_joy_h, -1, 1, -45, 45)
	ackermann_twist = AckermannDrive()
	ackermann_twist.steering_angle = steering_angle

	if btn_a > 0:
		ackermann_twist.speed = 80.0
	elif btn_x > 0:
		ackermann_twist.speed = 150.0
	else:
		ackermann_twist.speed = 120.0

	pub.publish(ackermann_twist)

def transformAnalogToSteerAngle(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

if __name__ == "__main__":
	rospy.init_node('movr_teleop_joy_pub')
	pub = rospy.Publisher('movr_cmd', AckermannDrive)
	sub = rospy.Subscriber("joy", Joy, joy_cb)
	rospy.spin()