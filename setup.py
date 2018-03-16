#!/usr/bin/env python
from setuptools import setup

with open('README.rst') as f:
    readme = f.read()
with open('CHANGES.rst') as f:
    changes = f.read()

setup(
    name='microrepl',
    version='0.6',
    description='A REPL client for MicroPython running on the BBC micro:bit.',
    long_description=readme + '\n\n' + changes,
    author='Nicholas H.Tollervey',
    author_email='ntoll@ntoll.org',
    url='http://micropython.org/',
    scripts = ['microrepl.py', ],
    license='apache2',
    install_requires=['pyserial', ],
    package_data={'': ['README.rst', 'CHANGES.rst',
                  'mbedWinSerial_16466.exe']},
    entry_points = {
        'console_scripts': [
            'microrepl = microrepl:main',
            'urepl = microrepl:main',
        ],
    }
)
