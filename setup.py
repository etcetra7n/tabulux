import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tabulux", 
    version="1.0.0",
    author="John",
    author_email="JohnPix005@gmail.com",
    description="A package for creating console tables",
    long_description=long_description,
    long_description_content_type="text",
    url="https://github.com/John-pix/Tabulator-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
