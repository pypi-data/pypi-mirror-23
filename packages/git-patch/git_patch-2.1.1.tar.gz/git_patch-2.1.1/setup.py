__author__ = 'rajatv'

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='git_patch',
    version='2.1.1',
    description='Patch management for open source fork projects',

    author='Rajat Venkatesh',
    author_email='rajatvenkatesh@alumni.cmu.edu',

    license='Apache 2.0',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],

    packages=find_packages(),
    install_requires=['pyaml', 'argparse'],

    entry_points={
        'console_scripts': [
            'git-patch=git_patch.git_patch:main',
        ],
    },
)
