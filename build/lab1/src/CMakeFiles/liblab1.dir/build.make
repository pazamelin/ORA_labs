# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pazamelin/github/ORA_labs

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pazamelin/github/ORA_labs/build

# Include any dependencies generated for this target.
include lab1/src/CMakeFiles/liblab1.dir/depend.make

# Include the progress variables for this target.
include lab1/src/CMakeFiles/liblab1.dir/progress.make

# Include the compile flags for this target's objects.
include lab1/src/CMakeFiles/liblab1.dir/flags.make

lab1/src/CMakeFiles/liblab1.dir/naive.cpp.o: lab1/src/CMakeFiles/liblab1.dir/flags.make
lab1/src/CMakeFiles/liblab1.dir/naive.cpp.o: ../lab1/src/naive.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pazamelin/github/ORA_labs/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lab1/src/CMakeFiles/liblab1.dir/naive.cpp.o"
	cd /home/pazamelin/github/ORA_labs/build/lab1/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/liblab1.dir/naive.cpp.o -c /home/pazamelin/github/ORA_labs/lab1/src/naive.cpp

lab1/src/CMakeFiles/liblab1.dir/naive.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/liblab1.dir/naive.cpp.i"
	cd /home/pazamelin/github/ORA_labs/build/lab1/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pazamelin/github/ORA_labs/lab1/src/naive.cpp > CMakeFiles/liblab1.dir/naive.cpp.i

lab1/src/CMakeFiles/liblab1.dir/naive.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/liblab1.dir/naive.cpp.s"
	cd /home/pazamelin/github/ORA_labs/build/lab1/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pazamelin/github/ORA_labs/lab1/src/naive.cpp -o CMakeFiles/liblab1.dir/naive.cpp.s

lab1/src/CMakeFiles/liblab1.dir/rabin_karp.cpp.o: lab1/src/CMakeFiles/liblab1.dir/flags.make
lab1/src/CMakeFiles/liblab1.dir/rabin_karp.cpp.o: ../lab1/src/rabin_karp.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pazamelin/github/ORA_labs/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object lab1/src/CMakeFiles/liblab1.dir/rabin_karp.cpp.o"
	cd /home/pazamelin/github/ORA_labs/build/lab1/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/liblab1.dir/rabin_karp.cpp.o -c /home/pazamelin/github/ORA_labs/lab1/src/rabin_karp.cpp

lab1/src/CMakeFiles/liblab1.dir/rabin_karp.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/liblab1.dir/rabin_karp.cpp.i"
	cd /home/pazamelin/github/ORA_labs/build/lab1/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pazamelin/github/ORA_labs/lab1/src/rabin_karp.cpp > CMakeFiles/liblab1.dir/rabin_karp.cpp.i

lab1/src/CMakeFiles/liblab1.dir/rabin_karp.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/liblab1.dir/rabin_karp.cpp.s"
	cd /home/pazamelin/github/ORA_labs/build/lab1/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pazamelin/github/ORA_labs/lab1/src/rabin_karp.cpp -o CMakeFiles/liblab1.dir/rabin_karp.cpp.s

# Object files for target liblab1
liblab1_OBJECTS = \
"CMakeFiles/liblab1.dir/naive.cpp.o" \
"CMakeFiles/liblab1.dir/rabin_karp.cpp.o"

# External object files for target liblab1
liblab1_EXTERNAL_OBJECTS =

lab1/src/libliblab1.a: lab1/src/CMakeFiles/liblab1.dir/naive.cpp.o
lab1/src/libliblab1.a: lab1/src/CMakeFiles/liblab1.dir/rabin_karp.cpp.o
lab1/src/libliblab1.a: lab1/src/CMakeFiles/liblab1.dir/build.make
lab1/src/libliblab1.a: lab1/src/CMakeFiles/liblab1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pazamelin/github/ORA_labs/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library libliblab1.a"
	cd /home/pazamelin/github/ORA_labs/build/lab1/src && $(CMAKE_COMMAND) -P CMakeFiles/liblab1.dir/cmake_clean_target.cmake
	cd /home/pazamelin/github/ORA_labs/build/lab1/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/liblab1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lab1/src/CMakeFiles/liblab1.dir/build: lab1/src/libliblab1.a

.PHONY : lab1/src/CMakeFiles/liblab1.dir/build

lab1/src/CMakeFiles/liblab1.dir/clean:
	cd /home/pazamelin/github/ORA_labs/build/lab1/src && $(CMAKE_COMMAND) -P CMakeFiles/liblab1.dir/cmake_clean.cmake
.PHONY : lab1/src/CMakeFiles/liblab1.dir/clean

lab1/src/CMakeFiles/liblab1.dir/depend:
	cd /home/pazamelin/github/ORA_labs/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pazamelin/github/ORA_labs /home/pazamelin/github/ORA_labs/lab1/src /home/pazamelin/github/ORA_labs/build /home/pazamelin/github/ORA_labs/build/lab1/src /home/pazamelin/github/ORA_labs/build/lab1/src/CMakeFiles/liblab1.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lab1/src/CMakeFiles/liblab1.dir/depend

