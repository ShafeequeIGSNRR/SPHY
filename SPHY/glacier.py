# -*- coding: utf-8 -*-
#
# The Spatial Processes in HYdrology (SPHY) model:
# A spatially distributed hydrological model that calculates soil-water and
# cryosphere processes on a cell-by-cell basis.
#
# Copyright (C) 2013  Wilco Terink
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

#-Authorship information-###################################################################
__author__ = "Wilco Terink"
__copyright__ = "Wilco Terink"
__license__ = "GPL"
__version__ = "2.0.4"
__email__ = "terinkw@gmail.com"
__date__ ='26 May 2019'
############################################################################################

print 'glacier module imported'

#-Function to calculate melt from clean ice or debris covered glaciers
def GlacCDMelt(pcr, temp, ddf, glacfrac):
    glacdmelt = pcr.max(0, temp) * ddf * glacfrac
    return glacdmelt

#-Total glacier melt
def GMelt(glaccimelt, glacdcmelt):
    glacmelt = glaccimelt + glacdcmelt
    return glacmelt

#-Function to calculate runoff from glaciers
def GlacR(glacf, gmelt, glacfrac):
    glacr = glacf * gmelt * glacfrac
    return glacr

#-Function to calculate glacier percolation to groundwater
def GPerc(glacf, gmelt, glacfrac):
    gperc = (1 - glacf) * gmelt * glacfrac
    return gperc