﻿from setuptools import setup, find_packages

setup(
    name='pyNlple',
    packages=find_packages(),
    include_package_data=True,
    version='0.2.3',
    description='NLP procedures in python brought to you by YouScan.',
    author='Paul Khudan',
    author_email='pk@youscan.io',
    company='YouScan Limited',
    url='https://github.com/YouScan/pyNlple',
    install_requires=['requests>=2.9.1',
                      'pandas>=0.19.0',
                      'gensim>=0.13.3',
                      'elasticsearch>=2.0.0,<3.0.0',
                      'nltk>=3.2.0'],

    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='pynlple.tests',

)