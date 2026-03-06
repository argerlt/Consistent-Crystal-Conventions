"""
Inverting an Orientation
========================

This is one of the more out there ideas of mine, need some feedback.
"""

# %%
# This is a section header
# ------------------------
# Main points
#   - orientations describe the ...orientatoin... of an object in a crystallographic space relative to an XYZ reference grid.
#   - in passive left-to-right, that would be written as xyz --> CS,
#   - in active right-to-left, that would be written as CS <-- xyx
#   - Additionally, there is no name for the thing that "undoes" an orientation. instead, people just write :math:`g^{-1}` or :math:`inv(g)`.
#   - The same notation is also used for inverting an orientation, WHICH IS DIFFERENT W.R.T HOW SYMMETRY IS LATER APPLIED!
#   - this also compounds with column-vs-row major ordering, increaing the confusion about "transposing" or "inverting" or "complex conjugate"
#   - Also, the thing that "undoes" an orientation is NOT an orientation, it does a different action and can only be applied to a differing set of objects. it should have it's own name.
#   - So, I propose "Orientation" and "Alignment".
#   - Passive Orientation:   CS <-- xyx
#   - Passive Alignment:     xyz <-- CS
#   - Active Orientation:    xyz --> CS
#   - Active Alignment       CS --> xyx
#   - This also clears up a bunch of REALLY common misorientation problems (elaborate)

myvariable = 2
print("my variable is {}".format(myvariable))
