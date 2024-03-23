cmake_minimum_required(VERSION 3.5)
project(cpp_siro)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# Agrega el ejecutable del nodo
add_executable(siro_node_suscriptor src/siro_node_suscriptor.cpp)
add_executable(siro_node_publicador src/siro_node_publicador.cpp)

# Especifica las dependencias para el ejecutable
ament_target_dependencies(siro_node_suscriptor rclcpp std_msgs)
ament_target_dependencies(siro_node_publicador rclcpp std_msgs)

# Instala el ejecutable
install(TARGETS
  siro_node_suscriptor
  siro_node_publicador
  DESTINATION lib/${PROJECT_NAME}
)

# Instala los scripts y los recursos
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
