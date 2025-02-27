cmake_minimum_required(VERSION 3.26)
project(Task_Manager)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH "/opt/homebrew/opt/qt")

find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(Task_Manager main.cpp
        Domain.cpp
        Domain.h
        Service.cpp
        Service.h
        gui.cpp
        gui.h
        gui.ui)
target_link_libraries(Task_Manager
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

