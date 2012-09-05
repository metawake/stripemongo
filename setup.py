import os
from setuptools import setup

setup(
    name='StripeMongo',
    version='0.5.0',
    author='Alex Alexapolsky',
    author_email='newsforfun@gmail.com',
    packages=['stripemongo'],
    url='http://pypi.python.org/pypi/StripeMongo/',
    license='LICENSE.txt',
    description='MongoDB storage for incoming Stripe data in Django.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django",
        "pymongo",
    ],
)