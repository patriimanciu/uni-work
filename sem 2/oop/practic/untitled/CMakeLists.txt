cmake_minimum_required(VERSION 3.26)
project(Research2)

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

add_executable(untitled main.cpp
        window.cpp
        window.h
        window.ui
        Idea.cpp
        Idea.h
        Idea.h
        Researcher.cpp
        Researcher.h
        Service.cpp
        Service.h
        IdeaTableModel.cpp
        IdeaTableModel.h
)
target_link_libraries(untitled
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

