# -*- coding: utf-8 -*-

from rapydo.utils import __version__
from rapydo.utils import DEFAULT_FILENAME

from setuptools import setup
# BUG https://stackoverflow.com/a/14220893
# from distutils.core import setup

setup(
    name='rapydo_utils',
    description='A set of python utilities used across all RAPyDo projects',
    version=__version__,
    author="Paolo D'Onorio De Meo",
    author_email='p.donorio.de.meo@gmail.com',
    url='https://github.com/rapydo/utils',
    license='MIT',
    packages=[
        'rapydo.utils'
    ],
    package_data={
        'rapydo.utils': [
            'logging.ini',
            '%s.yaml' % DEFAULT_FILENAME
        ]
    },
    python_requires='>=3.4',
    install_requires=[
        # NOTE: install_requires specify what a project
        # minimally needs to run correctly
        "beeprint",
        "PyYAML",
        "pytz",
    ],
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
    ],
    keywords=['utilities', 'rapydo']
    # download_url='https://github.com/author/repo/tarball/1.0',
)
