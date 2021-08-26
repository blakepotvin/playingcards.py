import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="playingcards.py",
    version="1.0.0",
    description="An Advanced Python Playing Card Module that makes creating playing card games simple and easy!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Prodxgy/playingcards.py",
    author="Prodxgy",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["playingcards"],
    python_requires=">=3.6.0",
)