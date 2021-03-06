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

sunset1 = [[0.0, 0.0, 1.0],	# blue
		[0.5, 0.0, 0.4],	# purple
		[1.0,0.0, 0.0],		# red
		[0.8, 0.2, 0.0],	# orange1
		[0.8, 0.5, 0.0], 	# orange2
		[0.8, 0.8, 0.0]]	# yellow
		#[1.0, 1.0, 0.5]]	# bright yellow

cmap_sunset1 = cls.LinearSegmentedColormap.from_list('sunset1', sunset1, N=6)

dark = [[0.0, 0.0, 0.0],
		[0.0, 0.8, 0.0],
		[0.0, 0.0, 0.8],
		[0.8, 0.0, 0.0],
		[0.9, 0.9, 0.0]]

cmap_dark = cls.LinearSegmentedColormap.from_list('dark', dark, N=5)

dark2 = [[0.0, 0.0, 0.8],
		[0.0, 0.0, 0.0],
		[0.0, 0.0, 0.8],
		[1.0, 0.0, 0.0],
		[0.9, 0.9, 0.0]]

cmap_dark2 = cls.LinearSegmentedColormap.from_list('dark', dark2, N=5)

gold = [[0.2, 0.0, 0.3],	# dark blueish purple
		[1.0, 0.85, 0.0], # golden yellow
		[1.0, 0.2, 0.0]]  # reddish orange

cmap_gold = cls.LinearSegmentedColormap.from_list('gold', gold, N=3)

gold2 = [[1.0, 0.85, 0.0], # golden yellow
		[0.2, 0.0, 0.3],	# dark blueish purple
		[1.0, 0.2, 0.0]]  # reddish orange

cmap_gold2 = cls.LinearSegmentedColormap.from_list('gold2', gold2, N=3)

clouds = [[0.0, 0.0, 0.9],
		[0.4, 0.4, 1.0],
		[0.9, 0.9, 1.0],
		[1.0, 1.0, 1.0]]

cmap_clouds = cls.LinearSegmentedColormap.from_list('clouds', clouds, N=4)
