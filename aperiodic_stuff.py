#!usr/bin/python
# -*- coding: utf-8 -*-import string

import numpy as np
import random as rnd

import output

'''
def get_index(k, n):
	if k < n:
		return 0,n
	else:
		return k-n, n-1
'''
		
def aperiodic_tiling(n=1000, m=2, step_offset=2):
	# init:
	A = -1*np.ones((n,n))
	#B = np.zeros((n,n))
	colors = list(range(m))
	
	for x_i in range(n):
		s_max = 1
		for y_i in range(x_i,n):
			if A[x_i][y_i] < 0:
				c = rnd.choice(colors)
				step = s_max+step_offset
				s_max = step
				i = 0
				while y_i+i*step < n:
					A[x_i][y_i+i*step] = c
					A[y_i+i*step][x_i] = c
					#B[x_i][y_i+i*step] = step
					i += 1
			#if step < n:
			#	print (y_i)
				
	#print (B)
	return A

n = 50
m = 3
for m in [2,3,4,5]:
	A = aperiodic_tiling(n=n, m=m)
	A_scaled = output.auto_upscale(A)
	output.save_as_img(A_scaled, 'apertest_m'+str(m), cmapdim=m, dirname='img_aper')
	