# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='flat_sales',
    version=version,
    description='Flat sales app for Real Estate Builders',
    author='Deepak',
    author_email='dngupta78@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
