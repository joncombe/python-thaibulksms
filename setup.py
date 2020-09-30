# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='python-thaibulksms',
    version='0.0.1',
    author=u'Jon Combe',
    author_email='jon@salebox.io',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    url='https://github.com/joncombe/python-thaibulksms',
    license='BSD licence, see LICENCE file',
    description='Python functions to send SMSs via ThaiBulkSMS.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
