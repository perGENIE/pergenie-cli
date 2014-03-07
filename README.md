[perGENIE](http://pergenie.org) is a Web/CUI application for
**personal genome interpretation**. This repository contains
the core utils of perGENIE, such as `Disease Risk Report`.


## Quick Start (For non-developers)

Without installation, just download this repository and run:

    $ python ./pergenie [command] [options]


## Usage Examples

To run `Disease Risk Report`:

    $ python ./pergenie riskreport -I example/vcf_whole_genome.vcf \
                                   -F vcf_whole_genome \
                                   -P Asian

----

*For developpers*,

## How to Install

If you are familier with Python Package Index
([pip](https://pypi.python.org/pypi/pip)), install via pip:

    $ pip install pergenie

Or clone this repository, then, install by setup script:

    $ python setup.py install


## How to run test

    $ python setup.py test


## How to contribute

Pull requests are welcome! Feel free to contact me :)


## Lisence

GPL version 3 or later


(c) 2012-2014 Kensuke NUMAKURA
