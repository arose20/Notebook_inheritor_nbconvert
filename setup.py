from setuptools import setup, find_packages

setup(
    name="Notebook_inheritor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "nbformat",
        "nbconvert",
        "pandas",
        "numpy",
    ],
)
