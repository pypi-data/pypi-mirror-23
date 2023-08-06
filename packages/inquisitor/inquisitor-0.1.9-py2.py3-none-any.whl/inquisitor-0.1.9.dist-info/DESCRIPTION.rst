Inquisitor
==========

| This Python module provides a python wrapper around the API of Econdb.com.
| For a successful response, API users must provide an authentication. To obtain an authentication token, users can register at econdb.com.

Installation
------------

Just type:

.. code:: bash

    pip install inquisitor

You can also find `Inquisitor on Github
<https://github.com/inquirim/inquisitor/>`_



Documentation
-------------

The documentation on installation, use and API description is found at econdb.com `documentation page. <https://www.econdb.com/docs/libraries/#python/>`_

Usage example
-------------

.. code:: python

	import inquisitor
	qb = inquisitor.Inquisitor()

	### List sources 
	qb.sources()

	### List datasets
	qb.datasets(source='EU')

	### Obtain series data
	qb.series(dataset='EI_BSCO_M')


