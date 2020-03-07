import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rates_pca",
    version="0.0.1",
    author="Mark Higgins",
    description="Illustrate PCA on a simple rates term structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
    ]
)
