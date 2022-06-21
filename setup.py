# -*- coding: utf-8 -*-
# @Author: Mehaei
# @Date:   2022-06-14 11:49:05
# @Last Modified by:   Mehaei
# @Last Modified time: 2022-06-21 11:50:33
from distutils.core import setup
from setuptools import find_packages


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name='local_fake_useragent',
    version='2.0.1',
    description='Random request headers for local versions of browsers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mehaei',
    author_email='pymehaei@gmail.com',
    url='https://github.com/Mehaei/local_ua',
    install_requires=[],
    license='Apache License 2.0',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    platforms=["all"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ]
)