from setuptools import find_packages, setup

setup(
    name="OptiComp",
    version="0.1.0",
    description="Library to easily compare optimizers on a custom or common objective.",
    long_description=open('README.md').read(),
    author="SJWRD",
    url="https://github.com/OptiComp/OptiComp",
    packages=find_packages(include=['opticomp', 'opticomp.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "tqdm",
    ]
)
