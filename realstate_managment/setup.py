from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in realstate_managment/__init__.py
from realstate_managment import __version__ as version

setup(
	name="realstate_managment",
	version=version,
	description="this app is realstate managment ",
	author="inceptionSystem",
	author_email="majhar.inception@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
