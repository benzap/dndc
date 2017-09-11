#!/usr/bin/env python

from setuptools import setup


setup(name='dndc',
      version='0.0.1',
      description='Dungeons and Dragons Commandline',
      author='Benjamin Zaporzan',
      author_email='benzaporzan@gmail.com',
      url='https://github.com/benzap/dndc',
      packages=['dndc', 'tests'],
      requires=['docopt'],
      entry_points={
          'console_scripts': ['dndc = dndc.__main__:main']
      },
      test_suite='nose.collector',
      install_requires=['nose'],
      tests_require=['nose'],
     )