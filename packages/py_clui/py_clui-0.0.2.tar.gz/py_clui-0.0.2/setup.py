import codecs

from py_clui import (__author__, __author_email__, __version__)


README = codecs.open('README.md', encoding='UTF-8').read()


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='py_clui',
    version=__version__,
    description='Toolkit for quickly building nice looking command line interfaces',
    long_description=README,
    url='https://github.com/hmleal/py-clui',
    author=__author__,
    author_email=__author_email__,
    packages=[
        'py_clui'
    ],
    classifiers = []
)
