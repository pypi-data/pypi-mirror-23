#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="portinus",
    version="0.9.16",
    author="Justin Dray",
    author_email="justin@dray.be",
    url="https://github.com/justin8/portinus",
    description="This utility creates a systemd service file for a docker-compose file",
    packages=find_packages(),
    package_data={'portinus': ['templates/*']},
    license="MIT",
    install_requires=[
        "click",
        "docker",
        "jinja2"
    ],
    tests_require=["nose",
        "coverage",
        "mock",
    ],
    test_suite="nose.collector",
    entry_points={
        "console_scripts": [
            "portinus=portinus.cli:task",
            "portinus-monitor=portinus.monitor.cli:task",
        ]
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
    ],
)
