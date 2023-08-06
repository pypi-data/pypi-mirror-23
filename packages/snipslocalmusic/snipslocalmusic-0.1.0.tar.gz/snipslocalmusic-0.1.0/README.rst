Local music player skill for Snips
==================================

|Build Status| |PyPI| |MIT License|


Installation
------------

The skill is on `PyPI`_, so you can just install it with `pip`_:

.. code-block:: console

    $ pip install snipslocalmusic

Usage
-----

The skill allows you to brew coffee using a `Smarter Coffee`_ machine. In order to use it, you need the IP address of your Smarter Coffee machine:

.. code-block:: python

    from snipssmartercoffee.snipssmartercoffee import SnipsSmarterCoffee

    smarter = SnipsSmarterCoffee(ip) 
    smarter.brew()

Copyright
---------

This skill is provided by `Snips`_ as Open Source software. See `LICENSE.txt`_ for more
information.

.. |Build Status| image:: https://travis-ci.org/snipsco/snips-skill-localmusic.svg
   :target: https://travis-ci.org/snipsco/snips-skill-localmusic
   :alt: Build Status
.. |PyPI| image:: https://img.shields.io/pypi/v/snipslocalmusic.svg
   :target: https://pypi.python.org/pypi/snipslocalmusic
   :alt: PyPI
.. |MIT License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/snipsco/snips-skill-smartercoffee/master/LICENSE.txt
   :alt: MIT License

.. _`PyPI`: https://pypi.python.org/pypi/snipshue
.. _`pip`: http://www.pip-installer.org
.. _`Snips`: https://www.snips.ai
.. _`LICENSE.txt`: https://github.com/snipsco/snips-skill-smartercoffee/blob/master/LICENSE.txt
