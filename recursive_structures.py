#!usr/bin/python
# -*- coding: utf-8 -*-import string

import numpy as np
import math

import colormaps as cm
import output

OUTER_SUM = 'OUTER_SUM'
INFLATION_TILING = 'INFLATION_TILING'

def update_outer_sum(R, r_x, r_y, As, a_x, a_y, d_x, d_y, j):
	x = r_x+d_x*a_x
	y = r_y+d_y*a_y
	r = R[r_x][r_y] + As[j][a_x][a_y]
	return x, y, r
	
def update_tiling(R, r_x, r_y, As, a_x, a_y, d_x, d_y, j=None):
	x = r_x*d_x + a_x
	y = r_y*d_y + a_y
	r = As[int(R[r_x][r_y])][a_x][a_y]
	return x,y,r

def recursive_inflating(As, it, mod=3, style=OUTER_SUM):
	'''
	Args:
		As  : list of matrices
		it  : number of iterations
		mod : modulo that is applied on the final matrix
		style : one of
			'KRONECKER_ADD'
			'INFLATION_TILING'
	'''
	
	if style == OUTER_SUM:
		update = update_outer_sum
	elif style == INFLATION_TILING:
		update = update_tiling
		d_x, d_y = As[0].shape
		d_block_x = d_x
		d_block_y = d_y
	else:
		return
	m = len(As)
	#full_dimm_x = 1
	#full_dimm_y = 1
	#for i in range(it):
	#	j = i%m
	#	dx, dy = As[j].shape
	#	full_dimm_x *= dx
	#	full_dimm_y *= dy
	
	d_total_x = 1
	d_total_y = 1
	R = np.zeros((d_total_x, d_total_y))
	for i in range(it):
		d_it_x = d_total_x
		d_it_y = d_total_y
		
		if style == OUTER_SUM:
			d_x, d_y = As[i%m].shape
			d_block_x = d_it_x
			d_block_y = d_it_y
			
		d_total_x *= d_x
		d_total_y *= d_y
			
		R_it = np.zeros((d_total_x, d_total_y))
		for a_x in range(d_x):
			for a_y in range(d_y):
				for r_x in range(d_it_x):
					for r_y in range(d_it_y):
						x,y,r = update(R, r_x, r_y, As, a_x, a_y, d_block_x, d_block_y, i%m)
						# print ("R_it["+str(x)+", "+str(y)+"] = "+str(r))
						R_it[x][y] = r #R[r_x][r_y] + As[i%m][a_x][a_y]
		R = R_it
	
	if style == OUTER_SUM and mod > 0:
		R = np.mod(R, mod)
	return R
	
def run(As, it, mod, stylecode='outsum', name=''):
	if stylecode == 'outsum':
		style = OUTER_SUM
	elif stylecode == 'tiles':
		style = INFLATION_TILING
	else:
		print ("No valid style specified!")
		return
	
	R = recursive_inflating(As, it, mod, style=style)
	output.save_as_img(R, stylecode+"_"+name+"_mod"+str(mod)+"_it"+str(it), cmapdim=mod)
	
def run_all_auto(As, name='', stylecode='outsum'):
		d_max = np.max([A.shape for A in As])
		
		it_max = int(math.log(1000, d_max))
		if stylecode == 'outsum':
			style = OUTER_SUM
			it_min = 4
			mod_max = 6
		elif stylecode == 'tiles':
			style = INFLATION_TILING
			it_min = 3
			mod_max = len(As)
		d = max(As[0].shape)
		
		for it in range(it_min, it_max+1):
			R = recursive_inflating(As, it, mod=-1, style=style)
			R_scaled = output.auto_upscale(R)
			for mod in range(2, mod_max+1):
				R_m = np.mod(R_scaled, mod)
				output.save_as_img(R_m, stylecode+"_"+name+"_mod"+str(mod)+"_it"+str(it), cmapdim=mod)

if __name__ == '__main__':
	print ('hello world')