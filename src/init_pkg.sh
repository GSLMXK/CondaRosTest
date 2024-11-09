# work in src
pkg_name=turtle_demo
catkin_create_pkg $pkg_name rospy
mkdir -p $pkg_name/launch
touch $pkg_name/launch/$pkg_name.launch
mkdir $pkg_name/scripts