from distutils.core import setup
import sys

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of ArbitrageSpotter requires Python {}.{}, but you're trying to
install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install ArbitrageSpotter
This will install the latest version of Django which works on your
version of Python. If you can't upgrade your pip (or Python), request
an older version of ArbitrageSpotter.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

setup(name="ArbitrageSpotter",
    version="0.1dev",
    description="Script to find arbitrage oppotunities across exchanges",
    author="Joel Jaeschke",
    author_email="joel.jaeschke@gmail.com",
    packages=["Source"],
    requires=["json", "requests"],
    long_description=open("README.txt").read()
    )