PROJECT(MyHello)
cmake_minimum_required(VERSION 2.8)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_EXECUTABLE(client client.cpp)
TARGET_LINK_LIBRARIES(client ${CONAN_LIBS})
