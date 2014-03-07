from setuptools import setup, find_packages
import os

VERSION = '0.1.0'
LONG_DESCRIPTION = os.linesep.join([open('README').read(),
                                    open('CHANGELOG').read()])

setup(
    name='pergenie',
    version=VERSION,

    author='Kensuke NUMAKURA',
    author_email='numakura@sb.ecei.tohoku.ac.jp',

    description='`perGENIE` is ....',
    long_description=LONG_DESCRIPTION,
    url='https://bitbucket.org/knmkr/...',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        # "License :: OSI Approved :: **** License",
        "Natural Language :: English",
        # "Natural Language :: Japanese",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords=['bioinformatics', 'personal genome', 'GWAS'],
    license='',

    packages=find_packages(),
    package_data={'pergenie': ['example/*',
                               'data/*',
                               'test/test_*',
                               'test/testcase_*/*']},
    entry_points={'console_scripts': ['pergenie = pergenie:main']},
    test_suite='test.test_all'
)
