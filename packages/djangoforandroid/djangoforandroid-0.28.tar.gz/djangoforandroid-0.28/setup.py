import os
from setuptools import setup, find_packages

#with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'djangoforandroid',
    version = '0.28',
    packages = find_packages(),

    author = 'Yeison Cardona',
    author_email = 'yeisoneng@gmail.com',
    maintainer = 'Yeison Cardona',
    maintainer_email = 'yeisoneng@gmail.com',

    #url = 'http://www.pinguino.cc/',
    url = 'http://yeisoncardona.com/',
    download_url = 'https://bitbucket.org/djangoforandroid/django-for-android/downloads',

    install_requires = ['python-for-android', 'django'],

    include_package_data = True,
    license = 'BSD License',
    description = "Deploy Django web application on Android as APK.",
#    long_description = README,

    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
