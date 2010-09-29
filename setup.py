#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ltmo',
    version='0.11',
    author=u'Matías Iturburu, Francisco Herrero',
    author_email='maturburu@gmail.com, francisco.herrero@gmail.com',
    url='http://github.com/tutuca/ltmo',
    description = 'Un sitio para los amigos',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PIL',
        'markdown',
        'psycopg2',
        'django',
        'django-tagging',
        'django-pagination'
    ]


)
