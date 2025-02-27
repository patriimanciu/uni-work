cmake_minimum_required(VERSION 3.26)
project(ArtAuction)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)



find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(ArtAuction main.cpp
        User.cpp
        User.h
        Item.cpp
        Item.h
        Session.cpp
        Session.h
        Subject.h
        Observer.h
        window.cpp
        window.h
        window.ui)
target_link_libraries(ArtAuction
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

