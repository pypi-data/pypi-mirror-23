naposapi
========

**Use at your own risk**

A simple API to lookup drugs on the database for acute porphyria (developed by NAPOS).

Usage
-----

::

    >>> import naposapi
    >>> naposapi.lookup_classification('B01AA03')
    ClassificationResult(code='PNP', level=1, name='Probably not porphyrinogenic', description='Used as a first hand choice. No precautions needed.')


