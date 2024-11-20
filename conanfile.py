from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class JsonRecipe(ConanFile):
    name = "nlohmann_json"
    version = "3.11.2"
    generators = "CMakeToolchain"
    # Optional metadata
    license = "MIT"
    author = "See https://github.com/nlohmann/json for information"
    url = "https://github.com/nlohmann/json"
    description = "JSON for C++"
    topics = ("json", "c++")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "*"

    def deploy(self):
        copy(self, "*", src=self.package_folder, dst=self.deploy_folder)
    
    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["nlohmann_json"]
