# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "visier.sdk.api.data-handling"
VERSION = "0.0.3"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Visier Data and Job Handling APIs",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Visier Data and Job Handling APIs"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache License, Version 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    Visier APIs for data and job handling
    """,  # noqa: E501
    package_data={"visier.sdk.api.data_handling": ["py.typed"]},
)
