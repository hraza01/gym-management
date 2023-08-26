from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gym_membership/__init__.py
from gym_membership import __version__ as version

setup(
    name="gym_membership",
    version=version,
    description="A basic application to manage gym membership",
    author="Hasan Raza",
    author_email="razahasan24@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
