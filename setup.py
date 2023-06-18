from setuptools import find_packages, setup


setup(
    name="firebase-tools",
    version="0.0.1",
    author="Mathias Gout",
    packages=find_packages(exclude=["tests"]),
    install_requires=["firebase-admin==6.1.0"],
    python_requires="==3.9.*",
)
