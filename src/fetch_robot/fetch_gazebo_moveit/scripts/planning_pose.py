#!/usr/bin/env python3
import rospy
from moveit_msgs.msg import MoveItErrorCodes
from moveit_python import MoveGroupInterface, PlanningSceneInterface
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

if __name__ == '__main__':
    rospy.init_node("planningforpose")
    move_group = MoveGroupInterface("arm", "base_link")

    gripper_frame = 'wrist_roll_link'
    # set two poses for the gripper to move around"
    gripper_poses = [Pose(Point(0.1, 0.384, 1.326),
                          Quaternion(0.173, -0.693, -0.242, 0.657)),
                     Pose(Point(0.1, 0.545, 1.322),
                          Quaternion(-0.274, -0.701, 0.173, 0.635))]

    gripper_pose_stamped = PoseStamped()
    gripper_pose_stamped.header.frame_id = 'base_link'

    while not rospy.is_shutdown():
        for pose in gripper_poses:
            gripper_pose_stamped.header.stamp = rospy.Time.now()
            # Set the message pose
            gripper_pose_stamped.pose = pose
            # planning for the pose
            move_group.moveToPose(gripper_pose_stamped, gripper_frame)
            result = move_group.get_move_action().get_result()

            if result:
                if result.error_code.val == MoveItErrorCodes.SUCCESS:
                    rospy.loginfo("Hello there!")
                else:
                    rospy.logerr("Arm goal in state: %s",
                                 move_group.get_move_action().get_state())
            else:
                rospy.logerr("Failure no result returned.")

    # This stops all arm movement goals
    move_group.get_move_action().cancel_all_goals()
