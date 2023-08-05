PyPHS
======
A python software dedicated to the simulation of multiphysical systems in the Port-Hamiltonian Systems (PHS) formalism. 

.. image:: https://badge.fury.io/py/pyphs.svg
    :target: https://badge.fury.io/py/pyphs

.. image:: https://img.shields.io/badge/licence-CeCILL--B-blue.svg
    :target: http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html

.. image:: https://img.shields.io/badge/python-2.7%2C%203.5%2C%203.6-blue.svg
    :target: https://www.travis-ci.org/afalaize/pyphs
    
.. image:: https://img.shields.io/badge/documentation-website-blue.svg
    :target: https://afalaize.github.io/pyphs/

It is developped by :

* `Antoine Falaize <https://afalaize.github.io/>`_, `Team M2N <http://lasie.univ-larochelle.fr/Axe-AB-17>`_ (Mathematical and Numerical Methods) at the `LaSIE Research Lab <http://lasie.univ-larochelle.fr>`_ (CNRS UMR 7356), hosted by `Université de La Rochelle <http://www.univ-larochelle.fr/>`_, France. 
* `Thomas Hélie <http://recherche.ircam.fr/anasyn/helie/>`_, `Project/team S3 <http://s3.ircam.fr/?lang=en>`_ (Sound Signals and Systems) at `STMS Research Lab <http://www.ircam.fr/recherche/lunite-mixte-de-recherche-stms/>`_ (CNRS UMR 9912), hosted by `IRCAM <http://www.ircam.fr/>`_, Paris, France. 

It was initially developed between 2012 and 2016 as a part through a funding from French doctoral school `EDITE <http://edite-de-paris.fr/spip/>`_ (UPMC ED-130), and in connection with the French National Research Agency project `HaMecMoPSys <https://hamecmopsys.ens2m.fr/>`_.

.. image:: https://www.travis-ci.org/afalaize/pyphs.svg?branch=master
    :target: https://www.travis-ci.org/afalaize/pyphs
 

.. image:: https://ci.appveyor.com/api/projects/status/lmj2m2hfbo0bdqku/branch/master?svg=true
	:target: https://ci.appveyor.com/project/afalaize/pyphs

.. image:: https://codecov.io/gh/afalaize/pyphs/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/afalaize/pyphs

.. image:: https://www.quantifiedcode.com/api/v1/project/0c1fbf5b44e94b4085a24c18a1895947/badge.svg?branch=master
  :target: https://www.quantifiedcode.com/app/project/0c1fbf5b44e94b4085a24c18a1895947
  :alt: issues   

.. image:: https://landscape.io/github/afalaize/pyphs/master/landscape.svg?style=flat
   :target: https://landscape.io/github/afalaize/pyphs/master
   :alt: Health
       
Installation
==============
It is possible to install ``PyPHS`` from package (if you just want to use it) or source (if you plan to use it for development). Whichever method you choose, make sure that all prerequisites are installed.

Prerequisites
-------------

The ``PyPHS`` package run on Python 2.7 and Python
3.5 or newer (3.4 is no longer tested), with the following packages installed:

- `sympy <http://www.sympy.org/fr/>`_
- `numpy <http://www.numpy.org>`_
- `scipy <http://www.scipy.org>`_
- `matplotlib <http://matplotlib.org/>`_
- `networkx <http://networkx.github.io/>`_
- `stopit <https://pypi.python.org/pypi/stopit>`_
- `progressbar2 <https://pypi.python.org/pypi/progressbar2>`_
- `nose <https://github.com/nose-devs/nose>`_ (to run the tests)

Please refer to the `requirements.txt <requirements.txt>`_ file for the minimum
required versions and make sure that these modules are up to date.

Additionally, `theano <http://deeplearning.net/software/theano/>`_ is used if installed (for faster numerical evaluation of symbolic expressions).

The generated C++ sources build with CMake >= 3.1 (see **Configuration** below). The code relies on the `Eigen library <http://eigen.tuxfamily.org/index.php?title=Main_Page>`_ (not needed for pure Python usage).

Install from package
--------------------

The instructions given here should be used if you just want to install the package, e.g. to run the bundled programs or use some functionality for your own project. If you intend to change anything within the `PyPHS` package, please follow the steps in the next section.

The easiest way to install the package is via ``pip`` from the `PyPI (Python
Package Index) <https://pypi.python.org/pypi>`_::

    pip install pyphs

This includes the latest code and should install all dependencies automatically. If this is not the case, each dependency can be install the same way with ``pip``.

You might need higher privileges (use su or sudo) to install the package globally. Alternatively you can install the package locally
(i.e. only for you) by adding the ``--user`` argument::

    pip install --user pyphs

