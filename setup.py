from setuptools import setup, find_packages


VERSION = '0.1.3'
DESCRIPTION = '## Dhamaka'
LONG_DESCRIPTION = "A Python-Module that helps you crash Anyone's PC or Laptop. Note: *This is for don't educational Purposes only. Don't Use it against anyone*"


# Setting up
setup(
    name="Dhamaka",
    version=VERSION,
    author="VeersinghZ",
    author_email="codergrand@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests', 'numpy', 'cryptography'],
    include_package_data=True,
    keywords=['Danger', 'Spamming', 'Education', 'Fun', 'VeersinghZ'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
