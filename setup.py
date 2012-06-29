from setuptools import setup
setup(
    name='koji-downloader',
    version='1.0',
    author = "Jiri Moskovcak",
    author_email = "jmoskovc@redhat.com",
    description = ("Simple tool to download the scratch builds from Fedora build system"),
    license = "GPLv2+",
    url = "https://github.com/mozeq/koji-downloder",
    scripts = ['src/koji-downloader'],
    package_dir = {'': 'src'},
    data_files = [('/usr/share/koji-downloader', ['src/scratch_downloader.gtkbuilder']),]
)
