cmake_minimum_required(VERSION 3.26)
project(Search_Engine)

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

add_executable(Search_Engine main.cpp
        gui.cpp
        gui.h
        gui.ui
        service.cpp
        service.h
        domain.cpp
        domain.h)
target_link_libraries(Search_Engine
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

