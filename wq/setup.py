from os.path import join, dirname
from setuptools import setup

LONG_DESCRIPTION = """
A modular framework for building custom offline-capable desktop and mobile web apps.
"""

def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(
    name = 'wq',
    version = '0.2.0',
    author='S. Andrew Sheppard',
    author_email='andrew@wq.io',
    url='http://wq.io/',
    license='MIT',
    description='A modular framework for building custom offline-capable desktop and mobile web apps.',
    long_description=long_description(),
    install_requires=['wq.app>=0.3.1', 'wq.io>=0.1.0', 'wq.db>=0.2.0'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
