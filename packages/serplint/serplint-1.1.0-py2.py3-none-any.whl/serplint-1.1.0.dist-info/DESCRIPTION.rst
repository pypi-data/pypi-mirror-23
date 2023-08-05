serplint
--------

A linter for the `Serpent <https://github.com/ethereum/serpent>`__
language.

.. figure:: https://i.imgur.com/VXb7mtK.png
   :alt: screenshot

   screenshot

Installation
~~~~~~~~~~~~

Until a new release of Serpent is uploaded to PyPi it's necessary to
install like so:

.. code:: sh

    $ pip install serplint
    $ pip install git+https://github.com/ethereum/serpent.git@3ec98d01813167cc8725a951bd384c629158af2b#egg=ethereum-serpent

Usage
~~~~~

.. code:: sh

    $ serplint filename.se

Current tests
~~~~~~~~~~~~~

-  undefined variables

Planned tests
~~~~~~~~~~~~~

-  array index out of bounds
-  function parameter not used in function
-  function parameter shadowing
-  magic numbers
-  unused assignment

Integrations
~~~~~~~~~~~~

TODO:

-  neovim + neomake
-  vscode
-  sublime


