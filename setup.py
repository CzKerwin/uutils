#-*- coding:utf-8 -*-

import setuptools

#############################################
# File Name: setup.py
# Author: CzKerwin
# Mail: czksnk@woodcol.com
# Created Time:  2020-4-12 18:27:16
#############################################

setuptools.setup(
    name="uutils",
    version="0.0.3",
    author="CzKerwin",
    author_email="czksnk@outlook.com",
    description="uutils",
    long_description="uutils",
    long_description_content_type="text/markdown",
    url="https://github.com/CzKerwin/uutils.git",
    packages=setuptools.find_packages(),
    license = "MIT Licence",
    python_requires='>=3.5',
    include_package_data = True,
    platforms = "any",
    install_requires = [],
)
