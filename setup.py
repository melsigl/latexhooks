from setuptools import find_packages
from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="latexhooks",
    version="0.1.1",
    description="LaTeX related hooks for pre-commit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alihamdan/latexhooks",
    author="Ali Hamdan",
    author_email="ali.hamdan.fr@gmail.com",
    license="GPL-v3",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pylatexindent=latexhooks.latexindent:main",
        ]
    },
)
