cmake_minimum_required(VERSION 3.8)
project(pkg03_topic_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(pkg00_interfaces REQUIRED)

############################################################
add_executable(demo02_talker_cpp src/demo02_talker_cpp.cpp)
add_executable(demo02_listener_cpp src/demo02_listener_cpp.cpp)

ament_target_dependencies(
  demo02_talker_cpp
  "rclcpp"
  "pkg00_interfaces"
)
ament_target_dependencies(
  demo02_listener_cpp
  "rclcpp"
  "pkg00_interfaces"
)

install(TARGETS 
  demo02_talker_cpp
  demo02_listener_cpp
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

############################################################

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
