cmake_minimum_required(VERSION 3.26)
project(MicrobialWorld)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)


find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(MicrobialWorld main.cpp
        Biologist.h
        Bacterium.h
        Service.cpp
        Service.h
        window.cpp
        window.h
        window.ui
        BacteriaTable.cpp
        BacteriaTable.h)
target_link_libraries(MicrobialWorld
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

