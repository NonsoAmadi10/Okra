import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name="okra-py-houdini10",
    verrsion="1.0.0",
    author="Houdini10",
    author_email="nonsoamadi@aol.com",
    description="Integrate the Okra API seamlessly in your python app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NonsoAmadi10/Okra.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language ::Python::3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
