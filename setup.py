from setuptools import setup, find_packages
import os

VERSION = '0.1.4'
LONG_DESCRIPTION = os.linesep.join([open('README.rst').read(),
                                    open('CHANGELOG.rst').read()])

setup(
    name='pergenie',
    version=VERSION,

    author='Kensuke Numakura',
    author_email='knmkr3gma+pip@gmail.com',

    description='perGENIE is a Web/CUI application for personal genome interpretation.',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/perGENIE/pergenie-cli',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Natural Language :: Japanese",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords=['bioinformatics', 'personal genome'],
    license='GNU AGPLv3',

    packages=find_packages(),
    package_data={'pergenie': ['example/*',
                               'data/*',
                               'test/test_*',
                               'test/testcase_*/*']},
    entry_points={'console_scripts': ['pergenie = pergenie:main']},
    test_suite='test.test_all'
)
