serplint
--------

A linter for the `Serpent <https://github.com/ethereum/serpent>`__
language.

.. figure:: https://i.imgur.com/VXb7mtK.png
   :alt: screenshot

   screenshot

Installation
~~~~~~~~~~~~

.. code:: sh

    $ pip install --upgrade serplint

Usage
~~~~~

.. code:: sh

    $ serplint filename.se

Current tests
~~~~~~~~~~~~~

-  undefined variables
-  reassigned arguments
-  unused arguments
-  unused assignment

Planned tests
~~~~~~~~~~~~~

-  array index out of bounds
-  data and event shadowing
-  magic numbers

Integrations
~~~~~~~~~~~~

-  Sublime Text 3
   `syntax <https://packagecontrol.io/packages/Serpent%20Syntax>`__ and
   `linter <https://packagecontrol.io/packages/SublimeLinter-contrib-serplint>`__
-  `neovim +
   neovmake <https://github.com/neomake/neomake/blob/663e9a73ef7f1c666feffa7f70851fb559212db7/autoload/neomake/makers/ft/serpent.vim>`__

TODO
~~~~

-  Visual Studio Code


