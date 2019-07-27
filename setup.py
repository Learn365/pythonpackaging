import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-wangbaikang",
    version="0.0.1",
    author="wangbaikang",
    author_email="baikangwang@hotmail.com",
    description="A small example pacakge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Learn365/pythonpackaging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
