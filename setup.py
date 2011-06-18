# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.9'

setup(name='ltmo',
      version=version,
      description="light weight blogging, heavy weight time-wasting",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Banners, Django',
      author='Inventta',
      author_email='maturburu@gmail.com',
      url='http://ltmo.com.ar',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      package_data={
        'ltmo' : ['templates/*.html'],
      },
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'django'
        'PIL',
        'django-tagging',
        'markdown',
        'pygments',
        'django-pagination',
        'psycopg2',
        'south',
        'django-debug-toolbar',
        'python-markdown-video',
        'markdown-urlize',
        'banners',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
