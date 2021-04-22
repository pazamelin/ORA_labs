# Works with 3.11 and tested through 3.19
cmake_minimum_required(VERSION 3.1...3.19)

# Project name and a few useful settings. Other commands can pick up the results
project(ORA_labs
        VERSION 0.1
        LANGUAGES CXX)

# Optionally set things like CMAKE_CXX_STANDARD, CMAKE_POSITION_INDEPENDENT_CODE here
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_EXTENSIONS OFF)

# Build options
option(BUILD_TESTS "build tests executables" ON)

# Options' status
message(STATUS "BUILD_TESTS: ${BUILD_TESTS}")

## [testing]
enable_testing()
# Include the Catch2 testing library local header-only directory
include_directories(PRIVATE extern/)

set(CATCH_PATH "${PROJECT_SOURCE_DIR}/extern/")

macro(register_test TEST_NAME)
    if (BUILD_TESTS)
        # Tests need to be added as executables first
        add_executable(${TEST_NAME} ${TEST_NAME}.cpp)

        target_include_directories(${TEST_NAME} PRIVATE ${CATCH_PATH})
        # If you register a test, then ctest and make test will run it.
        # You can also run examples and check the output, as well.
        add_test(NAME ${TEST_NAME} COMMAND ${TEST_NAME}) # Command can be a target
    endif ()
endmacro(register_test)

add_subdirectory(string_matching)
