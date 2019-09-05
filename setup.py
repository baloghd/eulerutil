import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eulerutil",
    version="0.1",
    author="Domonkos BALOGH",
    author_email="balogh.domonkos@gmail.com",
    description="Utility package for solving Project Euler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/baloghd/eulerutil",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)