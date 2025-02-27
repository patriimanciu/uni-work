cmake_minimum_required(VERSION 3.26)
project(Car_Manager)

set(CMAKE_CXX_STANDARD 17)

add_executable(Car_Manager main.cpp
        DynamicVector.h
        domain/car.cpp
        domain/car.h
        repository/repo.cpp
        repository/repo.h
        service/service.cpp
        service/service.h
        ui/ui.cpp
        ui/ui.h)
