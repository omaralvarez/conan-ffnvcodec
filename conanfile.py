from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools

class ffnvcodecConan(ConanFile):
    name = "ffnvcodec"
    version = "9.0.18.1"
    description = "nv-codec-headers for ffmpeg https://github.com/FFmpeg/nv-codec-headers"
    url = "https://github.com/omaralvarez/conan-ffnvcodec"
    repo_url = "https://github.com/FFmpeg/nv-codec-headers"
    topics = ("c", "header-only")
    generators = "cmake"

    def source(self):
        self.run("git clone -b 'n%s' --single-branch --depth 1 %s" % (self.version, self.repo_url))
    
    def build(self):
        with tools.chdir("nv-codec-headers"):
            autotools = AutoToolsBuildEnvironment(self)
            #autotools.configure()
            print(self.package_folder)
            self.run('sed -e s#/usr/local#%s#g Makefile > Makefile.tmp' % self.package_folder)
            self.run('mv Makefile.tmp Makefile')
            autotools.make()
            autotools.install()
    
    # def package(self):
    #     self.copy("*.h", dst="include", keep_path=False)

    def package_id(self):
        self.info.header_only()
