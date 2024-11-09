#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

# 全局变量，存储两只乌龟的位置信息
turtle1_pose = Pose()
turtle2_pose = Pose()


def turtle1_pose_callback(msg):
    global turtle1_pose
    turtle1_pose = msg


def turtle2_pose_callback(msg):
    global turtle2_pose
    turtle2_pose = msg


def move_turtle():
    rospy.init_node('turtle_follow', anonymous=True)

    # 订阅乌龟位姿
    rospy.Subscriber('/turtle1/pose', Pose, turtle1_pose_callback)
    rospy.Subscriber('/turtle2/pose', Pose, turtle2_pose_callback)

    # 发布控制 turtle2 的速度话题
    vel_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 设置更新频率为 10Hz

    while not rospy.is_shutdown():
        # 计算 turtle2 跟随 turtle1 的速度控制
        vel_msg = Twist()

        # 计算距离
        distance = math.sqrt((turtle1_pose.x - turtle2_pose.x) ** 2 + (turtle1_pose.y - turtle2_pose.y) ** 2)

        # 当距离大于 0.5 时，调整 turtle2 的线速度和角速度
        if distance > 0.5:
            # 线速度
            vel_msg.linear.x = 1.0 * distance
            # 角速度
            vel_msg.angular.z = 4.0 * (math.atan2(turtle1_pose.y - turtle2_pose.y,
                                                  turtle1_pose.x - turtle2_pose.x) - turtle2_pose.theta)
        else:
            # 停止移动
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0

        # 发布速度消息
        vel_pub.publish(vel_msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
