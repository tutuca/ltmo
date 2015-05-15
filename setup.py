#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
from pip.req import parse_requirements


requirements = parse_requirements('requirements.txt')

setup(
    name='ltmo',
    version='0.14',
    description="light weight blogging, heavy weight time-wasting",
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Blog, Django',
    author='Matias Iturburu, Fran Herrero',
    author_email='maturburu@gmail.com',
    url='http://ltmo.com.ar',
    packages=['ltmo', 'leaks'],
    package_data={
        'ltmo': ['templates/*.html', 'static/*.*'],
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'manage = ltmo.manage:do_manage',
        ],
    },
    install_requires=[str(r.req) for r in requirements]
)
