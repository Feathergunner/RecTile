#!usr/bin/python
# -*- coding: utf-8 -*-import string

import numpy as np

import recursive_structures as rs
import output
import misc

A1 = np.asarray([[1,0],[0,0]])
A2 = np.asarray([[0,0],[0,1]])

if __name__ == '__main__':
	it  = [2, 3, 4, 5, 6]
	mod = [2, 3, 4, 5, 6]
	for style in misc.expcodes:
		for ofs in misc.ofscodes:
			for ofm in misc.ofmmodes:
				if not style == misc.EXP_OUTER_SUM:
					this_mod = 2
				else:
					this_mod = mod
				if not (ofm == misc.OFM_ORT and (style == misc.EXP_OUTER_SUM or style == misc.OFFSET_NONE)):
					# compute recursive inflation,
					# leave out redundant combinations of inflations and offsets
					# NOTE: these conditions depend on the matrices A1, A2 !!!
	
					print ('Style: '+misc.expcodes[style])
					print ('Offset: '+misc.ofscodes[ofs])
					print ('Offset-mode: '+misc.ofmmodes[ofm])
					Rs = rs.recursive_inflating([A1, A2], it=it, mod=this_mod, style=style, offset=ofs, offset_mode=ofm)
					for R_data in Rs:
						# todo: parallelize this loop
						i = R_data['it']
						m = R_data['mod']
						R = R_data['R']
						print ('\t i: ',i, ', m: ', m)
						R_scaled = output.auto_upscale(R, 500)
						if m > 2:
							output.save_as_img(R_scaled, output.construct_filename('example', style, ofs, ofm, m, i), cmapdim=m, dirname='basic_examples')
						else:
							output.save_as_img(R_scaled, output.construct_filename('example', style, ofs, ofm, m, i), cmapdim=m, dirname='basic_examples', col=False)
	