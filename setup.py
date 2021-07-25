import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tabulux",
    version="1.3.0",
    author="NioGreek",
    author_email="GreekNio@gmail.com",
    description="A package to form and retrieve tabular data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/John-pix/Tabulux-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
