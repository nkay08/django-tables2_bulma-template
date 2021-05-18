import os
import sys

from setuptools import find_packages, setup

import django_tables2_bulma_template

if sys.argv[-1] == "publish":
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a {} -m 'version {}'".format(django_tables2_bulma_template.__version__,
                                                   django_tables2_bulma_template.__version__))
    print("  git push --tags")
    sys.exit()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="django-tables2_bulma-template",
    version=django_tables2_bulma_template.__version__,
    description="A bulma template for django-tables2",
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["tables", "django", "bulma"],
    author="NKay",
    author_email="py@nkay.info",
    url="https://github.com/nkay08/django-tables2_bulma-template",
    license="MIT",
    packages=find_packages(exclude=["docs"]),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=requirements,
    zip_safe=False,
)