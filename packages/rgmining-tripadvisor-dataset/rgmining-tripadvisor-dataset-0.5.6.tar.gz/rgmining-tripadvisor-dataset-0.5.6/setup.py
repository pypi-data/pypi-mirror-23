#
# setup.py
#
# Copyright (c) 2017 Junpei Kawamoto
#
# This file is part of rgmining-tripadvisor-dataset.
#
# rgmining-tripadvisor-dataset is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rgmining-tripadvisor-dataset is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
# pylint: disable=invalid-name
"""Package information about a synthetic dataset for review graph mining.
"""
import distutils.command.install_data
from os import path
import site
import sys
import urllib
from setuptools import setup


def read(fname):
    """Read a file.
    """
    return open(path.join(path.dirname(__file__), fname)).read()


class CustomInstallData(distutils.command.install_data.install_data):
    """Custom install data command to download data files from the web.
    """

    def run(self):
        """Before executing run command, download data files.
        """
        for f in self.data_files:
            if not isinstance(f, tuple):
                continue
            for i, u in enumerate(f[1]):
                base = path.basename(u)
                f[1][i] = path.join(sys.prefix, f[0], base)
                if not path.exists(f[1][i]):
                    f[1][i] = path.join(sys.prefix, "local", f[0], base)
                if not path.exists(f[1][i]):
                    f[1][i] = path.join(site.getuserbase(), f[0], base)
                if not path.exists(f[1][i]):
                    f[1][i] = urllib.urlretrieve(u, base)[0]
        return distutils.command.install_data.install_data.run(self)


def load_requires_from_file(filepath):
    """Read a package list from a given file path.

    Args:
      filepath: file path of the package list.

    Returns:
      a list of package names.
    """
    with open(filepath) as fp:
        return [pkg_name.strip() for pkg_name in fp.readlines()]


setup(
    name="rgmining-tripadvisor-dataset",
    use_scm_version=True,
    author="Junpei Kawamoto",
    author_email="kawamoto.junpei@gmail.com",
    description="Trip Advisor dataset for Review Graph Mining Project",
    long_description=read("README.rst"),
    url="https://github.com/rgmining/tripadvisor",
    py_modules=[
        "tripadvisor"
    ],
    install_requires=load_requires_from_file("requirements.txt"),
    setup_requires=[
        "setuptools_scm"
    ],
    data_files=[(
        "rgmining/data",
        ["http://times.cs.uiuc.edu/~wang296/Data/LARA/TripAdvisor/TripAdvisorJson.tar.bz2"]
    )],
    test_suite="tests.suite",
    license="GPLv3",
    cmdclass={
        "install_data": CustomInstallData
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ]
)
