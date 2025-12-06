import launch
import launch_ros

def generate_launch_description():
    talker = launch_ros.actions.Node(
        package='pkg03_topic_py',
        executable='demo02_talker_py',
        output='screen'
    )
    
    listener = launch_ros.actions.Node(
        package='pkg03_topic_py',
        executable='demo02_listener_py',
        output='screen'
    )
    
    launch_description = launch.LaunchDescription([
        talker,
        listener,
    ])
    
    return launch_description