#deactivate
#conda init
#conda create -n ROS python=3.9
#conda activate ROS
conda config --add channels conda-forge
conda config --add channels robostack
conda config --set channel_priority strict
conda install ros-noetic-desktop-full
conda install compilers cmake pkg-config make ninja catkin_tools
#conda deactivate
#conda activate ros