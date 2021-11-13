from setuptools import setup, find_packages

setup(
    name="crowd_counting",
    version="1.0",
    license="GPL",
    packages=find_packages(include=['./*', 'images.*']),
    install_requires=[
        'torch',
        'torchvision',
        'h5py',
    ]
)