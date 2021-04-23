add_executable(run run.cpp)

# Using C++17 as the main lib
target_compile_features(run PRIVATE cxx_std_17)
# Should be linked to the main library
target_link_libraries(run PRIVATE liblab1)
