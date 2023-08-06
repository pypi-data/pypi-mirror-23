Maya Test
=========

|Build Status| |Coverage Status| |Scrutinizer Code Quality| |PyPI
version| |License: MIT|

Wrapper to easily test maya scripts and modules with the powerful pytest
framework.

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

You'll need to install: \* Autodesk Maya (2014+) \* Python (2.7+)

Installing
~~~~~~~~~~

.. code:: bash

    pip install mayatest

Usage
~~~~~

Run mayatest in the folder of the script or module.

.. code:: bash

    # To invoke pytest using mayapy from Maya 2017 do:
    mayatest -m 2017

    # Then the normal usage for pytest applies, e.g. to test specific  file:
    mayatest -m 2017 --pytest="test_sometest.py"
    # to only run test_func
    mayatest -m 2017 --pytest="test_sometest.py::test_func"

For more information using pytest go to their
`docs <https://docs.pytest.org/en/latest/usage.html>`__.

License
-------

This project is licensed under the MIT License - see the
`LICENSE.md <LICENSE.md>`__ file for details

.. |Build Status| image:: https://travis-ci.org/arubertoson/mayatest.svg?branch=master
   :target: https://travis-ci.org/arubertoson/mayatest
.. |Coverage Status| image:: https://coveralls.io/repos/github/arubertoson/mayatest/badge.svg?branch=master
   :target: https://coveralls.io/github/arubertoson/mayatest?branch=master
.. |Scrutinizer Code Quality| image:: https://scrutinizer-ci.com/g/arubertoson/mayatest/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/arubertoson/mayatest/?branch=master
.. |PyPI version| image:: https://badge.fury.io/py/mayatest.svg
   :target: https://badge.fury.io/py/mayatest
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT


