#!/usr/bin/env python
import rospy
from tf2_msgs.msg import TFMessage
from std_msgs.msg import String
from std_msgs.msg import Empty
	
def handle_tag(tag):
	id = tag.transforms[0].child_frame_id

	#0
	if id == "takeoff" : 
		pub = rospy.Publisher("bebop/takeoff", Empty, queue_size=10)
		rospy.init_node('subscriber', anonymous=True)
	
	#3
	if id == "land":
		pub = rospy.Publisher("bebop/land", Empty, queue_size=10)
		#rospy.init_node('subscriber', anonymous=True)

	#2
	#if id == "left": 
		#publish message

	#1
	#if id == "right":
		#publish message
	
	rospy.loginfo(rospy.get_caller_id() + "I heard something %s", id)

def main():
	rospy.init_node('subscriber', anonymous=True)
	rospy.Subscriber("/tf", TFMessage, handle_tag)
	rospy.spin()

if __name__=="__main__":	
	main()

#/tf tf2_msgs/TFMessage
#/tag_detection apriltags2_ros/AprilTagDetectectionArray

'''
transforms: 
  - 
    header: 
      seq: 0
      stamp: 
        secs: 1555798866
        nsecs: 113669351
      frame_id: "camera_base_link"
    child_frame_id: "camera_pan_link"
    transform: 
      translation: 
        x: 0.0
        y: 0.0
        z: 0.0
      rotation: 
        x: 0.0
        y: 0.0
        z: 0.0
        w: 1.0
'''
'''
rostopic pub /tf tf2_msgs/TFMessage "transforms: 
  - 
    header: 
      seq: 0
      stamp: 
        secs: 1555798866
        nsecs: 113669351
      frame_id: "camera_base_link"
    child_frame_id: "takeoff"
    transform: 
      translation: 
        x: 0.0
        y: 0.0
        z: 0.0
      rotation: 
        x: 0.0
        y: 0.0
        z: 0.0
        w: 1.0"
'''