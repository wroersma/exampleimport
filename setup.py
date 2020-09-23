"""The pycep python package."""
# coding=utf-8
from setuptools import setup, find_packages
from mypackagename import __version__

setup(
    name="mypackagename",
    version=__version__,
    packages=find_packages(exclude=['docs', 'tests', 'tools', 'utils']),
    url="https://github.com/simspace/pycep/",
    license='Apache 2.0',
    author="Wyatt Roersma",
    author_email="wyatt@simspace.com",
    description="This is the Example package import library",
    include_package_data=True,
    zip_safe=False,
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache 2.0',
                 'Programming Language :: Python :: 3.8'],
    package_data={
        'mypackagename': ['*.txt'],  'mypackagename:example': ['*.*'], 'mypackagename:data': ['*.txt']
    }
    )
