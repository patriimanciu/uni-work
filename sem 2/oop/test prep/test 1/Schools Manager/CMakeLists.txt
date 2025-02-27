cmake_minimum_required(VERSION 3.26)
project(Schools_Manager)

set(CMAKE_CXX_STANDARD 17)

add_executable(Schools_Manager main.cpp
        repository/DynamicVector.h
        domain/school.cpp
        domain/school.h
        repository/repo.cpp
        repository/repo.h
        service/service.cpp
        service/service.h
        ui/ui.cpp
        ui/ui.h)
