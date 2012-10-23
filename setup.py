""" Client library for interacting with Gerrit.

The MIT License

Copyright 2012 Sony Mobile Communications. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from setuptools import setup

setup(
    name="pygerrit",
    description="Client library for interacting with Gerrit",
    version="0.0.4",
    license="The MIT License",
    author="David Pursehouse",
    author_email="david.pursehouse@sonymobile.com",
    maintainer="David Pursehouse",
    maintainer_email="david.pursehouse@sonymobile.com",
    url="http://sonymobile.com",
    packages=['pygerrit'],
    keywords='gerrit, json',
    install_requires=['paramiko'],
)