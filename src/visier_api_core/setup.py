# coding: utf-8

"""
    Visier Authentication APIs

    Visier APIs for authenticating with Visier. To use Visier's public APIs, you must first authenticate yourself as a Visier user who is allowed to use Visier APIs.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "visier-api-core"
VERSION = "0.99201.1508"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "Flask >= 3.0.0",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Visier Authentication APIs",
    author="Visier",
    author_email="alpine@visier.com",
    url="",
    keywords=["Visier", "Visier-SDK", "Visier Authentication APIs"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache License, Version 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    Visier APIs for authenticating with Visier. To use Visier&#39;s public APIs, you must first authenticate yourself as a Visier user who is allowed to use Visier APIs.
    """,  # noqa: E501
    package_data={"visier_api_core": ["py.typed"]},
)
