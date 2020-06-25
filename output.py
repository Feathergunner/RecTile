#!usr/bin/python
# -*- coding: utf-8 -*-import string

import os
import numpy as np

import matplotlib.pyplot as plt

import misc
import colormaps as cm

def save_as_img(A, filename="tiling", cmapdim=3, dirname='img', bw=True, col=True):
	dirname = str(dirname)
	if not os.path.isdir(dirname):
		os.mkdir(dirname)
	if cmapdim <= 3:
		if col:
			plt.imsave(dirname+'/'+filename+'_rgb.png', A, cmap=cm.cmap_rgb_3)
		if bw:
			plt.imsave(dirname+'/'+filename+'_gs.png', A, cmap=cm.cmap_gs_3)
	elif cmapdim <= 6:
		if col:
			plt.imsave(dirname+'/'+filename+'_rgb.png', A, cmap=cm.cmap_rgb_6)
		if bw:
			plt.imsave(dirname+'/'+filename+'_gs.png', A, cmap=cm.cmap_gs_6) 
		

def upscale(R, scale):
	d_x, d_y = R.shape
	R_scaled = np.zeros((d_x*scale, d_y*scale))
	for r_x in range(d_x):
		for r_y in range(d_y):
			for a_x in range(scale):
				for a_y in range(scale):
					R_scaled[r_x*scale+a_x][r_y*scale+a_y] = R[r_x][r_y]
	return R_scaled

def auto_upscale(A, n_max=2000):
	x,y = A.shape
	d_max = max(x,y)
	if d_max > n_max:
		return A
	else:
		return upscale(A, 1+n_max//d_max)
		
def construct_filename(name, style, offset, offset_mode, mod, it):
	if not offset == misc.OFFSET_NONE:
		of_string = misc.ofscodes[offset]+"_"+misc.ofmmodes[offset_mode]
	else:
		of_string = misc.ofscodes[offset]
	return name+"_"+misc.expcodes[style]+"_"+of_string+"_mod"+str(mod)+"_it"+str(it)