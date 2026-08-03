from setuptools import find_packages
from setuptools import setup

setup(
    name='depth_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('depth_interfaces', 'depth_interfaces.*')),
)
