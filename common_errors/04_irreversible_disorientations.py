"""
A Demonstration of the Information Loss in Symmetry Reduction
=============================================================
#TODO: convert from latex to python, and simplfy
The following is a copy/paste of chapter 3 of my thesis, and needs a LOT of cleanup, but has all the basic code.
"""

import numpy as np
import matplotlib.pyplot as plt
from orix.plot.rotation_plot import _setup_rotation_plot
from orix.quaternion.orientation_region import OrientationRegion
from orix.quaternion import symmetry
from orix.quaternion import Rotation
from orix.quaternion import Orientation
from orix.quaternion import Misorientation

###############################################################################
# define two grain using an axis and a rotation angle
# ---------------------------------------------------
grain_a = Rotation.from_axes_angles([-1, 2, 3], 25*np.pi/180)
grain_b = Rotation.from_axes_angles([4, -1, 7], 140*np.pi/180)
# define two symmetry groups. The first is the 3-fold 
#dihedral group, the second is space group 432.
SG_a = symmetry.D3
SG_b = symmetry.C6

# The misorientation calculation, where "~" represents 
# the inversion operation
m_ab = ~grain_a *grain_b

# the set of all symmetrically-equivalent misorientations 
# is found by applying all the symmetry operations in SG_a 
# to the left and SG_b to the right. This gives a 
# 6-by-24 array of all 144 permutations.
all_m_ab = Rotation(SG_a.outer(m_ab*SG_b))

###############################################################################
# Calculate the orientation and misorientation fundamental zones
# --------------------------------------------------------------
ori_fz_a = OrientationRegion.from_symmetry(SG_a)
ori_fz_b = OrientationRegion.from_symmetry(SG_b)
mis_fz_ab = OrientationRegion.from_symmetry(SG_a, SG_b)

###############################################################################
# find which representations are inside each of the fundamental zones
# -------------------------------------------------------------------
m_in_a = all_m_ab[all_m_ab < ori_fz_a]
m_in_b = all_m_ab[all_m_ab < ori_fz_b]
disorientation_ab = all_m_ab[all_m_ab < mis_fz_ab]

###############################################################################
# find all the representations that share the minimum angle
# ---------------------------------------------------------
min_angle = all_m_ab.angle.min() + 1E-6
min_angle_m = all_m_ab[all_m_ab.angle <= min_angle]

###############################################################################
# attempt to recover grain_a from the disorientation
# --------------------------------------------------
not_grain_a = disorientation_ab*~grain_b*SG_b
# symmeterize it to show it is not symmetrically 
# equivalent to grain_a
all_not_grain_a = Rotation(SG_a.outer(not_grain_a*SG_b).flatten())

###############################################################################
# get the wireframes for plotting the fundamental zones
# -----------------------------------------------------
D3_fz_bounds = ori_fz_a.get_plot_data().to_rodrigues().xyz
C6_fz_bounds = ori_fz_b.get_plot_data().to_rodrigues().xyz
D3_C6_fz_bounds = mis_fz_ab.get_plot_data().to_rodrigues().xyz

###############################################################################
# plot everything
# ---------------
fig, ax = _setup_rotation_plot(projection='3d')
ax.plot_wireframe(*D3_fz_bounds, color='k', linewidth=0.5, label=r"$D_3$ Fundamental Zone")
ax.plot_wireframe(*D3_C6_fz_bounds, color='r', linewidth=2, label=r"$D_3$-$C_6$ Fundamental Zone")
ax.scatter(*(min_angle_m.to_rodrigues().xyz), c='b', s= 40, label="Equidistant representations")
ax.scatter(*(disorientation_ab.to_rodrigues().xyz), c = 'k', s= 140, label=r"disorientation $d_{ab}$")
ax.axis('off')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0, wspace=0)
ax.set_aspect('equal')

###############################################################################
# Plot it again, but with the attempted inversion of the disorentations
# ---------------------------------------------------------------------
fig, ax = _setup_rotation_plot(projection='3d')
ax.plot_wireframe(*D3_fz_bounds, color='k', linewidth=0.5, label=r"$D_3$ Fundamental Zone")
ax.plot_wireframe(*D3_C6_fz_bounds, color='r', linewidth=2, label=r"$D_3$-$C_6$ Fundamental Zone")
ax.scatter(*(min_angle_m.to_rodrigues().xyz), c='b', s= 40, label="Equidistant representations")
ax.scatter(*(disorientation_ab.to_rodrigues().xyz), c = 'k', s= 140, label=r"disorientation $d_{ab}$")
ax.scatter(*(grain_b.to_rodrigues().xyz), label=r"$g_B$")
ax.scatter(*(all_not_grain_a.to_rodrigues().xyz), label=r"$dis_AB \cdot inv(g_A)$ ")
ax.axis('off')
ax.set_aspect('equal')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0, wspace=0)
fig.legend(loc = "lower right")

