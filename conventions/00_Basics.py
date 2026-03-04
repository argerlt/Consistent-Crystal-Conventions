"""
Vectors and transforms
======================
#TODO: summary
"""

import numpy as np
import matplotlib.pyplot as plt

# %%
# Vector Algebra Basics
# ---------------------
#
# Lets start by re-introducing some basic Vector algebra concepts, namely
# **Vectors** and **Transforms**.
#
# Vectors
# =======
# Consider a normal Euclidean space math:`E` of  :math:`n` dimensions, such as :math:`E^2` (an infinite 2D plane)
# or :math:`E^3` (a normal 3D space like the one we all live in).
# By additionally defining an origin point, we can define a vectors space :math:`V^n`, where
# each point in :math:`V^n` (ie, for :math:`v \in V^n`) represents a unique vector between the origin and that point.
#
# Next, lets adopt a righthanded orthonormal
# convention, meaning:
#   - We described points :math:`v \in V^n` using linear combinations of the unit vectors :math:`\{e_i : i = 1 ...n\}`
#   - These unit vectors are orthogonal, meaning :math:`e_i \cdot e_j = \delta_{ij}` where :math:`\delta_{ij}` is the `Kronecker delta <https://en.wikipedia.org/wiki/Kronecker_delta>`_.
# 
# And for `V^3` 
# specifically:
#   - :math:`e_i \times e_j = \epsilon_{ijk}e_k`, were  is the `Levi-Civita Symbol <https://en.wikipedia.org/wiki/Levi-Civita_symbol>`_ and :math:`\times` represents the `cross product <https://en.wikipedia.org/wiki/Cross_product>`_.
# as a non-rigorous simplification, this final point is what defines :math:`\begin{bmatrix} 1 \\ 0 \\ 0\end{bmatrix} \times \begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 1\end{bmatrix}` and not :math:`\begin{bmatrix} 0 \\ 0 \\ -1\end{bmatrix}`
#
# From these definitions, we are able to generate the following useful terms, which are
# identically defined in :code:`numpy`:
#   - the vector norm, :math:`||a|| = \sum_{i=1}^n a_i^2` 
#   - the dot product, :math:`a \cdot b = \sum_{i=1}^n {a_i}{b_j}`
#   - the cross product, :math:`a \times b = \sum_{i=1}^3\sum_{j=1}^3 {a_i}{b_j}{\epsilon_{ijk}}`
#
# These definitions are sufficient for the current work, but for a more expanded set of definitions, readers should refer to Chapter 1.1 of #TODO:line CSMann. Many of the definitions
# given there will become relevant for later sections.
#
# Linear Transformations
# ======================
# A "transform" in this context is an operation that re-maps every point :math:`v \in V^n` to another point in :math:`V^n`.
# A linear transformation :math:`L`has the further constraint that::math:
#    L(1 2 )









# %%
# This is a section header
# ------------------------
#


# %%
# This is a section header?
# =========================
#
# banana
# This is the first section!
# The `#%%` signifies to Sphinx-Gallery that this text should be rendered as
# reST and if using one of the above IDE/plugin's, also signifies the start of a
# 'code block'.
## Subheading?
# ------------
# This line won't be rendered as reST because there's a space after the last block.
myvariable = 2
print("my variable is {}".format(myvariable))
# This is the end of the 'code block' (if using an above IDE). All code within
# this block can be easily executed all at once.

# %%
# This is another section header
# ------------------------------
#
# In the built documentation, it will be rendered as reST after the code above!
# This is also another code block.

print('my variable plus 2 is {}'.format(myvariable + 2))