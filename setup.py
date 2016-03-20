# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from pip.req import parse_requirements

REQUIREMENTS = parse_requirements('requirements.txt')
with open(os.path.join(os.path.dirname(__file__), 'README.mkd')) as readme:
    README = readme.read()

setup(
    name='ltmo',
    version='0.14',
    description="light weight blogging, heavy weight time-wasting",
    long_description=README,
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Blog, Django',
    author='Inventta',
    author_email='maturburu@gmail.com',
    url='http://ltmo.com.ar',
    packages=find_packages('leaks', 'banners', 'ltmo'),
    package_data={
        'ltmo': ['templates/*.html'],
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'manage = ltmo.manage:do_manage',
        ],
    },
    install_requires=[
        'django',
        'Pillow',
        'markdown',
        'pygments',
        'django-tagging',
        'django-pagination',
        'django-registration',
        'python-social-auth',
        'django-debug-toolbar',
        'markdown',
        'pygments',
        'south',
        #'psycopg2',
    ]
)
