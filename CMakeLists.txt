# Works with 3.11 and tested through 3.20
cmake_minimum_required(VERSION 3.11...3.20)

# Project name and a few useful settings. Other commands can pick up the results
project(ORA_labs
        VERSION 0.1
        DESCRIPTION ""
        LANGUAGES CXX)

# Only do these if this is the main project, and not if it is included through add_subdirectory
if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)

    # Optionally set things like CMAKE_CXX_STANDARD, CMAKE_POSITION_INDEPENDENT_CODE here

    # Let's ensure -std=c++xx instead of -std=g++xx
    set(CMAKE_CXX_EXTENSIONS OFF)

    # Let's nicely support folders in IDEs
    set_property(GLOBAL PROPERTY USE_FOLDERS ON)

    # Testing only available if this is the main app
    # Note this needs to be done in the main CMakeLists
    # since it calls enable_testing, which must be in the
    # main CMakeLists.
    include(CTest)
endif()

# Testing option
option(LAB1_BUILD_TESTS "build tests executables" ON)
message(STATUS "LAB1_BUILD_TESTS : ${LAB1_BUILD_TESTS}")

# Testing option
option(LAB2_BUILD_TESTS "build tests executables" ON)
message(STATUS "LAB2_BUILD_TESTS : ${LAB2_BUILD_TESTS}")

# Testing option
option(LAB3_BUILD_TESTS "build tests executables" ON)
message(STATUS "LAB3_BUILD_TESTS : ${LAB3_BUILD_TESTS}")

# Testing option
option(LAB4_BUILD_TESTS "build tests executables" ON)
message(STATUS "LAB4_BUILD_TESTS : ${LAB4_BUILD_TESTS}")

# Add sub directories
add_subdirectory(lab1)
