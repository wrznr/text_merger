# -*- coding: utf-8 -*-
import codecs

from setuptools import setup, find_packages

setup(
    name='text_merger',
    version='0.0.1',
    description='Text merger',
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    author='Kay-Michael Würzner',
    author_email='wuerzner@gmail.com',
    url='https://github.com/wrznr/text_merger',
    license='MIT License',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=open('requirements.txt').read().split('\n'),
    package_data={
        '': ['*.json', '*.yml', '*.yaml'],
    },
    entry_points={
        'console_scripts': [
            'text_merger=text_merger.scripts.text_merger:cli',
        ]
    },
)
