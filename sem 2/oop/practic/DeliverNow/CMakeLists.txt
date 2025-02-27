cmake_minimum_required(VERSION 3.26)
project(DeliverNow)

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

add_executable(DeliverNow main.cpp
        courier.h
        package.h
        DataManager.cpp
        DataManager.h
        mainwindow.cpp
        mainwindow.h
        mainwindow.ui
        courierwindow.cpp
        courierwindow.h
        courierwindow.ui
        map.cpp
        map.h
        map.ui
)
target_link_libraries(DeliverNow
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

