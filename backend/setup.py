from setuptools import setup, find_packages

setup(
    name='movie-picture-pipeline',    # Your project name
    version='0.1.0',                  # Version number
    packages=find_packages(where=''),  # Discover packages in src
    package_dir={'': ''},
    install_requires=[                 # List of dependencies
    ],
)