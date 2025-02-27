cmake_minimum_required(VERSION 3.26)
project(Real_Estate_Agency)

set(CMAKE_CXX_STANDARD 17)

add_executable(Real_Estate_Agency main.cpp
        ui.cpp
        ui.h
        domain.cpp
        domain.h)
