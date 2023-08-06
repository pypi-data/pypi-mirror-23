"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import setuptools   # Always prefer setuptools over distutils
import codecs       # To use a consistent encoding
import os
import sys
import pip.utils


__version__ = "1.0-alpha2"
__version__ = str(pip.utils.packaging.version.Version(__version__))  # normalize the version number

__install_requires__ = [
    "argparse",
    "pathspec"
]


#
# Add "publish" for convenience
# Use `python setup.py publish` to publish to PyPI
#
if sys.argv[-1] == "publish":
    dirPath = os.path.dirname(__file__)
    if dirPath != "":
        os.chdir(dirPath)
    os.system("python %s sdist" % os.path.basename(__file__))
    os.system("twine upload dist/statedump-%s.tar.gz" % __version__)
    sys.exit()



setuptools.setup(

    name = "statedump",

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version = __version__,

    description = "A Python package helping to dump and restore posix state (user/group/permissions) of files.",

    # Get the long description from the README file
    long_description = codecs.open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "README"),
        encoding = "utf-8").read(),

    # The project's main homepage.
    url = "https://github.com/WenbinHou/statedump",

    # Author details
    author = "Wenbin Hou",
    author_email="catchyrime@fastmail.com",

    # Choose your license
    license = "GPLv3",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [

        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #   6 - Mature
        #   7 - Inactive
        "Development Status :: 2 - Pre-Alpha",

        # Indicate who your project is intended for
        "Intended Audience :: System Administrators",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Recovery Tools",
        "Topic :: Utilities",

        # The language
        "Natural Language :: English",

        # Supporting operating systems
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],

    # What does your project relate to?
    keywords = "posix file state permission",

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages = ["statedump"],

    # Alternatively, if you want to distribute just a my_module.py, uncomment this:
    #
    #py_modules = ["my_module"],

    # List run-time dependencies here.
    # These will be installed by pip when your project is installed.
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires = __install_requires__,

    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #
    #extras_require = {
    #    "dev": ["check-manifest"],
    #    "test": ["coverage"],
    #},

    # If there are data files included in your packages that need to be installed, specify them here.
    # If using Python 2.6 or less, then these have to be included in MANIFEST.in as well.
    #
    #package_data = {
    #    "sample": ["package_data.dat"],
    #},

    # Although "package_data" is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    #
    # In this case, "data_file" will be installed into "<sys.prefix>/my_data"
    #data_files = [("my_data", ["data/data_file"])],

    # To provide executable scripts, use entry points in preference to the "scripts" keyword.
    # Entry points provide cross-platform support and allow pip to create the appropriate
    # form of executable for the target platform.
    entry_points = {
        "console_scripts": [
            "statedump = statedump.StateDump:main",
        ],
    },
)
