SPECTRUM : Spectral Analysis in Python
==========================================



.. image:: https://badge.fury.io/py/spectrum.svg
    :target: https://badge.fury.io/py/spectrum.svg

.. image:: https://secure.travis-ci.org/cokelaer/spectrum.png
    :target: http://travis-ci.org/cokelaer/spectrum

.. image:: https://coveralls.io/repos/cokelaer/spectrum/badge.png?branch=master 
    :target: https://coveralls.io/r/cokelaer/spectrum?branch=master 

.. image:: https://landscape.io/github/cokelaer/spectrum/master/landscape.png
    :target: https://landscape.io/github/cokelaer/spectrum/master

.. image:: https://badge.waffle.io/cokelaer/spectrum.png?label=ready&title=Ready 
    :target: https://waffle.io/cokelaer/spectrum


:contributions: Please join https://github.com/cokelaer/spectrum
:issues: Please use https://github.com/cokelaer/spectrum/issues




.. image:: http://www.thomas-cokelaer.info/software/spectrum/html/_images/psd_all.png
    :class: align-right
    :width: 50%

**Spectrum** contains tools to estimate Power Spectral Densities using methods based on Fourier transform, Parametric methods or eigenvalues analysis:

    * The Fourier methods are based upon correlogram, periodogram and Welch estimates. Standard tapering windows (Hann, Hamming, Blackman) and more exotic ones are available (DPSS, Taylor, ...). 
    * The parametric methods are based on Yule-Walker, BURG, MA and ARMA, covariance and modified covariance methods.
    * Non-parametric methods based on eigen analysis (e.g., MUSIC) and minimum variance analysis are also implemented.
    * Multitapering is also available

Installation
================

::

    pip install spectrum


Contributions
==================

Please see `github <http://github.com/cokelaer/spectrum>`_ for any issues/bugs/comments/contributions.


Some notebooks (external contributions)
-------------------------------------------

* http://nbviewer.ipython.org/gist/juhasch/5182528
