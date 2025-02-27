cmake_minimum_required(VERSION 3.26)
project(Task_Manager)

set(CMAKE_CXX_STANDARD 17)

add_executable(Task_Manager main.cpp
        DynamicVector.h
        domain/Task.cpp
        domain/Task.h
        repository/Repository.cpp
        repository/Repository.h
        service/Service.cpp
        service/Service.h
        ui/UI.cpp
        ui/UI.h)
