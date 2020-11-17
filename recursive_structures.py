#!usr/bin/python
# -*- coding: utf-8 -*-import string

import numpy as np
import math

import colormaps as cm
import output
import misc

### update-functions 
# these functions construct an entry of a block of the inflated matrix 
# based on a basis block R and
# a additional information matrices As
# the position of the block a_x, a_y and
# the position of the block-entry r_x, r_y and
# the block dimensions d_x, d_y

# return the position x,y and a value r

def update_outer_sum(R, r_x, r_y, As, a_x, a_y, d_x, d_y, j, shift_x=0, shift_y=0, offset_mode=misc.OFM_PAR):
	# unshifted position:
	x = r_x + d_x*a_x
	y = r_y + d_y*a_y
	# shifted position:
	if offset_mode == misc.OFM_PAR:
		x_shift = (r_x+shift_x*a_x)%d_x + d_x*a_x
		y_shift = (r_y+shift_y*a_y)%d_y + d_y*a_y
	else:
		x_shift = (r_x+shift_x*a_y)%d_x + d_x*a_x
		y_shift = (r_y+shift_y*a_x)%d_y + d_y*a_y
	# value:
	r = R[r_x][r_y] + As[j][a_x][a_y]
	return x_shift, y_shift, r
	
def update_tiling(R, r_x, r_y, As, a_x, a_y, d_x, d_y, j=None, shift_x=0, shift_y=0, offset_mode=misc.OFM_PAR):
	# unshifted position:
	x = r_x*d_x + a_x
	y = r_y*d_y + a_y
	# shifted position:
	if offset_mode == misc.OFM_PAR:
		x_shift = r_x*d_x + ((a_x+shift_x*r_x)%d_x)
		y_shift = r_y*d_y + ((a_y+shift_y*r_y)%d_y)
	else:
		x_shift = r_x*d_x + ((a_x+shift_x*r_y)%d_x)
		y_shift = r_y*d_y + ((a_y+shift_y*r_x)%d_y)
	# value:
	r = As[int(R[r_x][r_y])][a_x][a_y]
	return x_shift, y_shift, r
	
def update_repetition(R, r_x, r_y, As, a_x, a_y, d_x, d_y, j=None, shift_x=0, shift_y=0, offset_mode=misc.OFM_PAR):
	# unshifted position:
	x = r_x + d_x*a_x
	y = r_y + d_y*a_y
	# shifted position:
	if offset_mode == misc.OFM_PAR:
		x_shift = (r_x+shift_x*a_x)%d_x+d_x*a_x
		y_shift = (r_y+shift_y*a_y)%d_y+d_y*a_y
	else:
		x_shift = (r_x+shift_x*a_y)%d_x+d_x*a_x
		y_shift = (r_y+shift_y*a_x)%d_y+d_y*a_y
	# value:
	r = R[r_x][r_y]
	return x_shift, y_shift, r
	
