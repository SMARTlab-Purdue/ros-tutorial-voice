#!/usr/bin/env python

"""
voice_cmd_vel.py is a simple demo of speech recognition.
  You can control a mobile base using commands found
  in the corpus file.
"""

import roslib; roslib.load_manifest('pocketsphinx')
import rospy
import math
import time


from geometry_msgs.msg import Twist
from std_msgs.msg import String, Bool
#from std_msgs.msg import Bool

class voice_cmd_vel:

    def __init__(self):
        rospy.on_shutdown(self.cleanup)
        self.speed = 0.2
        self.twist_msg = Twist()
        self.bool_msg = Bool()

        # publish to cmd_vel, subscribe to speech output
        self.pub_vel = rospy.Publisher('cmd_vel', Twist)
        self.pub_bool = rospy.Publisher('voice_command', Bool)
        rospy.Subscriber('recognizer/output', String, self.speechCb)

        #r = rospy.Rate(10.0)
	rospy.spin()
        #while not rospy.is_shutdown():
            #self.pub_vel.publish(self.twist_msg)
            #self.bool_msg.data = True
            #self.pub_bool.publish(self.bool_msg)
            #r.sleep()
        
    def speechCb(self, speech_msg):
        rospy.loginfo(speech_msg.data)

        if speech_msg.data.find("full speed") > -1:
            if self.speed == 0.2:
                self.twist_msg.linear.x = self.twist_msg.linear.x*2
                self.twist_msg.angular.z = self.twist_msg.angular.z*2
                self.speed = 0.4
        if speech_msg.data.find("half speed") > -1:
            if self.speed == 0.4:
                self.twist_msg.linear.x = self.twist_msg.linear.x/2
                self.twist_msg.angular.z = self.twist_msg.angular.z/2
                self.speed = 0.2

        if speech_msg.data.find("forward") > -1:    
            self.twist_msg.linear.x = self.speed
            self.twist_msg.angular.z = 0
        elif speech_msg.data.find("left") > -1:
		self.twist_msg.linear.x = 0
                self.twist_msg.angular.z = self.speed*2
        elif speech_msg.data.find("right") > -1:   
		self.twist_msg.linear.x = 0         
                self.twist_msg.angular.z = -self.speed*2
        elif speech_msg.data.find("back") > -1:
            self.twist_msg.linear.x = -self.speed
            self.twist_msg.angular.z = 0
	elif speech_msg.data.find("move one meter") > -1:
	    t_end = time.time() + 5
	    while time.time() < t_end:
	    	self.twist_msg.linear.x = self.speed
            	self.twist_msg.angular.z = 0    
        	self.pub_vel.publish(self.twist_msg)  
	elif speech_msg.data.find("move two meters") > -1:
	    t_end = time.time() + 10
	    while time.time() < t_end:
	    	self.twist_msg.linear.x = self.speed
            	self.twist_msg.angular.z = 0    
        	self.pub_vel.publish(self.twist_msg)
	elif speech_msg.data.find("move three meters") > -1:
	    t_end = time.time() + 15
	    while time.time() < t_end:
	    	self.twist_msg.linear.x = self.speed
            	self.twist_msg.angular.z = 0    
        	self.pub_vel.publish(self.twist_msg)

        elif speech_msg.data.find("stop") > -1 or speech_msg.data.find("halt") > -1:          
            self.twist_msg = Twist()

        
        
        self.pub_vel.publish(self.twist_msg)
        self.bool_msg.data = True
        self.pub_bool.publish(self.bool_msg)

    def cleanup(self):
        # stop the robot!
        twist = Twist()
        #bool_r = Bool()
        #bool_r.data = False
        self.pub_vel.publish(twist)
        #self.pub_bool.publish(bool_r)

if __name__=="__main__":
    rospy.init_node('voice_cmd_vel')
    try:
        voice_cmd_vel()
    except:
        pass
