#!/usr/bin/env python3
import actionlib
import rospy

from math import sin, cos
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from control_msgs.msg import PointHeadAction, PointHeadGoal
# from moveit_python.geometry import rotate_pose_msg_by_euler_angles

# Move base using navigation stack
class MoveBaseClient(object):

    def __init__(self):
        self.client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Waiting for move_base...")
        self.client.wait_for_server()

    def goto(self, x, y, theta, frame="map"):
        move_goal = MoveBaseGoal()
        move_goal.target_pose.pose.position.x = x
        move_goal.target_pose.pose.position.y = y
        move_goal.target_pose.pose.orientation.z = sin(theta/2.0)
        move_goal.target_pose.pose.orientation.w = cos(theta/2.0)
        move_goal.target_pose.header.frame_id = frame
        move_goal.target_pose.header.stamp = rospy.Time.now()

        # TODO wait for things to work
        self.client.send_goal(move_goal)
        self.client.wait_for_result()

# Point the head using controller
class PointHeadClient(object):

    def __init__(self):
        self.client = actionlib.SimpleActionClient("head_controller/point_head", PointHeadAction)
        rospy.loginfo("Waiting for head_controller...")
        self.client.wait_for_server()

    def look_at(self, x, y, z, frame, duration=1.0):
        goal = PointHeadGoal()
        goal.target.header.stamp = rospy.Time.now()
        goal.target.header.frame_id = frame
        goal.target.point.x = x
        goal.target.point.y = y
        goal.target.point.z = z
        goal.min_duration = rospy.Duration(duration)
        self.client.send_goal(goal)
        self.client.wait_for_result()

if __name__ == "__main__":
    # Create a node
    rospy.init_node("move2point")

    # Make sure sim time is working
    while not rospy.Time.now():
        pass

    # Setup clients
    move_base = MoveBaseClient()
    head_action = PointHeadClient()

    rospy.loginfo("Moving to the first point...")
    move_base.goto(2.0, 2.0, 0.0)
    head_action.look_at(2.0, 4.0, 0.0, "base_link")
    

    # Move to second point
    rospy.loginfo("Moving to the second point...")
    move_base.goto(-1.0, 1., 0)
    head_action.look_at(-1.0, 2.0, 0.0, "base_link")