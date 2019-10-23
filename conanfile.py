import os

from conans import ConanFile, tools


class CrowConan(ConanFile):
    name = "crow"
    version = "master"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Crow here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    no_copy_source = True
    requires = ("boost/1.69.0@conan/stable")
    # No settings/options are necessary, this is header only

    def source(self):
        self.run("git clone --depth=1 --recursive https://github.com/ipkn/crow.git .")

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.hpp", dst="include", src="include")
