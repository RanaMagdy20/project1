#!/bin/env python3
import rospy 
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
import math 
import time
x=0
y=0
w=0
def poseback (posemsg):
    global x 
    global y, w
    x=posemsg.x
    y=posemsg.y
    w=posemsg.theta

def goal(xfinal , yfinal):
    global x
    global y,w
    vel_msg = Twist()
   
    while (True) :
        Klinear =0.5
        #Klinear= rospy.get_param("/Klinear")
        dist=math.sqrt(((xfinal-x)**2)+((yfinal-y)**2))
        linearspeed=dist*Klinear
        kangular=4.0
        #kangular= rospy.get_param("/kangular")
        finalangle=math.atan2(yfinal - y , xfinal - x)
        angspeed=(finalangle-w)*kangular
        vel_msg.linear.x=linearspeed
        vel_msg.angular.z=angspeed
        pub.publish(vel_msg)
        if (dist<=0.01):
            break
if __name__ == "__main__":
    rospy.init_node("hello")        
    rospy.loginfo("Start")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose",Pose,callback=poseback)
    rate = rospy.Rate(2) 
    xfinal= rospy.get_param("/xfinal")
    yfinal= rospy.get_param("/yfinal")
    goal(xfinal,yfinal)
    

   
    #while not rospy.is_shutdown():
    #xfinal=10
    #yfinal=1
    
    #while not rospy.is_shutdown():
    #
        #in_x=float(input('enter x'))
        #in_y=float(input('enter y'))
       
    
   
