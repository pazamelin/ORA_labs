include_directories(PRIVATE ../../extern)

# Tests need to be added as executables first
add_executable(unit unit.cpp)
add_executable(stress stress.cpp)

# I'm using C++17 in the test
target_compile_features(unit PRIVATE cxx_std_17)
target_compile_features(stress PRIVATE cxx_std_17)

# Should be linked to the main library
target_link_libraries(unit PRIVATE liblab1)
target_link_libraries(stress PRIVATE liblab1)

# If you register a test, then ctest and make test will run it.
# You can also run examples and check the output, as well.
add_test(NAME unit COMMAND unit) # Command can be a target
add_test(NAME stress COMMAND stress) # Command can be a target
