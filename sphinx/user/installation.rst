.. _installation:

============
Installation
============

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



