# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import os
import re

from setuptools import setup, find_packages


# Convert description from markdown to reStructuredText
try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst', 'markdown')
except (OSError, ImportError):
    description = ''


# Get package version number
# Source: https://packaging.python.org/single_source_version/
def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='do-audit',
    url='https://github.com/omni-digital/do-audit',
    download_url='https://github.com/omni-digital/do-audit/releases/latest',
    bugtrack_url='https://github.com/omni-digital/do-audit/issues',
    version=find_version('do_audit', '__init__.py'),
    license='MIT License',
    author='Omni Digital',
    author_email='developers@omni-digital.co.uk',
    maintainer='Omni Digital',
    maintainer_email='developers@omni-digital.co.uk',
    description="Audit your Digital Ocean account and make sure you know what's up",
    long_description=description,
    packages=find_packages(),
    include_package_data=True,
    scripts=['bin/do-audit'],
    install_requires=[
        'click>=6.7',
        'dnspython>=1.15.0',
        'python-dateutil>=2.6.0',
        'python-digitalocean>=1.11',
        'requests>=2.18.1',
        'six>=1.10.0',
        'tablib>=0.11.5',
    ],
    extras_require={
        'testing': [
            'pytest',
            'pytest-mock',
        ],
    },
    keywords='digital ocean audit do cli',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
