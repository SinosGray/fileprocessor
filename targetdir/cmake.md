---
categories:
- null
date: 2023-01-07 15:38:00
password: null
sticky: 100
tags:
- project
- executable
- library
- build
- libraries
title: cmake
---

> 

<!--more-->

# 常用命令

- **ADD_LIBRARY**
  
  语法 : `ADD_LIBRARY(<name> [STATIC | SHARED | MODULE] [source1] [source2 ...])`
  
  根据源码文件生成目标库。
  
  `STATIC`,`SHARED` 或者 `MODULE` 可以指定要创建的库的类型。 STATIC库是链接其他目标时使用的目标文件的存档。 SHARED库是动态链接的，并在运行时加载

- target_link_libraries
  该指令的作用为将目标文件与库文件进行链接。该指令的语法如下：
  
  ```cmake
  target_link_libraries(<target> [item1] [item2] [...]
                        [[debug|optimized|general] <item>] ...)
  ```

​    

# mac vscode cmake llvm开发环境

## 包

`brew install cmake llvm ninja pkgconfig` 

## vs 插件

cmake

cmake tools

codelldb(debug)

clangd

doxygen(快捷键产生注释)

## 配置文件

```cmake
# cmakelists.txt 
project(hello_world) 
cmake_minimum_required (VERSTON 3.15.0)
set(CMAKE_CXX_STANDARD 20) 
set(CMAKE_CXX_EXTENSTONS OFF)

add_executable(${CMAKE_PROJECT_NAME} hello.cpp)

find_package(fmt REQUIRED)

target_link_libraries(
${CMAKE_PROJECT_NAME} PRIVATE
fmt::fmt
)
```

```json
//.vscode/launch.json
{
  "version":"0.2.0",
 "configurations":{
   "type": "lldb",
   "request": "launch", 
   "name": "Debug",
   "program": "${command:cmake.LaunchTargetPath}",
   "args": [],
   "cwd": "${workspaceFolder}",
   "internalConsoleOptions": "neveropen",
   "console": "integratedTerminal"
 }
```

```
// build/compile_commands.json
// clang 实际执行编译指令
//settings->clangd settings->arguments
//clangd -help

//.clang-tidty是配置 clang-tidy 的文件
--compile-commands-dir=$(workspaceFolder}/build
--header-insertion=iwyu
--background-index
--clang-tidy
--pch-storage=memory 
-j=12
--pretty 
```

```yaml
# .clang-format
BasedOnStyle: LLVM
UseTab: Never
IndentWidth: 4
DerivePointerAlignment: false
PointerAlignment: true
AlwaysBreakAfterReturnType: None
AlwaysBreakTemplateDeclarations: true
AlwaysBreakBeforeMultilineStrings: true
AlignOperands: true
AlignAfterOpenBracket: true
AlignConsecutiveBitFields: true
AlignConsecutiveMacros: true
ConstructorInitializerAllOnOneLineOrOnePerLine: true
AllowAllConstructorInitializersOnNextLine: false
BinPackArguments: false
BinPackParameters: false
IncludeBlocks: Regroup
```

```json
// Users > akunda > Library > Application Support > Code > User > snippets > {} cpp.json
{
  "Main" : { 
    "prefix": "main",
    "body": [
      "int main(int argc, char* argc[]) {",
      "    $1",
      "    return 0;"
      "}"
      ],
    "description": "Main function"
  },
}
```

CMake：编辑用户本地 CMake 工具包 CMake: Edit User-Local CMake Kits

cmake-tools-kits.json

## 流程

`cmake config` choose toolchain

`build`

# 多层目录

主 cmakelists

