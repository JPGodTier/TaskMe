from setuptools import setup, find_packages

setup(
    name="TaskMe",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "colorama==0.4.6",
        "coverage==7.3.2",
        "iniconfig==2.0.0",
        "packaging==23.2",
        "pluggy==1.3.0",
        "pytest==7.4.3",
        "pytest-cov == 4.1.0",
        "pytest-mock == 3.12.0"
    ]
)
