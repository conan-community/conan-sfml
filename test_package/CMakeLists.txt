PROJECT(MyHello)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP(TARGETS)

add_executable(example example.cpp)
target_link_libraries(example CONAN_PKG::SFML)
