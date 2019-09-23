#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image


def callback(data):
    rospy.loginto(rospy.get_caller_id() + str(data.data))
    print(data.data)


def listener():
    rospy.init_node('vidFeed', anonymous=True)

    rospy.Subscriber('/bot/camera1/image_raw', Image, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
