"""
Active and Passive Transforms
================================
"""
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import axes3d


# %%
# Things to discuss
# -----------------
# basic outline:
#   - Active describes moving a thing relative to a reference, passive describes moviing reference relative to object.
#   - Examples of where both make sense (maybe skip?)
#   - Importantly, all alse being equal, switching active to passive REVERSES THE ORDER OF THE EQUATION
#   - IE, it makes sense to read passive rotations left-to-right quaternion style, and active right-to-left LA style (this also agrees with the preferred conventions for Physics vs CompSci) 
#   - BIG TO DO: prove this out? ie, can we mix active/passive in one equation? i think so....


# code snippet for rotating wirefraame to show passive
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Grab some test data.
X, Y, Z = axes3d.get_test_data(0.05)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
# %%

# fig = plt.figure()
# ax = fig.add_subplot(projection="3d")

# # Grab some example data and plot a basic wireframe.
# X, Y, Z = axes3d.get_test_data(0.05)
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# # Set the axis labels
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")

# # Rotate the axes and update
# for angle in range(0, 360 * 4 + 1):
#     # Normalize the angle to the range [-180, 180] for display
#     angle_norm = (angle + 180) % 360 - 180

#     # Cycle through a full rotation of elevation, then azimuth, roll, and all
#     elev = azim = roll = 0
#     if angle <= 360:
#         elev = angle_norm
#     elif angle <= 360 * 2:
#         azim = angle_norm
#     elif angle <= 360 * 3:
#         roll = angle_norm
#     else:
#         elev = azim = roll = angle_norm

#     # Update the axis view and title
#     ax.view_init(elev, azim, roll)
#     plt.title("Elevation: %d°, Azimuth: %d°, Roll: %d°" % (elev, azim, roll))

#     plt.draw()
#     plt.pause(0.001)



#TODO: add pointers to how this is "solved" in the conventions folder