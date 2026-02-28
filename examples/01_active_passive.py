"""
Active and Passive Transforms
=============================

This example doesn't do much, it just makes a simple plot
"""

# %%
# This is a section header
# ------------------------
# This is the first section!
# The `#%%` signifies to Sphinx-Gallery that this text should be rendered as
# reST and if using one of the above IDE/plugin's, also signifies the start of a
# 'code block'.

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

print("my variable plus 2 is {}".format(myvariable + 2))


# %%
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Grab some test data.
X, Y, Z = axes3d.get_test_data(0.05)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
# %%

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Grab some example data and plot a basic wireframe.
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# Set the axis labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Rotate the axes and update
for angle in range(0, 360 * 4 + 1):
    # Normalize the angle to the range [-180, 180] for display
    angle_norm = (angle + 180) % 360 - 180

    # Cycle through a full rotation of elevation, then azimuth, roll, and all
    elev = azim = roll = 0
    if angle <= 360:
        elev = angle_norm
    elif angle <= 360 * 2:
        azim = angle_norm
    elif angle <= 360 * 3:
        roll = angle_norm
    else:
        elev = azim = roll = angle_norm

    # Update the axis view and title
    ax.view_init(elev, azim, roll)
    plt.title("Elevation: %d°, Azimuth: %d°, Roll: %d°" % (elev, azim, roll))

    plt.draw()
    plt.pause(0.001)
