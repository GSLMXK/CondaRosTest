#!/usr/bin/env python
import rospy
from turtlesim.srv import Spawn


def spawn_turtle():
    rospy.init_node('spawn_turtle')
    rospy.wait_for_service('/spawn')
    index = 1
    try:
        spawn = rospy.ServiceProxy('/spawn', Spawn)
        while index <= 50:
            spawn(5.0, 5.0, 0.0, 'turtle2')
            rospy.loginfo("Spawned turtle2 at x=5.0, y=5.0")
            index += 1
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)


if __name__ == "__main__":
    spawn_turtle()
