from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_spanish_accounting/__init__.py
from erpnext_spanish_accounting import __version__ as version

setup(
	name="erpnext_spanish_accounting",
	version=version,
	description="Regional localisation to meet spanish accounting requirements",
	author="TORRMAN",
	author_email="info@torrman.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