###############################################################################
# TODO Text
# ---------
#
# For any orientation describing a crystal lattice, there is also a set of symmetrically equivalent orientations formed by combining
# #the rotation operation with the symmetry group of the lattice. Since the lattices produced are indistinguishable from each other,
# it is common to think of the rotations themselves as functionally identical. However, this is not true; symmetrically equivalent
# orientations only produce identical results when applied in the forward direction, where they define a lattice relative to a reference
# frame. The same is not true when inverted, where they describe a reference frame relative to a lattice.

r"""
To demonstrate this, consider the Cartesian reference plane $xy$ containing the 6 pointed skewed star $H$ shown below. $H$ has the symmetry
of the 6-fold cyclic group $C_6$, while the reference frame has a 1-fold cyclic symmetry $C_1$ (i.e., no symmetry). Forward rotations describe
the orientation of a shape relative to a reference, and thus $H \cdot R_1$ and $H \cdot R_1 \cdot 3_2 \equiv H \cdot R_5$ describe identical
shape orientations. Here, $3_2$ represents two consecutive clockwise rotations of 120 degrees. However, inverse rotations describe the
orientation of a reference frame relative to a shape. Thus, the reference frame defined by $H \cdot R_5 \cdot inv(R_5) $ that aligns with
the starting reference frame for $H$ is different from the reference frame defined by $H \cdot R_5 \cdot inv(R_5)$.
"""

"""
...
.. image:: /_static/rots.png
    :alt: Demonstration of orientation inversions that produce differing references
    :align: center

"""

