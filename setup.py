from setuptools import setup

setup(
    name="crowd_counting",
    version="1.0",
    license="GPL",
    packages=['crowd_counting'],
    package_dir={'crowd_counting': 'src'},
    install_requires=[
        'torch',
        'torchvision',
        'h5py',
    ]
)