from conans import ConanFile, CMake
import os


class SFMLTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "SFML/2.3.2@memsharded/testing"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake . %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        self.copy("*.dll", "bin", "bin")

    def test(self):
        self.run(os.sep.join([".", "bin", "client"]))

