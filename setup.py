import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "NCTULib-newb1er",
    version = "0.0.1",
    author = "newb1er",
    author_email = "32424677+newb1er@users.noreply.github.com",
    description = "A unofficial python package for NCTU Library"
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/newb1er/NCTULib",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: GPL-3.0",
    ]
)