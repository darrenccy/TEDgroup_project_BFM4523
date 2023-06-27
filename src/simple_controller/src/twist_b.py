#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("twist_publisher")

# Add a delay of 1 second for node initialization
rospy.sleep(1.0)

pub = rospy.Publisher("/r2d2_diff_drive_controller/cmd_vel", Twist, queue_size=1)

rate = rospy.Rate(10)  # 10 Hz

start_time = rospy.get_time()
while rospy.get_time() - start_time < 29.0:  # Run for 29 seconds in total
    twist = Twist()
    if rospy.get_time() - start_time < 6.9:  # Twist clockwise for 6.9 seconds
        twist.angular.z = 1.0  # Adjust the angular velocity as desired
    else:  # Move linearly for 22.1 seconds
        twist.linear.x = 1.5  # Adjust the linear velocity as desired
    pub.publish(twist)
    rate.sleep()
