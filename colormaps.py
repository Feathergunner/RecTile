#!usr/bin/python
# -*- coding: utf-8 -*-import string

import matplotlib.colors as cls

# default cmaps:
cmap_list_rgb_3 = [[1.0,0.0, 0.0],[1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
cmap_list_gs_3  = [[0.1, 0.1, 0.1],[0.5, 0.5, 0.5], [0.9, 0.9, 0.9]]

cmap_list_rgb_6  = [[1.0,0.0, 0.0],
					[1.0, 0.65, 0.0],
					[1.0, 1.0, 0.0], 
					[0.0, 1.0, 0.0],
					[0.0, 0.0, 1.0],
					[0.6, 0.0, 0.5]]
cmap_list_gs_6   = [[0.1, 0.1, 0.1],
					[0.26, 0.26, 0.26],
					[0.42, 0.42, 0.42],
					[0.58, 0.58, 0.58],
					[0.74, 0.74, 0.74],
					[0.9, 0.9, 0.9]]

cmap_rgb_3 = cls.LinearSegmentedColormap.from_list('custom_rgb_3', cmap_list_rgb_3, N=3)
cmap_gs_3  = cls.LinearSegmentedColormap.from_list('custom_gs_3', cmap_list_gs_3, N=3)

cmap_rgb_6 = cls.LinearSegmentedColormap.from_list('custom_rgb_6', cmap_list_rgb_6, N=6)
cmap_gs_6  = cls.LinearSegmentedColormap.from_list('custom_gs_6', cmap_list_gs_6, N=6)

# custom cmaps:
fire = [[1.0,0.0, 0.0],		# red
		[1.0, 0.65, 0.0],	# orange
		[1.0, 1.0, 0.5],	# bright yellow
		[0.8, 0.7, 0.7],	# grey
		[0.5, 0.4, 0.4],
		[0.2, 0.2, 0.2]]

cmap_fire = cls.LinearSegmentedColormap.from_list('fire', fire, N=6)


sunset = [[0.0, 0.0, 1.0],	# blue
		[0.5, 0.0, 0.4],	# purple
		[1.0,0.0, 0.0],		# red
		[0.8, 0.4, 0.0],	# orange
		[0.8, 0.7, 0.0], 	# yellow
		[0.8, 0.8, 1.0]]	# bright blue
		#[1.0, 1.0, 0.5]]	# bright yellow

cmap_sunset = cls.LinearSegmentedColormap.from_list('sunset', sunset, N=6)