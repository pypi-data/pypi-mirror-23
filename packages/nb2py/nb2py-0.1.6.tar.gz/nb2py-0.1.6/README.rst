nb2py
=====

Dumps marked code cells from a Jupyter notebook into a text file.

Features
--------

-  Reads a Jupyter Notebook and export marked code cells with the
   comment ``#~`` to a single ``.py`` file.
-  Exports cells marked with custom comments.
-  Exports a list of cells into a single file (useful to export markdown
   cells as a README.md file)

Dependencies
------------

None

Usage
-----

::

    import nb2py
    nb2py.dump('NB2PY_SOURCE.ipynb','nb2py.py')
    nb2py.dump_indices('NB2PY_SOURCE.ipynb','README.md',[3,2])

Notes: check that you saved your notebook before you use ``dump`` to see
the changes!

For examples, check the
`tutorial <https://github.com/HugoGuillen/nb2py/blob/master/tutorial.ipynb>`__.

Credits
-------

Created by `Hugo Guillen <https://github.com/HugoGuillen>`__, 2017.
