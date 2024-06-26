from setuptools import find_packages, setup

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="OptiComp",
    version="0.2.0",
    description="Easily compare/benchmark optimizers on a custom or common objective.",
    long_description=description,
    long_description_content_type="text/markdown",
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
        "matplotlib",
        "psutil",
    ]
)
