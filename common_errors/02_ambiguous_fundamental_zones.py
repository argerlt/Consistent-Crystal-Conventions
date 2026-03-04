"""
Defining Fundamental Zones
==========================

Maybe rename this? But it's the idea that the "traditional" min(theta) method doesn't work on misorientations
and disorientations, but adopting a variation of the common ad-hoc examples like ORIX uses for PF or
Krakow et al did for orientation space.
"""
# %%
# This is a section header
# ------------------------
# This section should just be a copy/paste of my related rant from 2022.
#    - convenient definition of fundamental zone is "region of unique points containing origin", works for Orientation
#    - Does NOT work for Miller or Misorientation, b/c symmetry elements run through origin. 
#    - As such, we need some ad-hoc additional definitions. ITC gives some for Miller/IPF, but NOT for Misorientation.
#    - However, Krakow indirectly does, and by solidifying their common sense definitions, we can come up with a solid convention of our own.
#
# As a note, I don't think the Krakow method works for all SO3 subgroups, JUST the 32 point groups (also maybe the 112 magnetic point groups?
# I should google that....)

import numpy as np
print(1+1)