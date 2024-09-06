# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1456
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
NAME = "visier-api-data-out"
VERSION = "0.0.302"
PYTHON_REQUIRES = ">=3.8"
REQUIRES = [
    "visier-api-core ~= 0.0.302",
]

setup(
    name=NAME,
    version=VERSION,
    description="Visier Data Out APIs",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Visier Data Out APIs"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache License, Version 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    Visier APIs for getting data out of Visier, such as aggregate data and data version information.
    """,  # noqa: E501
    package_data={"visier_api_data_out": ["py.typed"]},
)