"""
In this example, an obvious response is to point out $R_1 \cdot inv(R_5)$ and $R_5 \cdot inv(R_5)$ differ by $240^o$, which is the symmetry operation
$3_2$ and an allowed operation in $C_6$. However, in the context of texture, orientations are operations that transform data between different domains, 
and symmetry operations are only allowed in domains that share that symmetry. Thus, $R_1 \cdot 3_2 \cdot inv(R_5)$ translates from $C_1$ to $C_6$, 
performs a legal symmetry operation for $C_6$, and translates from $C_6$ back to $C_1$. This is all allowed. On the other hand, $R_1 \cdot inv(R_5) \cdot 3_2$ 
performs the $3_2$ transform in $C_1$ space, which is incorrect. 

The inverted orientation operations in Figure \ref{fig:dis-hex} only appear to work because orientation and orientation inversion pairs are a special case where rotation operations happen to be commutative. This is not true for general rotation operations. Also note that if someone were only given the angle of $R_1 \cdot inv(R_1 \cdot 3_2) =120^o$, it would be possible to fully describe the symmetry operation relating $R_1$ and $R_5$, but not the initial value of $R_1$ itself. Similarly, knowing only that $R_5=323^o$ is not enough information to determine the symmetry operation that transformed $R_1$ to $R_5$.


%For the case of orientations, it is easy to see  $R_1 \cdot inv(R_3)$ and $R_3 \cdot inv(R_3)$ are related by $120^o$, which is a symmetry element of the cyclic group $C_6$. It is not technically a valid operation (this will be discussed later), but this symmetry operation can be applied in the symmetry-less coordinate frame to realign with the original reference frame. Thus, the symmetry element relating $R_1$ to $R_3$ can be recovered from  the value of $R_1 \cdot inv(R_3)$, though the values of $R_1$ and $R_3$ used to make  $R_1 \cdot inv(R_3)$ can not.

The extension of this idea for misorientations is that a symmetry-reduced misorientation (also called a disorientation) loses information about the orientations that formed it. As a result, \textbf{the effect of applying an inverted misorientation is generally different from that of applying its equivalent disorientation.}

This is a mathematical rule and not a new discovery. ``The Structure of Intercrystalline Interfaces"~\cite{interfaces-2000} uses language alluding to this loss of information when defining disorientations (``...the difference between the lowest energy angle and the real angle...'', page 406). In the following sections of that book, the authors made a point of only using disorientation angles for energy calculations, and revert to misorientations for any rotation operations. Their definition of disorientations was later used in ``On Three-Dimensional Misorientation Spaces''~\cite{Krakow-2017}, the paper used by MTEX, ORIX, and several other projects for defining FZs. Krakow et al.'s paper never directly addressed the information loss from disorientations, but it does illustrate the related phenomena that changing the starting reference symmetry for a misorientation causes "symmetrically equivalent" operations to express differently in the reference space. This is done in Figure 7b of their paper which is reproduced here in Figure \ref{fig:krakow_7b}.

\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{thesis_pics/Krakow-fig7.png}
    \caption{Image of the two different possible fundamental zone mappings for misorientations transforming from point group $432$ to $\bar{3}$ dependent on which point group was used as the reference frame.}
    \label{fig:krakow_7b}
\end{figure}

Despite the relevance of this disorientation information loss for many works past and present, I do not know of any publication directly stating this phenomenon in the context of quantitative texture analysis and providing examples or visualization. This is especially unfortunate, as the misapplication of disorientations seems to be a common source of error for many researchers including myself. The remainder of this chapter attempts to fill this gap. It begins with a discussion of the relevant mathematical and texture concepts, and ends with a step-by-step discussion with examples and visualization for how and why disorientations lose information. At every step, actual rotations are given so that the readers can reproduce the results if they wish.


\section{Background}

Any disorientation discussion, including the ordering of an equation or the interpretation of subscripts, is dependent on the choices of convention. For readers already familiar with passive rotations, Lie groups, neo-Eulerian vectors, and fundamental zones, this background can be summarized as follows and the remainder of the section skipped:

\begin{itemize}
    \item All types of rigid body rotations are non-commutative.
    \item This chapter uses the passive convention. Thus, the equations are read from left to right.
    \item The standard fundamental zone definition for orientations~\cite{Morawiec:js0039} is insufficient for misorientations and therefore cannot be used to uniquely define a disorientation. This is solved using the definition of the asymmetric fundamental zone from Krakow et al.~\cite{Krakow-2017}.
\end{itemize}

\subsection{Allowable operations}

All rigid body rotations (RBR) are elements of the Lie (pronounced ``Lee'') group $SO(3)$. This is also true of the texture objects derived from them: orientations, misorientations, disorientations, and symmetry operators. All mathematical groups consist of a set of elements and an operator. For $SO(3)$, the set is all possible rotations in 3D space, and the operator is successive application of two rotations. In formulas, the operator is often represented as $AB$, $A\cdot B$, or $A*B$. This notation aligns well with the combination operation using a dot product in matrix representation and a Hamilton product in quaternion representation, but it is important to remember those operations are not the same as the concept of the combination operation.

$SO(3)$ elements are associative and invertible, but not commutative. Thus, these operations are all valid:
$$ A \cdot A^{-1} = I,  \quad \quad A \cdot \left( B \cdot C \right) = \left(A \cdot  B\right) \cdot C , \quad \quad B\cdot A \cdot A^{-1} = A^{-1} \cdot A \cdot B = B$$
and these operations are not:
$$AB \neq BA, \quad \quad ABA^{-1} \neq B  $$
This becomes particularly relevant when considering the order in which symmetry elements are applied.

\subsection{Rotation Parametrizations}
\label{ch4-rot-params}
There are multiple ways to represent a rotation mathematically, each optimized for different purposes. Quaternions are computationally fast and consistent, matrix representations work well with axis-aligned property calculations, Bunge angles allow for highly efficient Fourier series representations, and neo-Eulerian vectors are best for plotting and visualization.

Regardless of the representations used though, all equations using elements of $SO(3)$ will produce equivalent results. For example, consider two rotations $A$ and $B$.
\newpage

\begin{itemize}
    \item \textbf{A} : a 55 degree clockwise rotation around the vector $[1, 1, 1]$
    \begin{itemize}
        \item \textbf{quaternion:} $[0.870,0.267, 0.267, 0.267]$
        \item \textbf{matrix:} $ \left[\begin{smallmatrix} 
        0.716 & -0.331  & 0.615\\ 
        0.615 & 0.716 & -0.331 \\ 
        -0.331 & 0.615 & 0.716
        \end{smallmatrix} \right] $
        \item \textbf{Bunge angles:} $ \left[ 208.3^{\circ}, 44.3^{\circ}, 118.3^{\circ} \right]$        
    \end{itemize}
\end{itemize}
\begin{itemize}
    \item \textbf{B} : a 34 degree clockwise rotation around the vector $[0, 2, 3]$
    \begin{itemize}
        \item \textbf{quaternion:} $[0.956, 0, 0.162, 0.243]$
        \item \textbf{matrix:} $ \left[\begin{smallmatrix} 
        0.829 & -0.465  & 0.310\\ 
        0.465 & 0.882 & 0.079 \\ 
        -0.310 & 0.079 & 0.947
        \end{smallmatrix} \right] $
        \item \textbf{Bunge angles:} $ \left[ 225.7^{\circ}, 18.7^{\circ}, 75.7^{\circ} \right]$
    \end{itemize}
\end{itemize}

Combining these operations together in any form will produce equivalent representations whether the combination operations were Hamiltonians of quaternions, matrix products of orthogonal matrices, or successive rotations by Euler angles:
$$ A \cdot A \cdot B \cdot A^{-1} = [0.740, 0.436, 0.239, 0.481] =\left[\begin{smallmatrix} 
        0.421 & -0.520  & 0.743\\ 
        0.906 & 0.210 & -0.367 \\ 
        -0.349 & 0.828 & 0.560
        \end{smallmatrix} \right]  = \left[ 178^{\circ}, 56^{\circ}, 116^{\circ} \right] $$

\subsection{Active Versus Passive Notation}

The orientation of an object relative to a reference frame can be described in one of two ways. Either the active rotation that will align the object with the reference frame, or the passive rotation that will align the reference frame while the undisturbed object. These two conventions produce equal and opposite rotations, but also require reversed equations to describe the same operation. This is why writing the equation for a disorientation (i.e., the symmetry-reduced representation of the misalignment between two orientations) requires preemptively declaring a passive or active convention. 

Consider an operation that realigns the vector $ v = \begin{matrix} [ 0 & 1 & 0] \end{matrix}$ to the vector \newline
$\begin{matrix}v' = [0 & 0 & 1] \end{matrix}$. The passive rotation describing this transform would move the y-axis of the coordinate map to the position of the old z-axis, whereas the active would move the vector $v$ in an identical but reversed direction to align $v$ with the unmoved z-axis. Using matrix representations, this becomes:

$$ R_{A} = \left[\begin{matrix} 
        1 & 0  & 0\\ 
        0 & 0 & -1 \\ 
        0 & 1 & 0
        \end{matrix} \right] \quad \quad 
        R_{P} = \left[\begin{matrix} 
        1 & 0  & 0\\ 
        0 & 0 & 1 \\ 
        0 & -1 & 0
        \end{matrix} \right] \quad \quad R_{P}=R_{A}^{-1}  $$

To transform $v$ to $v'$, $R_A$ and $R_B$ must each be applied differently. For the active rotation, one might say " I want to apply a rotation to a vector to align it with a coordinate system" which in explicit right-to-left linear algebra notation would be written as:

$$e_{i} \cdot R_{A} \cdot v = \left[\begin{matrix} 
        e_1 & e_2  & e_3
        \end{matrix} \right] \left[\begin{matrix} 
        1 & 0  & 0\\ 
        0 & 0 & -1 \\ 
        0 & 1 & 0
        \end{matrix} \right] \left[\begin{matrix}0\\1\\0 \end{matrix}\right] = \left[\begin{matrix}0\\0\\1 \end{matrix}\right] $$

Conversely, the passive rotation would be stated as "I want to apply a rotation to the coordinate system to align it to a object", which would be written as:

$$v \cdot R_{P} \cdot e_{i}  = \left[\begin{matrix} 
        0 & 1  & 0
        \end{matrix} \right] \left[\begin{matrix} 
        1 & 0  & 0\\ 
        0 & 0 & 1 \\ 
        0 & -1 & 0
        \end{matrix} \right] \left[\begin{matrix}e_1 \\ e_2  \\ e_3
        \end{matrix}\right] = \left[\begin{matrix}0\\0\\1 \end{matrix}\right] $$

In shorthand notation, this just becomes: 

$$ R_A \cdot v = v' \quad \quad v \cdot R_P = v'\quad \quad R_A \cdot v =v \cdot R_P$$

The extension to this process for applying successive rotations is discussed more rigorously in "Crystallographic Texture and Group Representations" Section 1.5~\cite{man2023crystallographic}, but to summarize, converting from active to passive rotations or vice versa requires inverting both the rotations and the ordering. For example:

$$R_{P1} = R_{A1}^{-1} \quad \quad R_{P2} = R_{A2}^{-1} \quad \quad R_{P3} = R_{A3}^{-1} $$
$$R_{P123} = R_{P1}R_{P2}R_{P3} =R_{A1}^{-1}R_{A2}^{-1}R_{A3}^{-1} = {(R_{A3}R_{A2}R_{A1})}^{-1} = R_{A321}^{-1}$$

Thus, the proper way to write successive rotation operations using the passive convention is to order them from left to right, which is \textbf{opposite} of what is typically taught in linear algebra or continuum mechanics\footnote{This, in my opinion, seems to be the major dividing point on whether people prefer active or passive.Those seeing matrices as the fundamental representation of a rotation prefer active, where equations are read right to left. Those who prefer quaternions or treating rotations as an abstract concept outside linear algebra assumptions prefer passive, where equations read left to right like in grade school algebra}. An interesting side effect of this is that passive versus active rotations as described by Bunge angles (which are just three angles describing 3 successive rotations) are not only inverted but reversed.

$$A_{passive} = \left[ 225.7^{\circ}, 18.7^{\circ}, 75.7^{\circ} \right] \quad \quad A_{active} = \left[ 284.3^{\circ}, 341.3^{\circ}, 284.3^{\circ} \right]$$

The choice of active versus passive also affects the interpretation of what domain an orientation is transforming to and from, and thus the preferred ordering of subscripts. Consider three different domains. The first is the lab space, with a point group symmetry $C_1$.  This is the domain of the reference frame which orientations are defined relative to. The second is the three-fold dihedral group $D_3$ ($32$ in Hermann-Mauguin notation). The 6 symmetry operators of $D_3$ and their quaternion representations are:
$$D_3= \left[{\begin{matrix} 
I  \\
3_1 \\
3_2 \\
2_x \\
2_u \equiv 3_1 \cdot 2_x\\
2_v \equiv 3_2 \cdot 2_x\end{matrix}} \right]=\left[{\begin{matrix} 
1, & 0, & 0,  &0] \\
\frac{1}{2}, & 0, & 0, & \frac{\sqrt{3}}{2} \\
\frac{-1}{2}, & 0, & 0, & \frac{\sqrt{3}}{2} \\
0, & 1, & 0, & 0 \\
0, & \frac{1}{2}, & \frac{\sqrt{3}}{2}, & 0 \\
0, & \frac{-1}{2}, & \frac{\sqrt{3}}{2}, & 0 \\ 
\end{matrix}} \right]$$
The second is the 2-fold dihedral group, $D_2$. The 4 symmetry operators of $D_2$ and their quaternion representations are:
$$D_2= \left[{\begin{matrix} 
I  \\
2_x \\
2_y \\
2_z \end{matrix}} \right]=\left[{\begin{matrix} 
1, & 0, & 0,  &0] \\
0, & 1, & 0,  &0] \\
0, & 0, & 1,  &0] \\
0, & 0, & 0,  &1]  \end{matrix}} \right]$$

There are a few possible rotation objects, each of which describe transformations between specific types of domains.
\begin{itemize}
\item An orientation $g_a$ is from lab space into crystal space
\item An inverted orientation $g_{a'}$ is from crystal space into lab space
\item a misorientation $m$ is from one crystal space into another.
\item a symmetry is from one crystal space back to the same crystal space.
\item a rotation is from lab space back into lab space.
\end{itemize}
This can be difficult to keep track of, and the ordering changes based on passive or active. One possible option for notation to help track this would be the use of left and right superscripts.
$$ {^{C_1}}{g_b}{^{D_3}} \quad \quad  {^{D_2}}{g_{a'}}{^{C_1}} \quad  \quad  {^{D_2}}{m_{ab}}{^{D_3}} \quad \quad  {^{D_3}}{3_2}{^{D_3}} \quad  \quad  {^{C_1}}{R_{x}}{^{C_1}}$$
This makes it easy to quickly see which equations are symmetrically valid and/or equivalent by checking for matching left-right superscripts between operators.
$$ {^{C_1}}{g_a}{^{D_3}} \equiv  {^{C_1}}{g_a}{^{D_3}} \cdot  {^{D_3}}{3_1}{^{D_3}} \equiv  {^{C_1}}{g_a}{^{D_3}} \cdot  {^{D_3}}{3_2}{^{D_3}}$$
$$ {^{C_1}}{g_a}{^{D_6}} \neq  {^{D_6}}{3_1}{^{D_6}} \cdot  {^{C_1}}{g_a}{^{D_6}} \neq  {^{D_6}}{3_2}{^{D_6}} \cdot  {^{C_1}}{g_a}{^{D_6}} $$
However, this notation quickly becomes cluttered in large equations. Instead, it is simpler to remove all $C_1$ superscripts, since they provide no extra information on allowed symmetry groups, and drop the superscripts entirely from the symmetry operators since their name already encodes the symmetry groups they are allowed in. This still aids in checking the validity of symmetry operations, and also gives a useful way to distinguish between orientations and inverted orientations, which don't have a good name in texture literature. For example, the following functions are symmetrically valid:
$${g_a}^{D_3} \equiv  {}{g_a}{^{D_3}} \cdot {3_1} \equiv  {}{g_a}{^{D_3}} \cdot {3_2} \equiv  {}{g_a}{^{D_3}} \cdot {2_x} \equiv  {}{g_a}{^{D_3}} \cdot {2_u} \equiv  {}{g_a}{^{D_3}} \cdot {2_v}$$
$$ {^{D_3}}{m_{ab}}{^{D_2}} =  {^{D_3}}{g_{a'}}{} \cdot g_b^{^{D_2}} $$
$$  {^{D_3}}{m_{ab}}{^{D_2}} \equiv 3_1 \cdot  {^{D_3}}{m_{ab}}{^{D_2}} \cdot 2_x $$
whereas an invalid operation like an orientation followed by an inverted orientation
$$g_b^{^{D_2}} \cdot  {^{D_3}}{g_{a'}}{}$$
or a symmetry element applied to the improper side of a misorientation
$$ {^{D_3}}{m_{ab}}{^{D_2}} \cdot 2_u$$
are immediately obvious.

\subsection{Fundamental Zones for symmetry aware orientations}
\label{sect_fz}
A fundamental zone (FZ) is a continuous subdomain in $SO(3)$ that contains every unique representation only once. For simplicity, a common convention for orientations~\cite{Morawiec:js0039} is to define the FZ as the set of unique representations with the smallest angular magnitude. The boundaries for an FZ defined this way can be quickly found via a Voronoi tessellation of the symmetry elements, with the Voronoi cell containing the identity rotation giving the boundaries. The tesselation can be done for all systems on the 3D surface of the quaternion unit sphere, but crystal systems with $D_2$ as a quotient group can perform a simpler tesselation in Rodriguez space as well. Figure ~\ref{fig:fz_comp} gives an example of FZs defined this way for both $D_3$ in blue and $m\bar{3}m$ in red, both plotted inside a sphere of radius $\pi$ representing all possible rotations in axis-angle vector space~\cite{ rowenhorst-2015}.

\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{thesis_pics/FZ_comp.png}
    \caption{The bounds of the $D_3$ (blue) and $m\bar{3}m$ (red) fundamental zones compared the sphere of all possible orientations, plotted in axis-angle vector space. Plotting is done using homochoric vectors~\cite{rowenhorst-2015}.}
    \label{fig:fz_comp}
\end{figure}

However, this definition is insufficient for finding the disorientation of a misorientation, since multiple symmetry combinations produce different misorientations with identical magnitudes. The most extreme example of this is seen for a misorientation both to and from $432$. There are 24 symmetry operations in the point group $432$, meaning there are $24 \cdot 24 = 576$ permutations of symmetry operators that can be applied to find symmetrically equivalent misorientations.
    $$m_{a(i,j)} = S_i \cdot m_a S_j \quad for \quad i=1:48 \quad for \quad j=1:48$$

Of these 576 combinations, up to 24 unique misorientations will be tied for the smallest possible angular resolution, and thus all land in the $432$ fundamental zone. Figure \ref{fig:dis-plt} shows an example of this for the randomly chosen misorientation quaternion $m_a = [0.9537, 0.2411, 0.1607, 0.0804]$ (a 35-degree twist around the [3,2,1] axis).

\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{thesis_pics/dis_fz.png}
    \caption{On the left, and example of 24 symmetrically equivalent misorientations for the $432-432$ misorientation system equidistant from the origin. Of these, only one falls into the misorientation fundamental zone, which has the further requirement of being within the IPF sector shown on the right. The (001) mirror is accounted for by the IPF plot being limited to the northern hemisphere.}
    \label{fig:dis-plt}
\end{figure}

The maximum number of repetitions will be equal to the number of shared symmetry operators between the starting and ending groups, hence $432-432$ having the most with 24. A solution is to further restrict the disorientation fundamental zone as the subset of unique lowest angle misorientation representations whose rotation axes also fall within the fundamental zone of an inverse pole figure plot. Applying this to the example above, the disorientation fundamental zone is further restricted by 4 planes in axis-angle space corresponding with the (010), (110), (101), and (001) mirror planes that define the IPF zone for $432$ and $m\bar{3}m$.


\section{Defining and Calculating a Disorientation}

With these definitions, it is now possible to uniquely define a disorientation in the passive rotation convention as the symmetrically equivalent misorientation that falls within the disorientation fundamental zone. 
$$  {^{Sl}}{d_a}{^{Sr}} = Sl_i \cdot  {^{Sl}}{m_a}{^{Sr}} \cdot Sr_j, \quad \quad Sl_i \in Sl, \quad Sr_j \in Sr, \quad Sl_i \cdot m_a \cdot Sl_j \in FZ(Sl \rightarrow Sr)$$
$FZ$ is the misorientation fundamental zone as described in section \ref{sect_fz} and adopted from Krakow et.al~\cite{Krakow-2017}. Those working in Python and wishing to follow along with this section can use the  \texttt{OrientationRegion} 
 class in ORIX version 0.13.2~\cite{orix-code} to build fundamental zones adhering to this definition.

The previous fundamental zone plots used neo-Eulerian projections to make the fundamental zone visualizable, but the process of building an envelope by defining planes also works directly in quaternion space. The method requires only a single quaternion to define each bounding hyperplane; thus the $432-432$ fundamental zone can be described with only 5 vectors. This makes determination of the disorientation computationally very efficient using this approach. 

\section{Improperly Calculated Disorientations}

\subsection{Calculating Misorientations}
The first common problem with disorientations is when the misorientation they a generated from is improperly calculated. A misorientation is the symmetry-aware rotation between two crystal spaces. A common way they appear is when comparing two orientations, such as the orientations of two grains that share a boundary. Such a misorientation from grain $a$ to grain $b$ would be calculated as:
$$ {^{D_3}}{m_{ab}}{^{432}} = inv( {}{g_a}{^{D_3}}) \cdot  {}{g_b}{^{432}} =  {^{D_3}}{g_{a'}}{} \cdot  {}{g_b}{^{432}}$$
Which, in short-hand, is just:
$$m_{ab} = g_{a'} \cdot {g_b}$$

A common source of error is the use of an incorrect equation to define a misorientation. These are either symmetrically invalid:
$$ {^{D_3}}{m_{ab}}{^{432}} \neq  {}{g_a}{^{D_3}} \cdot  {}{g_b}{^{432}}$$
Symmetrically valid, but meaningless:
$$ {^{D_3}}{m_{ab}}{^{432}} \neq  {}{g_a}{^{D_3}} \cdot  {^{D_3}}{g_{b'}}{}$$
Or correct but inverted:
$$ {^{D_3}}{m_{ab}}{^{432}} \neq  {^{432}}{g_{b'}}{} \cdot  {}{g_a}{^{D_3}}$$
Of these, the second is equivalent to the rotation example in Figure \ref{fig:dis-hex}, describing a reference frame relative to a different reference frame. If $g_a$ and $g_b$ happen to be related by an element of $D_3$, this is a rare case where a symmetry from $D_3$ can be performed on the reference frame to realign information. Otherwise, a symmetry-less rotation is produced. If that rotation is then improperly treated as a misorientation and reduced to the fundamental zone, it will give an incorrect angle and axis of rotation.

However, the third is the most common mistake. This is because the operation described is the definition of a misorientation in active notation. Extrapolating the above notation for the active rotation convention, a misorientation between grain $a$ and $b$ would be the rotation that aligned the second grain $b$ in $432$ with the reference grain $a$ in $D_3$.

$$ {^{D_3}}{{mA}_{ab}}{^{432}} =  {^{432}}{{gA}_{b}}{} \cdot  {}{{gA}_{a'}}{^{D_3}}$$

A disorientation generated from this misorientation will still give the correct rotation angle, but the rotation axis will be wrong, unless the fundamental zone used has also been defined in the reverse direction, in which case the axis will be the inverse of the correct one.

\subsection{Applying Symmetry Operators}

The other common problem with misorientations and, by extension, disorientations is the improper application of symmetry operations. As discussed, rotation objects are non-commutative, therefore order matters. Additionally, symmetry operators can only be applied in their valid domains. For the misorientation $m_{ab}$ :

$$ {^{D_3}}{m_{ab}}{^{432}} =  {^{D_3}}{g_{a'}}{} \cdot  {}{g_b}{^{432}}$$

Any number of symmetry operators from $D_3$ can be applied before the misorientation, but not after. The opposite is true for $D^{432}$. Thus, this is valid:
$$m_{ab} \equiv 3_1 \cdot m_{ab} \cdot 2_y$$
However, this is not:
$$m_{ab} \neq 3_1 \cdot m_{ab} \cdot 3_2$$
Furthermore, even if two groups share a symmetry operator and that operator is applied to the left, then inverted on the right:
$$m_{ab} \neq 2_x \cdot m_{ab} \cdot 2_x$$
That misorientation is symmetrically equivalent to the original, but NOT necessarily identical. They will be rotations related by a symmetry operation, but could have a different rotation angle.

\section{The Loss of Orientation Information}

Up to this point, we have covered disorientations, how to calculate them, and many of the improper calculations that occur when handling them. Now it is time to consider how they are generated from orientations. Combining the equations for misorientations and disorientations in passive notation produces the following:

$$  {^{Sl}}{d_{ab}}{^{Sr}} = Sl_i \cdot  {^{Sl}}{g_{a'}}{} \cdot  {}{g_b}{^{Sr}} \cdot Sr_j, \quad \quad Sl_i \in Sl, \quad Sr_j \in Sr, \quad Sl_i \cdot g_{a'}\cdot g_b \cdot Sl_j \in FZ(Sl \rightarrow Sr)$$
Which, dropping the symmetry-checking superscript, becomes:
$$d_{ab} = Sl_i \cdot g_{a'}\cdot {g_b} \cdot Sr_j $$
A common operation with misorientations is to use a misorientation to describe some inter-granular or other relationship, then later use one of the original orientations to recover the other. This is symmetrically valid.
$$ m_{ab}\cdot g_{b'} = g_{a'}\cdot g_b \cdot g_{b'} = g_a,  \quad \quad g_{a} \cdot m_{ab}  = g_a \cdot g_{a'}\cdot g_b = g_b $$ 

Repeating this with disorientations fails, due to the loss of a shared reference that occurs when the symmetry operations are applied.
$$g_a \cdot d_{ab} = g_a \cdot Sl_i \cdot g_{a'}\cdot g_b \cdot Sr_j  $$

Even if the user were given the disorientation and tried to brute-force check all the allowed symmetry operators, it would still not be possible to recover $g_b$ using only $d_{ab}$, $g_a$, symmetry operators.
$$g_a \cdot d_{ab} \cdot Sr_{j'} = g_a \cdot Sl_i \cdot g_{a'}\cdot g_b \cdot Sr_j \cdot Sr_{j'} = g_a \cdot Sl_i \cdot g_{a'}\cdot g_b$$

Generally, there is no way to eliminate the term $g_a \cdot Sl_i \cdot g_{a'}$. The exception is when $g_a \cdot Sl_i \cdot g_{a'}$ is equal to a symmetry element of the symmetry group $Sl$. This can happen when $g_a$ shares an axis of rotation with $Sl_i$, or when $Sl_i =1$.

In summary, unless $g_a \cdot Sl_i \cdot g_{a'} \in Sl$, the conversion of a misorientation to a disorientation results in an unrecoverable loss of data. Thus, while a disorientation is symmetrically equivalent, it is not identical to the misorientations that formed it.

\subsection{Example calculation in Python}

As a final addition, the following is a short Python script that correctly plots a disorientation, as well as the orientation and misorientation fundamental zones for two grains of differing orientation and space group. The inability to reverse a disorientation is also presented.
"""





















