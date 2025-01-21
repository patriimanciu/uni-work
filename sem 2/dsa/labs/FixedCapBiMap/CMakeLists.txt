cmake_minimum_required(VERSION 3.22.4)
project(a)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(app
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        FixedCapBiMap.h
        FixedCapBiMap.cpp
        FixedCapBiMapIterator.cpp
        FixedCapBiMapIterator.h
        ShortTest.cpp
        ShortTest.h
        ExtraTest.cpp
        ExtraTest.h
        )

target_compile_options(app PRIVATE -g -Wall -O2)