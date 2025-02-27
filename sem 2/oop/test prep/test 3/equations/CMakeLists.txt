cmake_minimum_required(VERSION 3.26)
project(equations)

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

# Add all your source files to the executable
add_executable(equations
        main.cpp
        gui.cpp
        gui.h
        gui.ui
        domain.cpp
        domain.h
        service.cpp
        service.h
)

# Link Qt libraries to the executable
target_link_libraries(equations
        Qt6::Core
        Qt6::Gui
        Qt6::Widgets
)
