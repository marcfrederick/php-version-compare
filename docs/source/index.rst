php-version-compare
===================

A simple Python library for comparing "PHP-style" version strings using the 
rules of PHP's `version_compare <https://www.php.net/manual/en/function.version-compare.php>`_ function.

Installation
------------

To install the latest release of the library from PyPI, run:

.. code-block:: bash

   pip install php-version-compare

Alternatively, to install the latest development version directly from the Git
repository:

.. code-block:: bash

   pip install git+https://github.com/marcfrederick/php-version-compare

API Reference
-------------

This section contains automatically generated reference documentation from the
project's docstrings.

.. automodule:: php_version_compare
   :members:
   :imported-members:
   :undoc-members:

Versioning
----------

This project follows `Semantic Versioning <https://semver.org/>`_. You can find
all available versions on the 
`releases page <pip install git+https://github.com/marcfrederick/php-version-compare/releases>`_.

To check the installed version programmatically:

.. code-block:: python

   import php_version_compare
   print(php_version_compare.__version__)

License
-------

This project is licensed under either of the following, at your option:

- Apache License, Version 2.0, (LICENSE-APACHE or https://www.apache.org/licenses/LICENSE-2.0)
- MIT License (LICENSE-MIT or https://opensource.org/licenses/MIT)

Contributions are welcome under the same terms.

Contributing
------------

When contributing, you agree to license your contributions under both the
Apache and MIT licenses.
