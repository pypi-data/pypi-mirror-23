"""Mailmerge build and install configuration."""
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme_file:
    README = readme_file.read()

setup(
    name="mailmerge",
    description="A simple, command line mail merge tool",
    long_description=README,
    version="1.7.3",
    author="Andrew DeOrio",
    author_email="awdeorio@umich.edu",
    url="https://github.com/awdeorio/mailmerge/",
    download_url="https://github.com/awdeorio/mailmerge/tarball/1.7.3",
    license="MIT",
    packages=["mailmerge"],
    keywords=["mail merge", "mailmerge", "email"],
    install_requires=[
        "click",
        "configparser",
        "jinja2",
        "future",
    ],

    # Python command line utilities will be installed in a PATH-accessible bin/
    entry_points={
        'console_scripts': [
            'mailmerge = mailmerge.__main__:cli',
        ]
    },
)
