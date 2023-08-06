# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2017 Tijme Gommers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import find_packages, setup
from shutil import copyfile

copyfile(".semver", "detective/.semver")

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

with open("README.rst") as file:
    readme = file.read().replace(".svg?pypi=png.from.svg", ".png")

with open(".semver") as file:
    semver = file.read()

setup(
    version=semver,
    name="detective",
    description="A private detective that gathers information you're not supposed to know about",
    long_description=readme,
    keywords = ["vulnerability", "bug-bounty", "security", "information-disclosure", "sensitive-data-exposure", "scanner"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security"
    ],
    packages=find_packages(),
    package_data={
        "detective": [
            ".semver"
        ]
    },
    platforms=["any"],
    author="Tijme Gommers",
    author_email="tijme@finnwea.com",
    license="MIT",
    url="https://github.com/tijme/detective",
    install_requires=requirements
)