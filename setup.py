from setuptools import setup
from os import path


HERE = path.abspath(path.dirname(__file__))


def readme():
    with open(path.join(HERE, "README.rst")) as f:
        return f.read()


setup(
    name="apifootball",
    version="0.1",
    author="Lucas Maystre",
    author_email="lucas@maystre.ch",
    description="Python 3 client for the api-football.com API.",
    long_description=readme(),
    url="https://github.com/kickoffai/apifootball",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="football soccer api api-football client",
    packages=["apifootball"],
    install_requires=[
        "requests",
    ],
    setup_requires=["pytest-runner"],
    tests_require=[
        "pytest",
    ],
    include_package_data=True,
    zip_safe=False,
)
