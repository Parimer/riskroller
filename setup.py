from setuptools import setup, find_packages
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('risk/risk.py').read(),
    re.M
    ).group(1)

setup(
    name='riskroller',
    author='James Campbell',
    author_email='james@jamescampbell.us',
    version=version,
    license='GPLv3',
    description = 'Play one random or inputed initial conditions of a round of Risk.',
    packages=['riskroller'],
    py_modules=['riskroller'],
    keywords = ['risk', 'data-analysis', 'dice', 'statistics', 'die-roll'],
    classifiers = ["Programming Language :: Python :: 3 :: Only"],
    install_requires=[
        'argparse',
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'risk = risk.risk:main',
        ],
        },
    url = 'https://github.com/Parimer/riskroller',
    download_url = 'https://github.com/Parimer/riskroller/archive/{}.tar.gz'.format(version)
)