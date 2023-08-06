#!/usr/bin/env python2
# -*- coding:utf-8 -*-

'''
For pypi
'''

from setuptools import setup, find_packages

desc = ('TorCMS apps.')
setup(
    name='torcms_app',
    version='0.0.2',
    keywords=('torcms', 'tornado'),
    description=desc,
    long_description=''.join(open('README.rst').readlines()),
    license='MIT License',

    url='https://www.yunsuan.org',
    author='bukun',
    author_email='bukun@osgeo.cn',

    packages=find_packages(exclude=['torcms', 'script', 'lib', 'foo_run']),

    platforms='any',
    zip_safe=True,
    # install_requires=[''],

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
