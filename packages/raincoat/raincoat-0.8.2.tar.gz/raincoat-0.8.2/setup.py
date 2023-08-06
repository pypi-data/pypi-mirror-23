#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

version = '0.8.2'

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='raincoat',
    version=version,
    description="Raincoat has your code covered when you can't stay DRY.",
    long_description=readme + '\n\n' + history,
    author='Joachim Jablon',
    author_email='joachim.jablon@people-doc.com',
    url='https://github.com/novafloss/raincoat',
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["sh", "requests", "pip", "click", "colorama"],
    tests_require=["tox"],
    license="MIT",
    zip_safe=False,
    entry_points={
        'console_scripts': ['raincoat=raincoat:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
