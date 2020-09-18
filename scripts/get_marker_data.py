#!/usr/bin/env python

import rospy
import roslib
import tf

from geometry_msgs.msg import PoseArray
#from geometry_msgs.msg import Pose

#Define a class
class Whycon_detect():

	def __init__(self):
		#self.pose = Pose()
		rospy.init_node('whycon_detection',anonymous=True) # Initiating a node with name whycon detection
		self.whycon_coordinates = {} #Declaring a ditionary named whycon_coordinates
		rospy.Subscriber('/whycon/poses',PoseArray,self.whycon_callback)
	def whycon_callback(self,data):
		self.position_coordinates = []
		for i in range(len(data.poses)):
    			self.position_coordinates.append([data.poses[i].position.x, data.poses[i].position.y, data.poses[i].position.z])
        		self.whycon_coordinates[int(i)] = self.position_coordinates[i]
		print self.whycon_coordinates


if __name__=="__main__":
	marker = Whycon_detect()
	while not rospy.is_shutdown():
		rospy.spin()