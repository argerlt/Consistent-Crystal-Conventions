"""
Quaternions as Linear Transforms
================================
"""

# %%
# Things to discuss
# -----------------
# basic outline:
#   - start with complex numbers as "reshapers" of 2D plane
#   - show how :math:`sin(\theta) +{i}cos(\theta)`` is a 2D object that moves 2D objects
#   - For 2D, its equally mathematically difficult to just swith to 2x2 matrix, which is more inuitive
#   - Hamilton problem: equivalent doesn't exist for 3D. However, it does for 4D, and is efficient, lower error, and semi-human readable
#   - Formulation predates LA, and the correct way to write "q followed by p" is q*p (THIS IS A HUGE DEAL AND A SOURCE OF ERROR!)
#   - Also, since quat 4d but our world are 3D, easiest method is to do half of quat rote out of hyperplane, then second half back in, hence the hamiltonian
#   - :math:`(pq)^{-1} = q^{-1}[^-1]`. ie, switching passive to active reverses ordering. 


