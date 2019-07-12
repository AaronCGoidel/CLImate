import setuptools

with open("README.md", "r") as readme:
    ld = readme.read()

setuptools.setup(
    name="CLImate",
    version="0.0.2",
    author="Aaron Goidel",
    author_email="acgoidel@gmail.com",
    description="A set of tools for organizing CLI I/O",
    long_description=ld,
    long_description_content_type="text/markdown",
    url="https://github.com/AaronCGoidel/CLImate/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
    ],
)
