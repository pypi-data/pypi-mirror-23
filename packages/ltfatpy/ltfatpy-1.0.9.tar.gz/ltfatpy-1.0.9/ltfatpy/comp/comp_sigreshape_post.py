# -*- coding: utf-8 -*-
# ######### COPYRIGHT #########
#
# Copyright(c) 2017
# -----------------
#
# * LabEx Archimède: http://labex-archimede.univ-amu.fr/
# * Laboratoire d'Informatique Fondamentale : http://www.lif.univ-mrs.fr/
# * Institut de Mathématiques de Marseille : http://www.i2m.univ-amu.fr/
# * Université d'Aix-Marseille : http://www.univ-amu.fr/
#
# This software is a port from LTFAT 2.1.0 :
# Copyright (C) 2005-2017 Peter L. Soendergaard <peter@sonderport.dk>.
#
# Contributors
# ------------
#
# * Denis Arrivault <contact.dev_AT_lif.univ-mrs.fr>
# * Florent Jaillet <contact.dev_AT_lif.univ-mrs.fr>
#
# Description
# -----------
#
# ltfatpy is a partial Python port of the Large Time/Frequency Analysis Toolbox
# (http://ltfat.sourceforge.net/), a MATLAB®/Octave toolbox for working with
# time-frequency analysis and synthesis.
#
# Version
# -------
#
# * ltfatpy version = 1.0.9
# * LTFAT version = 2.1.0
#
# Licence
# -------
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ######### COPYRIGHT #########


""" Module of comp_sigreshape_post calculation

Ported from ltfat_2.1.0/comp/comp_sigreshape_post.m

.. moduleauthor:: Denis Arrivault
"""

from __future__ import print_function, division

import numpy as np


def comp_sigreshape_post(f, fl, wasrow, remembershape):
    """Get original dimensionality

    .. warning::
        This function returns **f** or a view of **f** if possible. In those
        cases, any value changed in the returned variable will also be
        changed in **f**.
    """
    fd = len(remembershape)

    if fd > 2:
        return f.reshape((fl,) + remembershape[1:fd])
    if wasrow:
        return f[np.newaxis, :]
    return f
