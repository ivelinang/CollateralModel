__author__ = 'Ivelin'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      13/11/2016
# Last Updated: 13/11/2016

# Filename:     Interpolator.py
# Python used:  3.4
#-------------------------------------------------------------------------------
# Description:  Serves as the main class for interpolation
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

import numpy as np
import scipy as sc
from scipy.interpolate import InterpolatedUnivariateSpline

class Interpolator(object):

    def __init__(self):
        pass

    @staticmethod
    def interpolate1d(x_axis, y_axis, keypoints, order):
        f=InterpolatedUnivariateSpline(x_axis, y_axis, k=order)
        interpolatedCurve=f(keypoints)

        return interpolatedCurve
