# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.10

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

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2018.1.2\bin\cmake\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2018.1.2\bin\cmake\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/Tutorial.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Tutorial.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Tutorial.dir/flags.make

CMakeFiles/Tutorial.dir/main.cpp.obj: CMakeFiles/Tutorial.dir/flags.make
CMakeFiles/Tutorial.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Tutorial.dir/main.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\Tutorial.dir\main.cpp.obj -c D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial\main.cpp

CMakeFiles/Tutorial.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Tutorial.dir/main.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial\main.cpp > CMakeFiles\Tutorial.dir\main.cpp.i

CMakeFiles/Tutorial.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Tutorial.dir/main.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial\main.cpp -o CMakeFiles\Tutorial.dir\main.cpp.s

CMakeFiles/Tutorial.dir/main.cpp.obj.requires:

.PHONY : CMakeFiles/Tutorial.dir/main.cpp.obj.requires

CMakeFiles/Tutorial.dir/main.cpp.obj.provides: CMakeFiles/Tutorial.dir/main.cpp.obj.requires
	$(MAKE) -f CMakeFiles\Tutorial.dir\build.make CMakeFiles/Tutorial.dir/main.cpp.obj.provides.build
.PHONY : CMakeFiles/Tutorial.dir/main.cpp.obj.provides

CMakeFiles/Tutorial.dir/main.cpp.obj.provides.build: CMakeFiles/Tutorial.dir/main.cpp.obj


# Object files for target Tutorial
Tutorial_OBJECTS = \
"CMakeFiles/Tutorial.dir/main.cpp.obj"

# External object files for target Tutorial
Tutorial_EXTERNAL_OBJECTS =

Tutorial.exe: CMakeFiles/Tutorial.dir/main.cpp.obj
Tutorial.exe: CMakeFiles/Tutorial.dir/build.make
Tutorial.exe: CMakeFiles/Tutorial.dir/linklibs.rsp
Tutorial.exe: CMakeFiles/Tutorial.dir/objects1.rsp
Tutorial.exe: CMakeFiles/Tutorial.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Tutorial.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\Tutorial.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Tutorial.dir/build: Tutorial.exe

.PHONY : CMakeFiles/Tutorial.dir/build

CMakeFiles/Tutorial.dir/requires: CMakeFiles/Tutorial.dir/main.cpp.obj.requires

.PHONY : CMakeFiles/Tutorial.dir/requires

CMakeFiles/Tutorial.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Tutorial.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Tutorial.dir/clean

CMakeFiles/Tutorial.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial\cmake-build-debug D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial\cmake-build-debug D:\KikoBrothers\Jerry\Documents\Programming\C-C++\Tutorial\cmake-build-debug\CMakeFiles\Tutorial.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Tutorial.dir/depend

