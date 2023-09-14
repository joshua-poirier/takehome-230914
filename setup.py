from setuptools import find_packages
from setuptools import setup

# description/readme
with open("README.md") as f:
    description = f.read()

setup(
    name="takehome-230914",
    version="0.1",
    author="Joshua Poirier",
    packages=find_packages(),
    license="MIT License",
    long_description=description,
    include_package_data=True,
)
