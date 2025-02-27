cmake_minimum_required(VERSION 3.26)
project(Weather)

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

add_executable(Weather main.cpp
        gui.cpp
        gui.h
        gui.ui
        Service.cpp
        Service.h
        Domain.cpp
        Domain.h)
target_link_libraries(Weather
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

