#!usr/bin/python
# -*- coding: utf-8 -*-import string

import numpy as np

import recursive_structures as rs
import output
import misc
import colormaps as cm

### NEEDS UPDATING ANd ADJUSTING
### WILL NOT WORK IN CURRENT STATUs

# Some sets of matrices:
A1 = np.asarray([[1,0,0],[0,0,0],[0,0,0]])
A2 = np.asarray([[0,0,1],[0,0,0],[0,0,0]])
A3 = np.asarray([[0,0,0],[0,0,0],[0,0,1]])
A4 = np.asarray([[0,0,0],[0,0,0],[1,0,0]])

At1 = np.asarray([[1,0,1],[0,2,0],[0,3,0]])
At2 = np.asarray([[1,2,1],[1,3,1],[1,2,1]])
At3 = np.asarray([[0,2,0],[1,2,1],[3,2,3]])
At4 = np.asarray([[3,2,3],[2,1,2],[1,0,1]])


B1 = np.asarray([[0,0,1],[0,0,0],[0,0,1]])
B2 = np.asarray([[0,0,0],[0,1,0],[0,0,0]])
B3 = np.asarray([[0,1,0],[0,1,0],[0,1,0]])

C1 = np.asarray([[1,0],[0,0]])
C2 = np.asarray([[1,1],[1,0]])

D1 = np.asarray([[0,1],[3,2]])
D2 = np.asarray([[3,0],[2,1]])
D3 = np.asarray([[2,3],[1,0]])
D4 = np.asarray([[1,2],[0,3]])

E1 = np.asarray([[1,0],[0,0]])
E2 = np.asarray([[0,0],[0,1]])
E3 = np.asarray([[0,0],[1,1]])
E4 = np.asarray([[0,1],[1,1]])

F1 = np.asarray([[1,0],[0,1]])
F2 = np.asarray([[0,1],[1,0]])
F3 = np.asarray([[0,1,0],[1,0,1]])
F4 = np.asarray([[0,1],[1,0],[0,1]])
F5 = np.asarray([[1,0],[0,1],[1,0]])
F6 = np.asarray([[1,0,1],[0,1,0]])

G1 = np.asarray([[1,0,0],[0,1,1],[1,1,2]])

H1 = np.asarray([[1,0,0],[0,1,1],[0,0,0]])

J1 = np.asarray([[1,1,1],[1,1,0],[1,0,0]])
J2 = np.asarray([[1,1,0],[0,0,1],[0,0,1]])

K1 = np.asarray([[1,1,1,1],[1,1,1,0],[1,1,0,0],[1,0,0,0]])
K2 = np.asarray([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,1]])
K3 = np.asarray([[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]])

L1 = np.asarray([[1,1,1,1,1],[1,1,1,1,0],[1,1,1,0,0],[1,1,0,0,0],[1,0,0,0,0]])
L2 = np.asarray([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]])
L3 = np.asarray([[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1]])
L4 = np.asarray([[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]])
	
M1 = np.asarray([[1,0,0,1], [0,0,1,1], [1,1,0,1], [0,0,1,2]])
M2 = np.asarray([[1,1,0,0], [1,0,0,0], [0,0,0,1], [0,0,1,2]])
M3 = np.asarray([[0,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,2]])
M4 = np.asarray([[1,0,0,0], [0,0,1,0], [0,1,2,1], [0,0,1,0]])

N1 = np.asarray([[0,0,1],[1,0,1],[2,1,0]])
N2 = np.asarray([[1,0,0],[0,1,0],[0,0,1]])
N3 = np.asarray([[1,0,1],[0,1,0],[1,0,1]])
N4 = np.asarray([[0,1,0],[1,0,1],[0,1,0]])
N5 = np.asarray([[0,1,0],[1,0,1],[0,0,0]])

Rand = np.random.randint(0, high=3, size=(4,4))

Z4 = np.zeros((4,4))
if __name__ == '__main__':
	# create images:
	#rs.run_all_auto([At1, At2, At3, At4], name='A1234', stylecode='tiles')
	#rs.run_all_auto([F1, F1, F2], name='F112', stylecode='outsum')
	#rs.run_all_auto([G1], name='G1', style=rs.EXP_OUTER_SUM)
	rs.run_all_offsets([F3, F2, F1, F1, F6, F1, F1, F4], it=7, mod=4, name="F32116114_clouds", custom_cmap=cm.cmap_clouds)
	#rs.run([F1, F2, F1, F1, F2], it=8, mod=4, name="F12112", style=misc.EXP_OUTER_SUM, offset=misc.OFFSET_BLOCK, offset_mode=misc.OFM_ORT)#, custom_cmap=cm.cmap_dark)
	#rs.run([F3, F2, F1, F1, F5, F1, F1, F3], it=7, mod=4, name="F32115113_dark2", style=misc.EXP_OUTER_SUM, offset=misc.OFFSET_NONE, custom_cmap=cm.cmap_dark2)