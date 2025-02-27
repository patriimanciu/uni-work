cmake_minimum_required(VERSION 3.26)
project(Research)

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

add_executable(Research main.cpp
        Data.cpp
        Data.h
        seniorwindow.cpp
        seniorwindow.h
        seniorwindow.ui
        juniorwindow.cpp
        juniorwindow.h
        juniorwindow.ui
        Observer.cpp
        Observer.h)
target_link_libraries(Research
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

