# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.12'

setup(
    name='ltmo',
    version=version,
    description="light weight blogging, heavy weight time-wasting",
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Blog, Django',
    author='Inventta',
    author_email='maturburu@gmail.com',
    url='http://ltmo.com.ar',
    package_data={
        'ltmo' : ['templates/*.html'],
    },
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'manage = ltmo.manage:do_manage',
        ],
    },
    install_requires=[
        'django',
        'Pillow',
        'django-tagging',
        'django-pagination',
        'django-social-auth',
        'django-debug-toolbar',
        'markdown',
        'pygments',
        'south',
        #'psycopg2',
        ],
    )