```cmake
cmake_minimum_required(VERSION 3.20)
set(CMAKE_CXX_STANDARD 20)
# Set the project name
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

message(STATUS "Build in main folder")
project (project_temp
    LANGUAGES C CXX
)

set(CMAKE_CXX_STANDARD 20)

set(src_directory ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(test_directory ${CMAKE_CURRENT_SOURCE_DIR}/test)
set(tool_directory ${CMAKE_CURRENT_SOURCE_DIR}/tool)
set(build_directory ${CMAKE_CURRENT_SOURCE_DIR}/build)
set(lib_directory ${CMAKE_CURRENT_SOURCE_DIR}/lib)

include_directories("${src_directory}/module" "${src_directory}/tinyxml2") 
add_subdirectory(${src_directory}/module)       # 包含下级子目录math
add_subdirectory(${src_directory}/tinyxml2)     # 在 subdir 中寻找 cmakelists

#link_libraries("${lib_directory}/libmodule.dylib" "${lib_directory}/libtinyxml2.dylib")

# Add an executable
add_executable(${CMAKE_PROJECT_NAME}
${src_directory}/main.cpp
)

############################################################
# Create a library
############################################################

#Generate the static library from the library sources

add_library(module_library STATIC 
    ${src_directory}/module/module.cpp
    ${src_directory}/module/module.h
)

add_library(tinyxml2_library STATIC 
    ${src_directory}/tinyxml2/tinyxml2.cpp
    ${src_directory}/tinyxml2/tinyxml2.h
)
target_link_libraries(
    ${CMAKE_PROJECT_NAME}    
    module_library
    tinyxml2_library
)
```

动态库 cmakelists

```cmake
# set_property(TARGET translator_grammar PROPERTY CXX_STANDARD 17)
# target_link_libraries(translator_grammar PRIVATE diagon_base)

message(STATUS "Enter tinyxml2 folder")

set(MODULE_NAME tinyxml2)

aux_source_directory(. MODULE_SOURCE)  

add_library(${MODULE_NAME} SHARED ${MODULE_SOURCE})
```

# A intro

```cmake
cmake_minimum_required(VERSION 3.5)

# Set the project name
project (hello_cmake)

# Add an executable
add_executable(hello_cmake main.cpp)

## add_executable(${PROJECT_NAME} main.cpp)
```

The +add_executable()+ command specifies that an executable should be
build from the specified source files

The root or top level folder that you run the cmake command from is known as your
**CMAKE_BINARY_DIR** and is the root folder for all your binary files.

Out-of-Source Build

```shell
mkdir build
cd build
cmake ..
make .
./hello_cmake
```

# B header

```cmake
cmake_minimum_required(VERSION 3.5)

# Set the project name
project (hello_headers)

# Create a sources variable with a link to all cpp files to compile
set(SOURCES
    src/Hello.cpp
    src/main.cpp
)

# Add an executable with the above sources
add_executable(hello_headers ${SOURCES})

# Set the directories that should be included in the build command for this target
# when running g++ these will be included as -I/directory/path/
target_include_directories(hello_headers
    PRIVATE 
        ${PROJECT_SOURCE_DIR}/include
)
```

## cmake variables

|CMAKE_SOURCE_DIR |The root source directory

|**CMAKE_CURRENT_SOURCE_DIR** |The current source directory if using sub-projects and directories.

|**PROJECT_SOURCE_DIR** |The source directory of the current cmake project.

|**CMAKE_BINARY_DIR** |The root binary / build directory. This is the directory where you ran the cmake command.

|CMAKE_CURRENT_BINARY_DIR |The build directory you are currently in.

|PROJECT_BINARY_DIR |The build directory for the current project.

The base install location is controlled by the variable **CMAKE_INSTALL_PREFIX**

In the previous examples, when running the make command the output only
shows the status of the build. To see the full output for debugging
purposes you can add +VERBOSE=1+ flag when running make.

```shell
make clean
make VERBOSE=1
```

# C static library