### The recursive inflation algorithm:
def recursive_inflating(As, it, mod=3, style=misc.EXP_OUTER_SUM, offset=misc.OFFSET_NONE, offset_mode=misc.OFM_PAR):
	'''
	Args:
		As  : list of matrices
		it  : number of iterations
		mod : modulo that is applied on the final matrix
		style : one of
			misc.EXP_OUTER_SUM
			misc.EXP_INFLATION
			misc.EXP_REPETITION
		offset : one of
			misc.OFFSET_NONE
			misc.OFFSET_BLOCK
			misc.OFFSET_PIXEL
		offset_mode : one of
			misc.OFM_PAR
			misc.OFM_ORT
	'''
	if isinstance(it, int):
		multiit = False
		R_ret = None
		it_max = it
	else:
		multiit = True
		R_ret = []
		it_max = max(it)
		
	do_mod = True
	if isinstance(mod, int):
		if mod > 1:
			mod = [mod]
		else:
			do_mod = False
	
	dx_A, dy_A = As[0].shape
	d_total_x = 1
	d_total_y = 1
	R = np.zeros((d_total_x, d_total_y))
	
	if style == misc.EXP_OUTER_SUM:
		update = update_outer_sum
	elif style == misc.EXP_INFLATION:
		update = update_tiling
		d_x, d_y = dx_A, dy_A
		d_block_x = d_x
		d_block_y = d_y
	else:
		update = update_repetition
		d_x, d_y = dx_A, dy_A
		d_total_x = d_x
		d_total_y = d_y
		R = As[0]
		it_max -= 1
		if isinstance(it, list):
			it = [i-1 for i in it]
	
	m = len(As)
	for i in range(it_max+1):
		#print ("it: ", i)
		d_it_x = d_total_x
		d_it_y = d_total_y
		
		if style == misc.EXP_OUTER_SUM:
			d_x, d_y = As[i%m].shape
			d_block_x = d_it_x
			d_block_y = d_it_y
		
		if style == misc.EXP_REPETITION:
			d_block_x = d_it_x
			d_block_y = d_it_y
			
		d_total_x *= d_x
		d_total_y *= d_y
		
		# construct shift values:
		if offset == misc.OFFSET_BLOCK:
			if style == misc.EXP_REPETITION:
				shift_dx = max(1, i*d_x)
				shift_dy = max(1, i*d_y)
			elif style == misc.EXP_OUTER_SUM:
				shift_dx = max(1, (i-1)*d_x)
				shift_dy = max(1, (i-1)*d_y)
			else:
				shift_dx = 1
				shift_dy = 1
				
		elif offset == misc.OFFSET_PIXEL:
			shift_dx = 1
			shift_dy = 1
		elif offset == misc.OFFSET_LINEAR:
			shift_dx = i+1
			shift_dy = i+1
		elif offset == misc.OFFSET_EXPON:
			shift_dx = dx_A**i
			shift_dy = dy_A**i
		else:
			shift_dx = 0
			shift_dy = 0
		
		if i == 0 and not style == misc.EXP_REPETITION:
			shift_dx = 0
			shift_dy = 0
		# in case of orthogonal shift, switch shift values for x and y directions:
		if offset_mode == misc.OFM_ORT:
			shift_dx, shift_dy = shift_dy, shift_dx
		
		R_it = np.zeros((d_total_x, d_total_y))
		for a_x in range(d_x):
			for a_y in range(d_y):
				for r_x in range(d_it_x):
					for r_y in range(d_it_y):
						# compute value and shifted coordinates:
						x,y,r = update(R, r_x, r_y, As, a_x, a_y, d_block_x, d_block_y, i%m, shift_dx, shift_dy, offset_mode=offset_mode)
						R_it[x][y] = r
		R = R_it
		if multiit and i in it:
			R_ret.append({'it':i, 'mod': 0, 'R':R})
	if R_ret == None:
		R_ret = [{'it':it_max, 'mod':0, 'R':R}]

	if style == misc.EXP_OUTER_SUM and do_mod:
		R_ret = [{
			'R': np.mod(R_data['R'], m),
			'mod': m,
			'it': R_data['it']}	for R_data in R_ret for m in mod]
		
	if len(R_ret) == 1:
		return R_ret[0]['R']
	return R_ret

### some methods that run the recursive inflation:

def run(As, it, mod, style=misc.EXP_OUTER_SUM, offset=misc.OFFSET_NONE, name='', custom_cmap=None):
	### not sure if this works anymore
	### needs testing & adjusting
	if style not in misc.expcodes:
		print ("Error! Not a valid style specified!")
		return
	if offset not in misc.ofscodes:
		print ("Error! Not a valid offset specified!")
		return
	R = recursive_inflating(As, it, mod, style=style, offset=offset)
	output.save_as_img(R, output.construct_filename(name, style, mod, it, offset), cmapdim=mod, custom_cmap=custom_cmap)
	
def run_all_auto(As, name='', style=misc.EXP_OUTER_SUM):
	### not sure if this works anymore
	### needs testing & adjusting
	d_max = np.max([A.shape for A in As])
	
	it_max = int(math.log(1000, d_max))
	if style == misc.EXP_OUTER_SUM:
		it_min = 4
		mod_max = 6
	elif style == misc.EXP_INFLATION:
		it_min = 3
		mod_max = len(As)
	elif style == misc.EXP_REPETITION:
		it_min = 4
		mod_max = 6
	
	d = max(As[0].shape)
	
	for it in range(it_min, it_max+1):
		R = recursive_inflating(As, it, mod=-1, style=style)
		R_scaled = output.auto_upscale(R)
		for mod in range(2, mod_max+1):
			R_m = np.mod(R_scaled, mod)
			output.save_as_img(R_m, output.construct_filename(name, style, mod, it, offset), cmapdim=mod)

if __name__ == '__main__':
	print ('hello world')