from setuptools import setup

import sys
if sys.version_info < (3,3):
    sys.exit("Sorry, Python 3.3 or greater is required")

setup(
  name='mpy-utils',
  version='0.1.6',
  description='MicroPython development utility programs',
  url='http://github.com/nickzoic/mpy-utils/',
  author='Nick Moore',
  author_email='nick@zoic.org',
  license="MIT",
  packages=["mpy_utils"],
  scripts=[
    "bin/mpy-fuse",
    "bin/mpy-upload",
    "bin/mpy-sync",
    "bin/mpy-watch",
  ],
  install_requires=[
    'fusepy>=2',
    'pyserial>=3',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Software Development :: Embedded Systems',
  ],
)
