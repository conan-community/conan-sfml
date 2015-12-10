from conans import ConanFile, CMake
from conans import tools
import os


class SFMLConan(ConanFile):
    name = "SFML"
    version = "2.3.2"
    url = "https://github.com/memsharded/conan-sfml.git"
    settings = "os", "compiler", "build_type", "arch"
    options = {"static": [True, False]}
    default_options = "static=True"

    def source(self):
        tools.download("https://github.com/SFML/SFML/archive/2.3.2.zip",
                       "sfml.zip")
        tools.unzip("sfml.zip")
        os.unlink("sfml.zip")

    def build(self):
        cmake = CMake(self.settings)
        static_libs = "-DSFML_USE_STATIC_STD_LIBS=ON" if "MD" not in str(self.settings.compiler.runtime) else ""
        shared = "-DBUILD_SHARED_LIBS=ON" if not self.options.static else "-DBUILD_SHARED_LIBS=OFF"
        self.run('cd SFML-2.3.2 && cmake . %s %s %s -DSFML_BUILD_EXAMPLES=OFF'
                 ' -DSFML_BUILD_DOC=OFF' % (shared, static_libs, cmake.command_line))
        self.run("cd SFML-2.3.2 && cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*", "include", "SFML-2.3.2/include")
        self.copy("*.lib", "lib", "SFML-2.3.2/lib", keep_path=False)
        self.copy("*.a", "lib", "SFML-2.3.2/lib", keep_path=False)
        self.copy("*.dll", "bin", "SFML-2.3.2/lib", keep_path=False)
        if self.options.static:
            arch = "x64" if self.settings.arch == "x86_64" else "x86"
            compiler = "msvc" if self.settings.compiler == "Visual Studio" else "mingw"
            self.copy("*.lib", "lib", "SFML-2.3.2/extlibs/libs-%s/%s" % (compiler, arch), keep_path=False)

    def package_info(self):
        debug = "-d" if self.settings.build_type == "Debug" else ""  
        for lib in ["audio", "graphics", "main", "network", "window", "system"]:
            static = "-s" if self.options.static and lib!="main" else ""
            self.cpp_info.libs.append("sfml-%s%s%s" % (lib, static, debug))
        if self.options.static:
            self.cpp_info.defines.append("SFML_STATIC")
            for lib in ["flac", "freetype", "ogg", "openal32", "vorbis", "vorbisenc", "vorbisfile", "jpeg"]:
                self.cpp_info.libs.append("%s" % (lib))
            self.cpp_info.libs.extend(["winmm", "opengl32", "gdi32", "ws2_32"])