Install from source
-------------------

If you plan to use the package as a developer, clone the Git repository::

    git clone --recursive https://github.com/afalaize/pyphs.git

Then you can simply install the package in development mode::

    python setup.py develop --user

To run the included tests::

    python setup.py test

Configuration
--------------

After installation, it is recommanded to configure the `config.py </pyphs/config.py>`_ to your needs. Particularily, this is where the local path to the CMake binary and `Eigen library <http://eigen.tuxfamily.org/index.php?title=Main_Page>`_ is specified.

Your local `config.py </pyphs/config.py>`_ file is located at the root of the `PyPHS` package, which can be recovered with:
    
    >>> from pyphs import path_to_configuration_file
    >>> print(path_to_configuration_file)


Upgrade of existing installations
---------------------------------

To upgrade the package, please use the same mechanism (pip vs. source) as you did for installation. In each case, it is recommanded to uninstall the package first.

Upgrade a package
~~~~~~~~~~~~~~~~~

Simply upgrade the package via pip:

    pip install --upgrade pyphs [--user]

In some cases, you will need to manually uninstall the package:

    pip uninstall pyphs
    pip install pyphs [--user]


Upgrade from source
~~~~~~~~~~~~~~~~~~~

Simply pull the latest sources::

    git pull

Package structure
-----------------

The package is divided into the following folders:

`/pyphs/tutorials </pyphs/tutorials>`_
  Tutorials for the main `PyPHS` classes (executable programs).

`/pyphs/examples </pyphs/examples>`_
  Various applications (executable programs).

`/pyphs/core </pyphs/core>`_

    `PHSCore` class :
        This is the core PHS structure. It provides several methods for the manipulation of symbolic expression (reorganization, connection, simplification, etc.). It is passed as an argument to the constructor of most of others PyPHS objects.

`/pyphs/graphs </pyphs/graphs>`_     

    `PHSNetlist` class : 
        Management of netlist description files.

    `PHSGraph` class :
        (1) Construction and manipulation of network systems,
        (2) Analysis of network realizability,
        (3) Generation of PHS equations (`PHSCore`).

`/pyphs/dictionary </pyphs/dictionary>`_
    Components are `PHSGraph` objects. The dictionary is organized in thematic sub-packages (*electronics*, *thermics*, *fractional calculus*, etc.). Each theme is organized in component sub-packages (`electronics.resistor`, `thermics.transfer`, `fraccalc.fracderec`, etc.).

`/pyphs/numerics </pyphs/numerics>`_

    `PHSNumericalEval` class :
        Numerical evaluation of a given `PHSCore`.

    `PHSCoreMethod` object :
        Construction of the *symbolic* expressions associated with several numerical methods (theta-schemes, trapezoidal rule, discret gradient, etc.).

    `PHSNumericalCore` object :
        Numerical evaluation of a given `PHSCore` associated with a given `PHSCoreMethod`.

    `PHSSimulation` object :
        Perform the simulation of a given `PHSCore` associated with a given `PHSCoreMethod` through the execution of the resulting `PHSNumericalCore`.

    `PHSData` object :
        Methods for writing, reading and rendering `PHSSimulation` file results.

`/pyphs/tests </pyphs/tests>`_
    Test programs executed by `nose` (see above).

`/pyphs/misc </pyphs/misc>`_

    Miscelaneous tools (plots, LaTeX code generation, signal processing, iles I/O).
  
Documentation
==============

Implemented methods
--------------------
The package began as an implementation of the methods proposed in the reference [1]_, in which the port-Hamiltonian formalism, the graph analaysis and the numerical method are exposed. This is worth to read before using the `pyphs` package. 

Tutorials and examples
-----------------------

The package comes with a serie of tutorials for the use of the main functionalities (`definition </pyphs/tutorials/phscore.py>`_, `evaluation </pyphs/tutorials/phsnumericaleval.py>`_, and `simulation </pyphs/tutorials/phssimulation.py>`_ of a core PHS structure). More tutorials are to come. Additionally, you can see the `examples </pyphs/examples>`_ scripts. Both the *tutorials* and the *examples* folders are located at your package root, which can be recovered in Python interpreter with:

    >>> import pyphs
    >>> help(pyphs)

The `website <https://afalaize.github.io/pyphs/>`_ is not currently up-to-date.


Reference
=========
.. [1] Falaize, A., & Hélie, T. (2016). `Passive Guaranteed Simulation of Analog Audio Circuits: A Port-Hamiltonian Approach <https://hal.archives-ouvertes.fr/hal-01390501>`_. Applied Sciences, 6(10), 273.
