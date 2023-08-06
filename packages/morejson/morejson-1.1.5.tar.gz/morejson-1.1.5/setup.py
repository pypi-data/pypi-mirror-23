"""Setup for the morejson package."""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import versioneer

README_RST = ''
with open('README.rst') as f:
    README_RST = f.read()

setup(
    name='morejson',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Wraps Python json, supporting more Python built-in types.",
    long_description=README_RST,
    license='MIT',
    author="Shay Palachy",
    author_email="shay.palachy@gmail.com",
    url='https://github.com/shaypal5/morejson',
    packages=['morejson'],
    install_requires=[],
    setup_requires=[],
    tests_require=['nose', 'coverage', 'pytz', 'tzlocal'],
    test_suite='nose.collector',
    platforms=['any'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Other/Nonlisted Topic',
        'Intended Audience :: Developers',
    ],
    keywords='json datetime timedelta timezone frozenset',
)
