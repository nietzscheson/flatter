from setuptools import setup, find_packages

setup(
    name="flatter",
    version="0.1.0",
    author="Cristian Angulo Nova | @nietzscheson",
    author_email="cristianangulonova@gmail.com",
    description="A Python library to flat list in any dimension",
    long_description="""
    Flatten python list in any dimension
    """,
    long_description_content_type="text/markdown",
    url="https://github.com/nietzscheson/flatter",
    install_requires=[],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
