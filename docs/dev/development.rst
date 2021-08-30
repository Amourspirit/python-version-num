================
VERR DEVELOPMENT
================

Environment
===========

``verr`` use a ``conda`` environment.

Creating environment
--------------------

.. code-block:: bash
    :caption: terminal
    :name: terminal-conda

    # from root dir of project
    $ conda env create --prefix env --file environment.yml

Alternativly environment can be set up by running ``conda_env_create.py``

.. code-block:: bash
    :caption: terminal
    :name: terminal-python

    # from root dir of project
    $ python cmd/conda_env/conda_env_create.py