|travis| |codecov| |pyup| |py3|

Giraumon
========

Giraumon is an anagram for Mirounga

Tools for Mirounga Hosting

Installation
------------

.. code-block:: bash

    pip install giraumon

or 

.. code-block:: bash

    git clone https://github.com/mgasystem/giraumon
    cd giraumon
    python setup.py install

Or in developper mode (Use virtualenv)

.. code-block:: bash

    git clone https://github.com/mgasystem/giraumon
    cd giraumon
    python setup.py develop

Configuration
-------------

Nothing to configure yet

Utilisation
-----------

In your repository application, use this command to initialize the files for deployment


.. code-block:: bash

    giraumon init . 

If no git found, you can creat one with -f,--force argument

.. code-block:: bash

    giraumon init --force . 


.. |travis| image:: https://travis-ci.org/mgasystem/giraumon.svg?branch=master
    :target: https://travis-ci.org/mgasystem/giraumon

.. |codecov| image:: https://codecov.io/gh/mgasystem/giraumon/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mgasystem/giraumon

.. |pyup| image:: https://pyup.io/repos/github/mgasystem/giraumon/shield.svg
    :target: https://pyup.io/repos/github/mgasystem/giraumon/

.. |py3| image:: https://pyup.io/repos/github/mgasystem/giraumon/python-3-shield.svg
    :target: https://pyup.io/repos/github/mgasystem/giraumon/
