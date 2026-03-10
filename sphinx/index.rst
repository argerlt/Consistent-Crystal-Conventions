==============================
Consistent Crystal Conventions
==============================

.. toctree::
    :hidden:
    :titlesonly:

    user/index.rst
    conventions/index.rst
    reference/index.rst

A community-driven effort to create a consistent crystallographic convention for use in Material Science and related fields.
See the :doc:`Motivation Page <user/motivation>` to learn more about the motivation behind this work.
Visitors can navigate through the site using the buttons along the top header, or using the links below.

TODO: Add working quick links like dscribed `here <https://sphinx-design.readthedocs.io/en/furo-theme/grids.html>` 


.. See: https://sphinx-design.readthedocs.io/en/furo-theme/grids.html
.. grid:: 3

    .. grid-item-card::
        :link: user/index
        :link-type: doc

        :octicon:`book;2em;sd-text-info`   User Guide
        ^^^

        Installation, Contribution, References

    .. grid-item-card::  
        :link: conventions/index
        :link-type: doc

        :octicon:`list-unordered;2em;sd-text-info`   Conventions
        ^^^

        Proposed Conventions, Examples, and Common Errors
    
    .. grid-item-card::
        :link:     reference/index
        :link-type: doc

        :octicon:`code;2em;sd-text-info`   Python API
        ^^^
        
        API reference for python code used in this work.


Quick Start
===========
This project is `hosted on GitHub <www.github.com/argerlt/Consistent-Crystal-Conventions>`_ and primarily uses Python and ReStructuredText. 

The documentation you are reading is built using `Sphinx-Gallery <https://sphinx-gallery.github.io/stable/index.html>`_ and `The PyData Sphinx Theme <https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html>`_,
and the website is hosted on `ReadtheDocs <https://about.readthedocs.com>`_ 

Users familiar with these concepts can `clone the repository themselves <www.github.com/argerlt/Consistent-Crystal-Conventions>`_,
though for convenience we suggest instead creating a conda environment:

    .. code-block:: bash

        git clone https://github.com/argerlt/Consistent-Crystal-Conventions.git
        conda create -n ccc python=3.12
        conda activate ccc
        cd Consistent-Crystal-Conventions
        pip install -e ./

This is especially helpful when building the documentation via Sphinx:

    .. code-block:: bash

        cd sphinx
        make clean
        make html

Which can then be viewed by opening :code:`sphinx/_build/html/index.html` in a web browser.

Futher details can be found on the :doc:`Installation Page <user/installation>`

If you are interested getting involved, see the :doc:`Collaboration Page <user/contributing>` for details on how to contribute, report errors, or 
express concerns about one of the many subjective convention choices made as part of this work.

