from setuptools import setup, find_packages

setup(
    name="TaskMe",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'colorama==0.4.6',
        'pytest==7.4.3',
        'pytest-cov==4.1.0'
    ]
)
