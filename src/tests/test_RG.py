 #
 # QTop
 #
 # Copyright (c) 2016 Jacob Marks (jacob.marks@yale.edu)
 #
 # This file is part of QTop.
 #
 # QTop is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.

import sys
sys.path.append('../')
from src import surface_codes, error_models, visualization
sys.path.append('decoders/')
from rg import *
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

L, d, p = 7, 7, .1

code = surface_codes.SurfaceCode(L, d)
model = error_models.CodeCapacity()
code = code.CodeCycle(model, p)
visualization.PlotPlaquette(code, "Before Decoding", 1)

decoder = HDRG_decoder()
code = decoder(code)
visualization.PlotPlaquette(code, "After Decoding", 2)
plt.show()

