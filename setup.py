# encoding: utf-8
# Created by Jeremy Bowman on Thu Feb 20 16:54:00 EST 2014
# Copyright (c) 2014 Safari Books Online. All rights reserved.
"""
yet-another-django-profiler setup script
"""

import os
from setuptools import setup, find_packages

from yet_another_django_profiler import __version__

version = '.'.join(str(n) for n in __version__)

install_requires = [
    'Django>=1.6.1,<1.7',
]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    install_requires.append('sbo-sphinx==2.0.1')

setup(
    name='yet-another-django-profiler',
    version=version,
    author='Jeremy Bowman',
    author_email='jbowman@safaribooksonline.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Software Development',
    ],
    description='Django middleware for performance profiling directly from the browser',
    url='http://github.com/safarijv/yet-another-django-profiler',
    packages=[
        'yet_another_django_profiler',
    ],
    scripts=['gprof2dot.py'],
    zip_safe=True,
    install_requires=install_requires,
)
