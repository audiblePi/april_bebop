#include <ros/ros.h>
#include <std_msgs/Empty.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "publisher");
    ros::NodeHandle node;

    ros::Publisher pub_takeoff = node.advertise<std_msgs::Empty>("/bebop/takeoff", 1);
    
    ros::Publisher pub_land = node.advertise<std_msgs::Empty>("/bebop/land", 1);

    ros::Rate rate(1);

    std_msgs::Empty msg;

    while(ros::ok()) {
        // pub_takeoff.publish(msg);
        // rate.sleep();

        //pub_land.publish(msg);
        //rate.sleep();
    }
}