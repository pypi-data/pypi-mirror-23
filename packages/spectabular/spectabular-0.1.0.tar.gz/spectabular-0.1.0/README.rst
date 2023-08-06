|Travis| |Conda| |Chat|

Spectabular: Visualization and eXploration
===================================


Spectabular is a program (and Python library) to visualize and explore large tabular datasets using statistics on an N-dimensional grid.
It mainly renders histograms, density plots and volume rendering  plots for visualization in the order of 10\ :sup:`9` rows in the order of 1 second.
For exploration it support selection in 1 and 2d, but it can also analyse the columns (dimensions) to find subspaces
which are richer in information than others.

.. image:: http://spectabular.readthedocs.org/en/latest/_images/overview.png

Spectabular uses several sites:

* Main page: http://spectabular.astro.rug.nl/
* Github for source, bugs, wiki, releases: https://github.com/maartenbreddels/spectabular
* Python Package Index for installing the source in your Python tree: https://pypi.python.org/pypi/spectabular/
* Documentation, similar to the homepage, but also has older versions: http://spectabular.readthedocs.org/

Installation
============

Using pip
::
 $ pip install --user --pre spectabular

Using conda
::
 conda install -c conda-forge spectabular


.. |Travis| image:: https://travis-ci.org/maartenbreddels/spectabular.svg?branch=master
   :target: https://travis-ci.org/maartenbreddels/spectabular
.. |Chat| image:: https://badges.gitter.im/maartenbreddels/spectabular.svg
   :alt: Join the chat at https://gitter.im/maartenbreddels/spectabular
   :target: https://gitter.im/maartenbreddels/spectabular?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Conda| image:: https://anaconda.org/conda-forge/spectabular/badges/downloads.svg
   :target: https://anaconda.org/conda-forge/spectabular
