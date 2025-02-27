cmake_minimum_required(VERSION 3.26)
project(Medical_Analyses)

set(CMAKE_CXX_STANDARD 17)

add_executable(Medical_Analyses main.cpp
        domain.cpp
        domain.h
        service.cpp
        service.h
        ui.cpp
        ui.h)
