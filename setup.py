from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in iot_erpnext/__init__.py
from iot_erpnext import __version__ as version

setup(
	name="iot_erpnext",
	version=version,
	description="IoT ERPNext",
	author="Pyroject",
	author_email="phuongtung0801@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