```cmake
cmake_minimum_required(VERSION 3.5)

project(hello_library)

############################################################
# Create a library
############################################################

#Generate the static library from the library sources
add_library(hello_library STATIC 
    src/Hello.cpp
)

target_include_directories(hello_library
    PUBLIC 
        ${PROJECT_SOURCE_DIR}/include
)


############################################################
# Create an executable
############################################################

# Add an executable with the above sources
add_executable(hello_binary 
    src/main.cpp
)

# link the new hello_library target with the hello_binary target
target_link_libraries( hello_binary
    PRIVATE 
        hello_library
)
```

This will cause the included directory used in the following places:

* When compiling the library
* When compiling any additional target that links the library.

The meaning of scopes are:

* +PRIVATE+ - the directory is added to this target's include directories
* +INTERFACE+ - the directory is added to the include directories for any targets that link this library.
* +PUBLIC+ - As above, it is included in this library and also any targets that link this library.

# D shared library

```cmake
cmake_minimum_required(VERSION 3.5)

project(hello_library)

############################################################
# Create a library
############################################################

#Generate the shared library from the library sources
add_library(hello_library SHARED 
    src/Hello.cpp
)
#As shown below, this allows you to reference the target using the alias name when linking it against other targets.
add_library(hello::library ALIAS hello_library)


target_include_directories(hello_library
    PUBLIC 
        ${PROJECT_SOURCE_DIR}/include
)

############################################################
# Create an executable
############################################################

# Add an executable with the above sources
add_executable(hello_binary
    src/main.cpp
)

# link the new hello_library target with the hello_binary target
target_link_libraries( hello_binary
    PRIVATE 
        hello::library
)
```

