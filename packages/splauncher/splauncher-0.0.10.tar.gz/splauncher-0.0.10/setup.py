from __future__ import print_function


__author__ = "John Kirkham <kirkhamj@janelia.hhmi.org>"
__date__ = "$May 18, 2015 12:09:31 EDT$"


from glob import glob
import os
import shutil
import sys

from setuptools import setup, find_packages

import versioneer


readme = ""
with open("README.rst") as readme_file:
    readme = readme_file.read()

build_requires = []
install_requires = []
tests_require = []
sphinx_build_pdf = False
if len(sys.argv) == 1:
    pass
elif ("--help" in sys.argv) or ("-h" in sys.argv):
    pass
elif sys.argv[1] == "bdist_conda":
    pass
elif sys.argv[1] == "build_sphinx":
    import sphinx.apidoc

    sphinx.apidoc.main([
        sphinx.apidoc.__file__,
        "-f", "-T", "-e", "-M",
        "-o", "docs",
        ".", "setup.py", "tests", "versioneer.py"
    ])

    build_prefix_arg_index = None
    for each_build_arg in ["-b", "--builder"]:
        try:
            build_arg_index = sys.argv.index(each_build_arg)
        except ValueError:
            continue

        if sys.argv[build_arg_index + 1] == "pdf":
            sphinx_build_pdf = True
            sys.argv[build_arg_index + 1] = "latex"
elif sys.argv[1] == "clean":
    saved_rst_files = ["docs/index.rst", "docs/readme.rst", "docs/todo.rst"]

    tmp_rst_files = glob("docs/*.rst")

    print("removing 'docs/*.rst'")
    for each_saved_rst_file in saved_rst_files:
        print("skipping '" + each_saved_rst_file + "'")
        tmp_rst_files.remove(each_saved_rst_file)

    for each_tmp_rst_file in tmp_rst_files:
        os.remove(each_tmp_rst_file)

    if os.path.exists("build/sphinx/doctrees"):
        print("removing 'build/sphinx/doctrees'")
        shutil.rmtree("build/sphinx/doctrees")
    else:
        print("'build/sphinx/doctrees' does not exist -- can't clean it")

    if os.path.exists(".eggs"):
        print("removing '.eggs'")
        shutil.rmtree(".eggs")
    else:
        print("'.eggs' does not exist -- can't clean it")

    if (len(sys.argv) > 2) and (sys.argv[2] in ["-a", "--all"]):
        if os.path.exists("build/sphinx"):
            print("removing 'build/sphinx'")
            shutil.rmtree("build/sphinx")
        else:
            print("'build/sphinx' does not exist -- can't clean it")
elif sys.argv[1] == "develop":
    if (len(sys.argv) > 2) and (sys.argv[2] in ["-u", "--uninstall"]):
        if os.path.exists("splauncher.egg-info"):
            print("removing 'splauncher.egg-info'")
            shutil.rmtree("splauncher.egg-info")
        else:
            print("'splauncher.egg-info' does not exist -- can't clean it")

setup(
    name="splauncher",
    version=versioneer.get_version(),
    description="A simple subprocess launcher with optional DRMAA support.",
    long_description=readme,
    url="https://github.com/jakirkham/splauncher",
    license="BSD 3-Clause",
    author="John Kirkham",
    author_email="kirkhamj@janelia.hhmi.org",
    scripts=glob("bin/*"),
    py_modules=["versioneer"],
    packages=find_packages(exclude=["tests*"]),
    cmdclass=versioneer.get_cmdclass(),
    build_requires=build_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="tests",
    keywords="splauncher",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=True
)
