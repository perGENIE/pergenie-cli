`perGENIE <http://pergenie.org/>`_ is a Web/CUI application for
**personal genome interpretation**. This repository contains
the core utils of perGENIE, such as ``Disease Risk Report``.

|travis| |pypi| |pypi_license|

================================
Quick Start (For non-developers)
================================

Without installation, just download this repository and run:

.. code-block:: bash

    $ python ./pergenie [command] [options]

==============
Usage Examples
==============

To run ``Disease Risk Report``:

.. code-block:: bash

    $ python ./pergenie riskreport -I example/vcf_whole_genome.vcf \
                                   -F vcf_whole_genome \
                                   -P Asian

===============
For developpers
===============

--------------
How to Install
--------------

If you are familier with `pip <https://pypi.python.org/pypi/pip>`_:

.. code-block:: bash

    $ pip install pergenie

Or clone this repository, then, install by setup script:

.. code-block:: bash

    $ python setup.py install

---------------
How to run test
---------------

.. code-block:: bash

    $ python setup.py test

=======
License
=======

Copyright (c) 2012,2013,2014,2015 perGENIE Team <knmkr3gma[at]gmail.com>

perGENIE is licensed under the GNU AGPLv3.0.

|agplv3|


.. |agplv3| image:: http://www.gnu.org/graphics/agplv3-88x31.png
   :alt: AGPLv3

.. |pypi| image:: https://img.shields.io/pypi/v/pergenie.svg
   :target: https://pypi.python.org/pypi/pergenie
   :alt: Latest version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/pergenie.svg
   :target: https://pypi.python.org/pypi/pergenie
   :alt: License on PyPI

.. |travis| image:: https://travis-ci.org/perGENIE/pergenie.svg?branch=master
   :target: https://travis-ci.org/perGENIE/pergenie
