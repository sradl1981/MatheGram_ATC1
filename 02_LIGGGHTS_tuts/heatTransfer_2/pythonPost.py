# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 15:35:00 2019

@author: sradl
"""

#~~~~~~~~~~~~~~~~~~USER INPUT~~~~~~~~~~~~~~~~~~~~~~~~~~~
fileName = 'post/myOut_40000.liggghts'

#~~~~~~~~~~~~~~END USER INPUT~~~~~~~~~~~~~~~~~~~~~~~~~~~
if 'dump' in locals():
    del dump #ensure dump is reloaded
    
from   dump import dump 
#import numpy as np
import matplotlib.pyplot as plt
plt.close("all")

#read / init the dump object
d = dump(fileName)

#plot speed
plt.figure()
plt.plot(d.snaps[0].atoms[:,d.names['vx']],'r.')

#plot temperature
plt.figure()
plt.plot(d.snaps[0].atoms[:,d.names['f_Temp']],'r.')

#plot temperature histogram
plt.figure()
myHist = plt.hist(d.snaps[0].atoms[:,d.names['f_Temp']], 
                  bins=20, 
                  density='true')


#~~~~~~~~~~~~~HINTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DUMP CLASS
#d.snaps[0].atoms[0][1]
#d.snaps[0].zlo

#access full data directly
#d.snaps[0].atoms[0][0]

#list names
#d.names 

#Get column index of a certain name (e.g., vx)
#d.names['vx']

#retrieve specific data for all atoms
#d.snaps[0].atoms[:,d.names['f_Temp']]

#retrieve data for an atom with ID
#idAtom=73
#d.atom(idAtom,"x")
