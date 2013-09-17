from os.path import join, dirname
from setuptools import setup, find_packages

LONG_DESCRIPION = """
Consistent API for reading and writing to external datasets
"""

def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(
    name = 'wq.io',
    version = '0.2.0',
    author='S. Andrew Sheppard',
    author_email='andrew@wq.io',
    url='http://wq.io/wq.io',
    license='MIT',
    packages=find_packages(),
    namespace_packages=['wq'],
    description='Consistent iterable API for reading and writing to external datasets',
    long_description=long_description(),
    install_requires=['httplib2','lxml','xlrd'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]
)
