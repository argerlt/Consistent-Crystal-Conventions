# Consistent-Crystal-Conventions

This repository is a first-pass attempt at creating a self-consistent and documented
set of conventions for handling crystallographic objects in material science, as well
as examples and visualizations of common errors that occur differing standards interact.

This work begins with the three basic objects in 3D space:
   - Vectors
   - Transforms
   - Symmetry

And builds up the decriptors needed for experimental tools such as EBSD, HEDM,
and TEM, as well as crystallographic concepts like orientations, misorientations,
and disorientations.

This is not intended as an end-all-be-all standard, but more as a teaching tool
as well as a reference point to help when converting data or techniques between
inconsistent conventions. (MTEX to ORIX, HEXRD to OIM, simulation to experiment, etc.)

This work is based on several existing standards (listed below). These are all
self-consistent and complete as isolated works, but create incongruities when used
together to describe concepts beyond their intended scopes. 

This work does however depart from the above standards in a few important ways:
1) It treats quaternions as the fundamental representation of a transform in 3D.
2) For every equation, python code is included, and if possible, augmented with 3D plots

*TODO: maybe add reasoning here?*

Documentation and Examples
==========================
All Documentation and examples are written with a combination of ReStructured Text and
Python, which is converted into Latex and HTML using ReadtheDocs, and is available online:
*TODO: add actual readthedocs link after I make it.*

The tools in the examples use the included `xtal_code`, whhich can be installed with ``pip``

.. code block:: python

    pip install -e ./Standard_crystal_transforms

*TODO: test this*

Starting References and Software
================================

The following publications are used as the basis for this work, **and should be cited in any publications or results derived from this work**

- [Crystallographic Texture and Group Representations](https://link.springer.com/book/10.1007/978-94-024-2158-3) (Chi-Sing Man): Sections 1.1 and 1.2
- [Structure of Materials](cambridge.org/highereducation/books/structure-of-materials/22A17D7856B8472E7B73B38F1147C0FD) (Marc De Graef and Michael McHenry) Chapters 4-10
- [International Tables for Crystallography, Volume A](https://it.iucr.org/A/)
- [On three-dimensional Misorientation spaces](https://doi.org/10.1098/rspa.2017.0274) (Robert Krakow et. al.)

*TODO: correctly reference/ credit these, add DOI's maybe?*

Additionally, while this is intended as a language-agnostic work, [ORIX](https://orix.readthedocs.io/en/stable/) is used as
the basis for much of the python code as many of the above standards have been partially implemented already.

Differences between this standard and ORIX
==========================================

ORIX, like all other software packages I am aware of, does not fully align with all the standards above, and has a few unique
hiccups. However, ORIX is also a semi-mature package with dozens of projects dependent on it,
so updating even accidental conventions will have significant knock-on effects.

Thus, this repository comes with a module MORIX (more orix) that alters some core functionality. If this
standard becomes popular, it might be rolled into ORIX eventually, or it might form a seperate project that ORIX
inherits from.

Related Talks
=============

This project will be first presented publically at TMS 2026 as part of the following talk:

**"An Effort Towards the Standardization of Disorientations in Texture"**

Texture analysis has been historically plagued by complications arising from differing orientation conventions. Recent work has helped alleviate this confusion, with two notable examples being the rotation representations from Rowenhorst et. al. 2015, and the misorientation fundamental zone conventions from Krakow et. al 2017. Many existing projects (MTEX, DREAM3D, ORIX , OIM, py4DSTEM, etc.) adopt or reference these standards, but these alone are insufficient to ubiquitously define disorientations between orientations. This can lead to difficult to diagnose errors when modeling relevant properties such as plastic deformation and fatigue. The current work builds on existing standards to define a unified set of texture conventions and includes an open-source repository of implementations in python. These can be adopted as-is by existing projects, but the primary intention is feedback from the community will help refine these conventions for an upcoming publication.

Austin Gerlt
*Hakon Anes*
*Steve Niezgoda*
*Marc Degraef*
*Anthony Rollett*
*David Rowenhorst*
Jake Benzing
(*Italicized names have expressed interest and are awaiting feedback*)

*TODO: add blurb with links encouraging contributions*


All software dependent on ORIX is released under a GPLv3 license (by necessity, not choice). All other
works are released under a *TODO, figure out proper CC license to use here*