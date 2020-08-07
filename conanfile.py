#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, CMake
import os
from glob import glob


class EigenConan(ConanFile):
    name = "eigen"
    version = "3.3.7.1"
    url = "https://github.com/ulricheck/conan-eigen"
    homepage = "http://eigen.tuxfamily.org"
    description = "Eigen is a C++ template library for linear algebra: matrices, vectors, \
                   numerical solvers, and related algorithms."
    license = "Mozilla Public License Version 2.0"
    no_copy_source = True
    options = {"EIGEN_USE_BLAS": [True, False],
               "EIGEN_USE_LAPACKE": [True, False],
               "EIGEN_USE_LAPACKE_STRICT": [True, False]}
    default_options = "EIGEN_USE_BLAS=False", "EIGEN_USE_LAPACKE=False", "EIGEN_USE_LAPACKE_STRICT=False"

    def source(self):
        git = tools.Git(folder="source_subfolder")
        git.clone("https://gitlab.com/libeigen/eigen.git","master")
        self.run("cd source_subfolder && git checkout 46f8a18567731925e06a7389a6c611e1dc420ea8")


    def build(self):
        #Import common flags and defines
        cmake = CMake(self)
       
        cmake.definitions["EIGEN_TEST_NOQT"] = "ON"
        cmake.definitions["BUILD_TESTING"] = "OFF"
        if not tools.os_info.is_windows:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = "ON"
        cmake.configure(source_folder="source_subfolder", build_folder="build_subfolder")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.includedirs.append('include/eigen3')

        if self.options.EIGEN_USE_BLAS:
            self.cpp_info.defines.append("EIGEN_USE_BLAS")

        if self.options.EIGEN_USE_LAPACKE:
            self.cpp_info.defines.append("EIGEN_USE_LAPACKE")

        if self.options.EIGEN_USE_LAPACKE_STRICT:
            self.cpp_info.defines.append("EIGEN_USE_LAPACKE_STRICT")

    # def package(self):
    #     self.copy("COPYING.*", dst="licenses", src="sources",
    #               ignore_case=True, keep_path=False)
    #     self.copy(pattern="*", dst="include/Eigen", src="sources/Eigen")

    # def package_id(self):
    #     self.info.header_only()

    # def package_info(self):
    #     if self.options.EIGEN_USE_BLAS:
    #         self.cpp_info.defines.append("EIGEN_USE_BLAS")

    #     if self.options.EIGEN_USE_LAPACKE:
    #         self.cpp_info.defines.append("EIGEN_USE_LAPACKE")

    #     if self.options.EIGEN_USE_LAPACKE_STRICT:
    #         self.cpp_info.defines.append("EIGEN_USE_LAPACKE_STRICT")