**Static Libraries:** A [Static library](https://www.geeksforgeeks.org/static-vs-dynamic-libraries/) or statically-linked library is a set of routines, external functions and variables which are resolved in a caller at compile-time and copied into a target application by a compiler, linker, or binder, producing an object file and a stand-alone executable. This executable and the process of compiling it are both known as a static build of the program. Historically, libraries could only be static. They are usually faster than the shared libraries because a set of commonly used object files is put into a single library executable file. One can build multiple executables without the need to recompile the file. Because it is a single file to be built, use of link commands are simpler than shared library link commands, because you specify the name of the static library.

**Shared Libraries:** [Shared libraries](https://www.geeksforgeeks.org/working-with-shared-libraries-set-1/) are .so (or in Windows .dll, or in OS X .dylib) files. These are linked dynamically simply including the address of the library (whereas static linking is a waste of space). Dynamic linking links the libraries at the run-time. Thus, all the functions are in a special place in memory space, and every program can access them, without having multiple copies of them.

# E installation

```cmake
cmake_minimum_required(VERSION 3.5)

project(cmake_examples_install)

############################################################
# Create a library
############################################################

#Generate the shared library from the library sources
add_library(cmake_examples_inst SHARED
    src/Hello.cpp
)

target_include_directories(cmake_examples_inst
    PUBLIC 
        ${PROJECT_SOURCE_DIR}/include
)

############################################################
# Create an executable
############################################################

# Add an executable with the above sources
add_executable(cmake_examples_inst_bin
    src/main.cpp
)

# link the new hello_library target with the hello_binary target
target_link_libraries( cmake_examples_inst_bin
    PRIVATE 
        cmake_examples_inst
)

############################################################
# Install
############################################################

# Binaries
# Install the binary generated from the target cmake_examples_inst_bin target to the destination ${CMAKE_INSTALL_PREFIX}/bin
install (TARGETS cmake_examples_inst_bin
    DESTINATION bin)

# Library
# Install the shared library generated from the target cmake_examples_inst target to the destination ${CMAKE_INSTALL_PREFIX}/lib
install (TARGETS cmake_examples_inst
    LIBRARY DESTINATION lib)

# Header files
# Install the header files for developing against the cmake_examples_inst library into the ${CMAKE_INSTALL_PREFIX}/include directory.
install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/ 
    DESTINATION include)

# Config
# Install a configuration file to the destination ${CMAKE_INSTALL_PREFIX}/etc
install (FILES cmake-examples.conf
    DESTINATION etc)
```

`make install`会把文件装到/usr/local/xxx 中

to uninstall

`sudo xargs rm < install_manifest.txt`

# F build type

```cmake
cmake_minimum_required(VERSION 3.5)

# Set a default build type if none was specified
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  message("Setting build type to 'RelWithDebInfo' as none was specified.")
  set(CMAKE_BUILD_TYPE RelWithDebInfo CACHE STRING "Choose the type of build." FORCE)
  # Set the possible values of build type for cmake-gui
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release"
    "MinSizeRel" "RelWithDebInfo")
endif()

# Set the project name
project (build_type)

# Add an executable
add_executable(cmake_examples_build_type main.cpp)
```

cmake gui 本电脑装在 qt 内

# G compile flags

```cmake
cmake_minimum_required(VERSION 3.5)

# Set a default C++ compile flag
# To set additional default compile flags you can add the following to your top level CMakeLists.txt
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DEX2" CACHE STRING "Set C++ Compiler Flags" FORCE)

# Set the project name
project (compile_flags)

# Add an executable
add_executable(cmake_examples_compile_flags main.cpp)

# compile flag
target_compile_definitions(cmake_examples_compile_flags 
    PRIVATE EX3
)
```

# H third party lib

```cmake
cmake_minimum_required(VERSION 3.5)

# Set the project name
project (third_party_include)


# find a boost install with the libraries filesystem and system
# Boost - Name of the library. This is part of used to find the module file FindBoost.cmake
# 1.46.1 - The minimum version of boost to find
# REQUIRED - Tells the module that this is required and to fail if it cannot be found
# COMPONENTS - The list of components to find in the library.

find_package(Boost 1.46.1 REQUIRED COMPONENTS filesystem system)

# check if boost was found
if(Boost_FOUND)
    message ("boost found")
else()
    message (FATAL_ERROR "Cannot find Boost")
endif()

# Add an executable
add_executable(third_party_include main.cpp)

# link against the boost libraries
target_link_libraries( third_party_include
    PRIVATE
        Boost::filesystem
)
```

This will search for CMake modules in the format "FindXXX.cmake" from the list of folders in `CMAKE_MODULE_PATH`. On linux the default search path will include `/usr/share/cmake/Modules`.

一些变量是 package specific, 需要查看FindXXX.cmake

# I compile with clang

```cmake
# Set the minimum version of CMake that can be used
# To find the cmake version run
# $ cmake --version
cmake_minimum_required(VERSION 3.5)

# Set the project name
project (hello_cmake)

# Add an executable
add_executable(hello_cmake main.cpp)
```

- CMAKE_C_COMPILER - The program used to compile c code.
- CMAKE_CXX_COMPILER - The program used to compile c++ code.
- CMAKE_LINKER - The program used to link your binary.

`cmake .. -DCMAKE_C_COMPILER=clang-3.6 -DCMAKE_CXX_COMPILER=clang++-3.6`

```bash
cmake .. -DCMAKE_C_COMPILER=/opt/local/bin/clang -DCMAKE_CXX_COMPILER=/opt/local/bin/clang++
```

# J ninja

`cmake .. -G Ninja`

# K import target

```cmake
cmake_minimum_required(VERSION 3.5)

# Set the project name
project (imported_targets)


# find a boost install with the libraries filesystem and system
find_package(Boost 1.46.1 REQUIRED COMPONENTS filesystem system)

# check if boost was found
if(Boost_FOUND)
    message ("boost found")
else()
    message (FATAL_ERROR "Cannot find Boost")
endif()

# Add an executable
add_executable(imported_targets main.cpp)

# link against the boost libraries
target_link_libraries( imported_targets
    PRIVATE
        Boost::filesystem
)
```

# L cpp standard

```cmake
cmake_minimum_required(VERSION 2.8)

# Set the project name
project (hello_cpp11)

# try conditional compilation
include(CheckCXXCompilerFlag)
# The line include(CheckCXXCompilerFlag) tells CMake to include this function to make it available for use.
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)

# check results and add flag
if(COMPILER_SUPPORTS_CXX11)#
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif(COMPILER_SUPPORTS_CXX0X)#
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
else()
    message(STATUS "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()

# Add an executable
add_executable(hello_cpp11 main.cpp)
```

```cmake
cmake_minimum_required(VERSION 3.1)

# Set the project name
project (hello_cpp11)

# set the C++ standard to C++ 11
set(CMAKE_CXX_STANDARD 11)
# Setting the CMAKE_CXX_STANDARD variable causes the CXX_STANDARD property on all targets. This causes CMake to set the appropriate flag at compille time.

# Add an executable
add_executable(hello_cpp11 main.cpp)
```

```cmake
cmake_minimum_required(VERSION 3.1)

# Set the project name
project (hello_cpp11)

# Add an executable
add_executable(hello_cpp11 main.cpp)

# set the C++ standard to the appropriate standard for using auto
target_compile_features(hello_cpp11 PUBLIC cxx_auto_type)

# Print the list of known compile features for this version of CMake
message("List of compile features: ${CMAKE_CXX_COMPILE_FEATURES}")
```

As with other `target_*` functions, you can specify the scope of the feature for the selected target. This populates the [INTERFACE_COMPILE_FEATURES](https://cmake.org/cmake/help/v3.1/prop_tgt/INTERFACE_COMPILE_FEATURES.html#prop_tgt:INTERFACE_COMPILE_FEATURES) property for the target.

The list of available features can be found from the [CMAKE_CXX_COMPILE_FEATURES](https://cmake.org/cmake/help/v3.1/variable/CMAKE_CXX_COMPILE_FEATURES.html#variable:CMAKE_CXX_COMPILE_FEATURES) variable. You can obtain a list of the available features using the following code:

```cmake
message("List of compile features: ${CMAKE_CXX_COMPILE_FEATURES}")
```

# library

```cmake
cmake_minimum_required (VERSION 3.5)

project(subprojects)

# Add sub directories
add_subdirectory(sublibrary1)
add_subdirectory(sublibrary2)
add_subdirectory(subbinary)

############################# subbinary
project(subbinary)

# Create the executable
add_executable(${PROJECT_NAME} main.cpp)

# Link the static library from subproject1 using its alias sub::lib1
# Link the header only library from subproject2 using its alias sub::lib2
# This will cause the include directories for that target to be added to this project
target_link_libraries(${PROJECT_NAME}
    sub::lib1
    sub::lib2
)



############################# sublibrary1
# Set the project name
project (sublibrary1)

# Add a library with the above sources
add_library(${PROJECT_NAME} src/sublib1.cpp)
add_library(sub::lib1 ALIAS ${PROJECT_NAME})

target_include_directories( ${PROJECT_NAME}
    PUBLIC ${PROJECT_SOURCE_DIR}/include
)



############################# sublibrary2
# Set the project name
project (sublibrary2)

add_library(${PROJECT_NAME} INTERFACE)
add_library(sub::lib2 ALIAS ${PROJECT_NAME})

target_include_directories(${PROJECT_NAME}
    INTERFACE
        ${PROJECT_SOURCE_DIR}/include
)
```

```bash
$ tree
.
├── CMakeLists.txt
├── subbinary
│   ├── CMakeLists.txt
│   └── main.cpp
├── sublibrary1
│   ├── CMakeLists.txt
│   ├── include
│   │   └── sublib1
│   │       └── sublib1.h
│   └── src
│       └── sublib1.cpp
└── sublibrary2
    ├── CMakeLists.txt
    └── include
        └── sublib2
            └── sublib2.h
```

# code generation(protobuf)

During the call to cmake it is possible to create files that use variables from the CMakeLists.txt and cmake cache. During CMake generation the file is copied to a new location and any cmake variables are replaced.

```cmake
cmake_minimum_required(VERSION 3.5)

# Set the project name
project (cf_example)

# set a project version
set (cf_example_VERSION_MAJOR 0)
set (cf_example_VERSION_MINOR 2)
set (cf_example_VERSION_PATCH 1)
set (cf_example_VERSION "${cf_example_VERSION_MAJOR}.${cf_example_VERSION_MINOR}.${cf_example_VERSION_PATCH}")

# Call configure files on ver.h.in to set the version.
# Uses the standard ${VARIABLE} syntax in the file
configure_file(ver.h.in ${PROJECT_BINARY_DIR}/ver.h)

# configure the path.h.in file.
# This file can only use the @VARIABLE@ syntax in the file
configure_file(path.h.in ${PROJECT_BINARY_DIR}/path.h @ONLY)

# Add an executable
add_executable(cf_example
    main.cpp
)

# include the directory with the new files
target_include_directories( cf_example
    PUBLIC
        ${CMAKE_BINARY_DIR}
)
```

```in
#ifndef __PATH_H__
#define __PATH_H__

// version variable that will be substituted by cmake
// This shows an example using the @ variable type
const char* path = "@CMAKE_SOURCE_DIR@";

#endif
```

```cmake
cmake_minimum_required(VERSION 3.5)

# Set the project name
project (protobuf_example)
# 更改位置
set(Protobuf_PROTOC_EXECUTABLE "/usr/local/Cellar/protobuf/21.9_1/bin/protoc")

# find the protobuf compiler and libraries
find_package(Protobuf REQUIRED)

# check if protobuf was found
if(PROTOBUF_FOUND)
    message ("protobuf found")
else()
    message (FATAL_ERROR "Cannot find Protobuf")
endif()

# Generate the .h and .cxx files
PROTOBUF_GENERATE_CPP(PROTO_SRCS PROTO_HDRS AddressBook.proto)

# Print path to generated files
message ("PROTO_SRCS = ${PROTO_SRCS}")
message ("PROTO_HDRS = ${PROTO_HDRS}")

# Add an executable
add_executable(protobuf_example
    main.cpp
    ${PROTO_SRCS}
    ${PROTO_HDRS})

target_include_directories(protobuf_example
    PUBLIC
    ${PROTOBUF_INCLUDE_DIRS}
    ${CMAKE_CURRENT_BINARY_DIR}
)

# link the exe against the libraries
target_link_libraries(protobuf_example
    PUBLIC
    ${PROTOBUF_LIBRARIES}
)
```

```protobuf
package tutorial;

message Person {
  required string name = 1;
  required int32 id = 2;
  optional string email = 3;

  enum PhoneType {
    MOBILE = 0;
    HOME = 1;
    WORK = 2;
  }

  message PhoneNumber {
    required string number = 1;
    optional PhoneType type = 2 [default = HOME];
  }

  repeated PhoneNumber phone = 4;
}

message AddressBook {
  repeated Person person = 1;
}
```

# static check

## clang-analyzer

```cmake
cmake_minimum_required (VERSION 3.5)

project(cppcheck_analysis)

# Use debug build as recommended
set(CMAKE_BUILD_TYPE Debug)

# Have cmake create a compile database
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Add sub directories
add_subdirectory(subproject1)
add_subdirectory(subproject2)
```

```bash
scan-build-3.6 cmake ..
scan-build-3.6 make
```

## clang-format

```cmake
cmake_minimum_required (VERSION 3.5)

project(cppcheck_analysis)

# Add a custom CMake Modules directory
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/modules
                      ${CMAKE_MODULE_PATH})

# Add sub directories
add_subdirectory(subproject1)
add_subdirectory(subproject2)

set(CLANG_FORMAT_BIN_NAME clang-format-3.6)
set(CLANG_FORMAT_EXCLUDE_PATTERNS  "build/" ${CMAKE_BINARY_DIR})
find_package(ClangFormat)
```

# unit test

# package management

## intro

Using your system provided packages is one of the oldest and most common form of package management solutions. For this, you use your systems package installer (e.g. apt, yum) to install libraries and headers into common locations. CMake can then use the `find_package()` function to search for these and make them available to your program.

## vendoring code

```bash
tree .
├── 3rd_party
│   └── catch2
│       ├── catch2
│       │   └── catch.hpp
│       └── CMakeLists.txt
├── CMakeLists.txt
├── src
│   └── example.cpp
```

If these projects support CMake directly, it may be possible to do `add_subdirectory()` on the libraries folder and have that project build and be made available to your code.

If the third party code doesn’t support CMake, you may need to create a "shim" layer on top of the project to allow it to be build and discovered from CMake.

## external project

A simple example of an external project is as follows:

```cmake
include(ExternalProject)
ExternalProject_Add(googletest
  URL    https://github.com/google/googletest/archive/bfc0ffc8a698072c794ae7299db9cb6866f4c0bc.tar.gz_
)
```

Once added you will have a target `googletest` which will attempt to download, build, and install google test when your build your project.

# tree example

```bash
.
├── CMakeLists.txt
├── LICENSE
├── README.md
├── cmake
│   ├── diagon_fuzzer.cmake #.cmake?
│   └── diagon_test.cmake
├── favicon.png
├── snap
│   ├── gui
│   │   ├── diagon.desktop
│   │   └── diagon.png
│   └── snapcraft.yaml
├── src # .hpp?
│   ├── api.cpp
│   ├── api.hpp
│   ├── environment.h.in
│   ├── favicon-32x32.png
│   ├── filesystem.hpp
│   ├── fuzzer.cpp
│   ├── google-analytics.html
│   ├── index.html
│   ├── input_output_test.cpp
│   ├── main.cpp
│   ├── run_diagon.sh
│   ├── screen #target_link_libraries add_library
│   │   ├── CMakeLists.txt
│   │   ├── Screen.cpp
│   │   └── Screen.h
│   ├── style.css
│   ├── translator
│   │   ├── Factory.cpp
│   │   ├── Factory.h
│   │   ├── Translator.cpp
│   │   ├── Translator.h
│   │   ├── antlr_error_listener.cpp
│   │   ├── antlr_error_listener.h
│   │   ├── flowchart
│   │   │   ├── CMakeLists.txt
│   │   │   ├── Flowchart.cpp
│   │   │   └── Flowchart.g4
│   │   ├── frame
│   │   │   ├── CMakeLists.txt
│   │   │   └── Frame.cpp
│   │   ├── grammar
│   │   │   ├── CMakeLists.txt
│   │   │   └── Grammar.cpp
│   │   ├── graph_dag
│   │   │   ├── CMakeLists.txt
│   │   │   ├── GraphDAG.cpp
│   │   │   └── dag_to_graph.cpp
│   │   ├── graph_planar
│   │   │   ├── CMakeLists.txt
│   │   │   ├── GraphPlanar.cpp
│   │   │   ├── GraphPlanar.g4
│   │   │   └── GraphPlanarEmpty.cpp
│   │   ├── math
│   │   │   ├── CMakeLists.txt
│   │   │   ├── Math.cpp
│   │   │   └── Math.g4
│   │   ├── sequence
│   │   │   ├── CMakeLists.txt
│   │   │   ├── Graph.cpp
│   │   │   ├── Graph.hpp
│   │   │   ├── Sequence.cpp
│   │   │   ├── Sequence.g4
│   │   │   └── Sequence.hpp
│   │   ├── table
│   │   │   ├── CMakeLists.txt
│   │   │   └── Table.cpp
│   │   └── tree
│   │       ├── CMakeLists.txt
│   │       └── Tree.cpp
│   └── util.hpp
├── test
│   └── Flowchart
│       ├── example
│       │   ├── input
│       │   └── output
│       └── loong-breakable-string
│           ├── input
│           └── output
└── tools
    ├── CMakeLists.txt
    ├── format.sh
    ├── license_headers.cpp
    └── logo.png

20 directories, 66 files
```
