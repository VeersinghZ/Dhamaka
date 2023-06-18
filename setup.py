from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'BSODinator'
LONG_DESCRIPTION = "A Python-Module that helps you crash Anyone's PC or Laptop. Note: *This is for don't educational Purposes only. Don't Use it against anyone*"

# Setting up
setup(
    name="BSODinator",
    version=VERSION,
    author="VeersinghZ",
    author_email="codergrand@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['multiprocessing', 'requests', 'numpy', 'webbrowser'],
    keywords=['BSOD', 'Spamming', 'Education', 'Fun', 'VeersinghZ'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
