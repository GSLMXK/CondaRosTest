#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 该例程将请求/show_person 服务，服务数据类型为 learning_service::Person 

import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')
    # tfBuffer = tf2_ros.Buffer()
    listener = tf.TransformListener()

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    # turtle_name = rospy.get_param("turtle","turtle2")
    spawner(4, 2, 0, "turtle2")

    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform("/turtle2", '/turtle1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        # rospy.loginfo("listener:%s" % turtle_name)

        turtle_vel.publish(cmd)
        rate.sleep()
