# -*- coding: utf-8 -*-

# Copyright 2017 Juan José Martín Miralles
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='trackanimation',

    version='1.0.0',

    description='GPS Track Animation Library',
    long_description=long_description,

    url='https://github.com/JoanMartin/trackanimation',

    author='Juan José Martín',
    author_email='',

    license='Apache License, Version 2.0',


    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "License :: OSI Approved :: Apache Software License",

        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Video",

        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],

    keywords='GPS GPX animation map geospatial geopositioning',

    packages=['trackanimation', ],
)