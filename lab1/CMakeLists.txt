# Works with 3.11 and tested through 3.20
cmake_minimum_required(VERSION 3.11...3.20)

# Project name and a few useful settings. Other commands can pick up the results
project(LAB1
        VERSION 0.1
        DESCRIPTION ""
        LANGUAGES CXX)

# The compiled library code is here
add_subdirectory(src)

# Testing only available if this is the main app
# Emergency override MODERN_CMAKE_BUILD_TESTING provided as well
if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME OR LAB1_BUILD_TESTS)
    add_subdirectory(tests)
endif()
