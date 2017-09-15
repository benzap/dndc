#!/usr/bin/env python

from setuptools import setup


setup(name='dndc',
      version='0.0.1',
      description='Dungeons and Dragons Commandline',
      author='Benjamin Zaporzan',
      author_email='benzaporzan@gmail.com',
      url='https://github.com/benzap/dndc',
      packages=['dndc', 'tests'],
      entry_points={
          'console_scripts': ['dndc = dndc.__main__:main']
      },
      test_suite='nose.collector',
      install_requires=[
          'nose',
          'docopt',
          'funcy',
          'soundex',
          'pyyaml',
          'mypy',
          'pygments',
          'pypiwin32',
          'kivy.deps.sdl2',
          'kivy.deps.glew',
          #'kivy.deps.gstreamer',
          'kivy',
      ],
      tests_require=['nose'],
     )
