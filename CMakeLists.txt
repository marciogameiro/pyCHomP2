cmake_minimum_required(VERSION 3.15...3.26)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

# cmake_policy(SET CMP0054 NEW)

# Visual Studio C++ does not support keywords such
# as "and", "not", etc. Settting the /permissive-
# flag for the compiler makes it suppor them.
if(MSVC)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /permissive-")
endif()

set(PYBIND11_FINDPYTHON ON)

find_package(pybind11 CONFIG REQUIRED)

# With the settings above pybind11 will find Python
# find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

# CMAKE_PROJECT_PATH is set in pyproject.toml
include_directories(${CMAKE_SOURCE_DIR}/${CMAKE_PROJECT_PATH}/include)
# include_directories(${CMAKE_SOURCE_DIR}/src/pychomp/_chomp/include)

pybind11_add_module(_chomp MODULE ${CMAKE_PROJECT_PATH}/chomp.cpp)
# pybind11_add_module(_chomp MODULE src/pychomp/_chomp/chomp.cpp)

# Delete this
# python_add_library(_chomp MODULE src/pychomp/_chomp/chomp.cpp WITH_SOABI)
# target_link_libraries(_chomp PRIVATE pybind11::headers)

message("USER PROJECT PATH IS ${CMAKE_PROJECT_PATH}")
message("CMAKE SOURCE DIR IS ${CMAKE_SOURCE_DIR}")
message("SKBUILD PROJECT NAME IS ${SKBUILD_PROJECT_NAME}")

install(TARGETS _chomp DESTINATION pychomp)
# install(TARGETS _chomp DESTINATION ${SKBUILD_PROJECT_NAME})
