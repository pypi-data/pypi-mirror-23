QmeQ: Quantum master equation for Quantum dot transport calculations
====================================================================

QmeQ is an open-source Python package for calculations of transport through
quantum  dot devices. The so-called Anderson-type models are used to describe
the quantum dot device, where quantum dots are coupled to the leads by
tunneling. QmeQ can calculate the stationary state **particle** and
**energy currents** using various approximate density matrix approaches. As for
now we have implemented the following first-order methods

* Pauli (classical) master equation
* Lindblad approach
* Redfield approach
* First order von Neumann (1vN) approach

which can describe the effect of Coulomb blockade. QmeQ also has one
second-order method

* Second order von Neumann (2vN) approach

which can additionally address cotunneling, pair tunneling, and
broadening effects.

Physics disclaimer
------------------

All the methods in QmeQ are approximate so depending on parameter regime they
**can fail**, and a good knowledge of the method is required whether to trust
the result or not. For example, Redfield, 1vN, and 2vN approaches can **violate
positivity** of the reduced density matrix and lead to **currents flowing against
the bias**. We still think it is important to have a package where a user can
duplicate existing calculations, check applicability of different methods, or
simply discover new kind of physics using different approximate master equations.

Installation
------------

For installation instructions see [INSTALL.md](INSTALL.md).

Tutorial & Examples
-------------------

For an introduction to QmeQ see this [tutorial][tutorial]
and various [examples][examples]

License
-------

QmeQ has [The BSD 2-Clause License][license] and it can be found
in [LICENSE.md](LICENSE.md).

[tutorial]: https://github.com/gedaskir/qmeq-examples/tree/master/tutorial/tutorial.ipynb
[examples]: https://github.com/gedaskir/qmeq-examples
[license]: https://opensource.org/licenses/BSD-2-Clause
