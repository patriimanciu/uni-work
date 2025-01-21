cmake_minimum_required(VERSION 3.26)
project(Stack)

set(CMAKE_CXX_STANDARD 17)

add_executable(Stack App.cpp
    Stack.cpp
    Stack.h
    ExtendedTest.cpp
    ExtendedTest.h
    ShortTest.cpp
    ShortTest.h
        ExtraTest.cpp
        ExtraTest.h
)
