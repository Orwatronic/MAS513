#! /usr/bin/env python
import sys
import rospy
import moveit_commander
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
robot = moveit_commander.RobotCommander()

arm_group = moveit_commander.MoveGroupCommander("manipulator")
# Put the arm in the --- position
arm_group.set_named_target("up")
plan1 = arm_group.go()

rospy.sleep(10)
moveit_commander.rosccp_shutdown()