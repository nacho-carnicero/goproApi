#!/usr/bin/env python

from setuptools import setup

# auto-convert README.md
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (ImportError, OSError):
    # we'll just use the poorly formatted Markdown file instead
    long_description = open('README.md').read()

setup(
    name='goproApi',
    version='0.0.1',
    description='A python3 API for controlling a GoPro.',
    long_description=long_description,
    url='https://github.com/nacho-carnicero/goproApi',
    author='Nacho Carnicero',
    author_email='ignacio.carnicero@sterblue.com',
    license=open('LICENSE').read(),
    packages=['src'],
    setup_requires=[
        'tox',
        'nose',
        'flake8'
    ],
    install_requires=[
        'Pillow',
        'wireless',
        'colorama',
        'goprohero'
    ],
    zip_safe=False
)
