#!/usr/bin/env python

from setuptools import setup, find_packages

tests_require = [
    'django',
    # also requires the disqus fork of haystack
]

setup(
    name='django-ratings2',
    version=".".join(map(str, __import__('djangoratings2').__version__)),
    author='Paulius Zaleckas',
    author_email='paulius.zaleckas@gmail.com',
    description='Generic Ratings in Django',
    url='http://github.com/pauliuszaleckas/django-ratings2',
    install_requires=[
        'django',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='djangoratings2.runtests.runtests',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
