
from setuptools import setup, find_packages

from codecs import open
from os import path

# Get the long description from the README file
#with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#    long_description = f.read()

setup(
    name='jjam',
    version='0.0.1',
    description='The first packaing',
    url='https://github.com/jam31118/test-packaging',
    author='sahn',
    author_email='jam45@naver.com',
    classifiers=[
        'Topic :: Scientific/Engineering :: Physics'
    ],
    keywords='test physics packaging',
    packages=find_packages()

)
