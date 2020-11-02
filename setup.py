import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name="pyokra-houdini10",
    verrsion="1.0.1",
    author="Houdini10",
    author_email="nonsoamadi@aol.com",
    description="A Python plugin for the okra API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NonsoAmadi10/Okra.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
