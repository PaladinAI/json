from conans import ConanFile
from conans import tools

class JsonConan(ConanFile):
    name = "json"
    version = "3.2.0"
    description = "JSON for Modern C++."
    url = "https://github.com/nlohmann/json"
    license = "MIT"
    exports_sources = "single_include/nlohmann/*"
    no_copy_source = True

    def package(self):
        self.copy("*.hpp", src="single_include/nlohmann", dst="include/json")

    def package_id(self):
        self.info.header_only()
