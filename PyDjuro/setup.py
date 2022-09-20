import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arithmetic-mngugi", # Replace with your own username
    version="0.0.1",
    author="Peter Mwangi Ngugi",
    author_email="mngugi7@gmail.com",
    description="A basic learning package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mngugi/Python-Level-One-O-One",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
