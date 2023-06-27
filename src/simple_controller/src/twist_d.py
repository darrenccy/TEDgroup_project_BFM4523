#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("twist_publisher")

# Add a delay of 1 second for node initialization
rospy.sleep(1.0)

pub = rospy.Publisher("/r2d2_diff_drive_controller/cmd_vel", Twist, queue_size=1)

rate = rospy.Rate(10)  # 10 Hz

    
start_time = rospy.get_time()
while rospy.get_time() - start_time < 27.4:  # Run for 27.4 seconds in total
    twist = Twist()
    if rospy.get_time() - start_time < 7.4:  # Twist clockwise for 7.4 seconds
        twist.angular.z = 1.0  # Adjust the angular velocity as desired
    
    elif rospy.get_time() - start_time < 19.9:  # Move forward for 12.5 seconds
        twist.linear.x = 1.5  # Adjust the linear velocity as desired
    
    elif rospy.get_time() - start_time < 24.9:  # Twist counterclockwise for 5 seconds
        twist.angular.z = 1.0  # Adjust the angular velocity as desired
    
    else:  # Reverse for 2.5 seconds
        twist.linear.x = -1.5  # Adjust the linear velocity as desired
        
    pub.publish(twist)
    rate.sleep()
