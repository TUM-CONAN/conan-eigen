# conan-eigen

![conan-eigen image](/images/conan-eigen.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/eigen%3Aconan/images/download.svg?version=3.3.4%3Astable)](https://bintray.com/conan-community/conan/eigen%3Aconan/3.3.4%3Astable/link)
[![Build Status](https://travis-ci.org/danimtb/conan-eigen.svg?branch=stable%2F3.3.4)](https://travis-ci.org/danimtb/conan-eigen)
[![Build status](https://ci.appveyor.com/api/projects/status/jyeh443gn0l0f3bi/branch/stable/3.3.4?svg=true)](https://ci.appveyor.com/project/danimtb/conan-eigen/branch/stable/3.3.4)

[Conan.io](https://conan.io) package for [Eigen](https://bitbucket.org/eigen/eigen) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/eigen%3Aconan).

## For Users: Use this package

### Basic setup

    $ conan install eigen/3.3.4@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    eigen/3.3.4@conan/stable

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

**Note:** It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to `conan-community` conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from `build_requires` and `requires` , and then running the `build()` method.

    $ conan create conan/stable

## Add Remote

    $ conan remote add conan-community "https://api.bintray.com/conan/conan-community/conan"

## Upload

    $ conan upload eigen/3.3.4@conan/stable --all -r conan-community

## License

[MIT License](LICENSE)
