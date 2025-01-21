cmake_minimum_required(VERSION 3.26)
project(Queue)

set(CMAKE_CXX_STANDARD 17)

add_executable(Queue App.cpp
        Queue.cpp
        Queue.h
        ExtendedTest.cpp
        ExtendedTest.h
        ShortTest.cpp
        ShortTest.h)
