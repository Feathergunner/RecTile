#!usr/bin/python
# -*- coding: utf-8 -*-import string

import matplotlib.pyplot as plt

import geometric_tilings as gt
	
def tilted_sqares():
	p1 = gt.Point (0, 0)
	p2 = gt.Point (0, 100)
	p3 = gt.Point (100,100)
	p4 = gt.Point (100, 0)
	
	rectangle = Structure([p1, p2, p3, p4])
	submat = [[0]]
	subpoints = [[[[0.8, 0.2, 0, 0],[0, 0.8, 0.2, 0],[0,0, 0.8, 0.2], [0.2, 0.0, 0.0, 0.8]]]]
	t = gt.Tiling(rectangle, submat, subpoints)
	t.draw()
	
def triangles():
	p1 = gt.Point(0,0)
	p2 = gt.Point(100, 0)
	p3 = gt.Point(50,86)
	
	triangle = Structure([p1, p2, p3])
	submat=[[0,0,0,0]]
	subpoints=[[[[1, 0, 0],[0.5, 0.5, 0],[0.5, 0, 0.5]],[[0.5, 0.5, 0],[0,1,0], [0, 0.5, 0.5]],[[0.5, 0, 0.5],[0, 0.5, 0.5],[0,0,1]],[[0, 0.5, 0.5],[0.5, 0., 0.5],[0.5, 0.5, 0]]]]
	t = gt.Tiling(triangle, submat, subpoints)
	t.draw(depth=5, filename='geometric_tilings/test_triangle_1.png')
	
def triangles_2():
	p1 = gt.Point(0,0)
	p2 = gt.Point(100, 0)
	p3 = gt.Point(50,86)
	
	eps = 0.05
	
	sp1 = [1,0,0]
	sp2 = [0.5-eps, 0.5-eps, 2*eps]
	sp3 = [0.5-eps, 2*eps, 0.5-eps]
	sp4 = [2*eps, 0.5-eps, 0.5-eps]
	sp5 = [0, 1, 0]
	sp6 = [0, 0, 1]
	
	triangle = Structure([p1, p2, p3])
	submat=[[0,0,0,0]]
	subpoints=[[
		[sp1, sp2, sp3],
		[sp2, sp5, sp4],
		[sp3, sp4, sp6],
		[sp4, sp3, sp2]]]
	t = gt.Tiling(triangle, submat, subpoints)
	t.draw(depth=5, filename='geometric_tilings/test_triangles_2_e'+str(eps)+'.png')
	
	
	subpoints=[[
		[sp1, sp2, sp3],
		[sp2, sp1, sp4],
		[sp3, sp4, sp1],
		[sp4, sp3, sp2]]]
	
def rectangles():
	p1 = gt.Point (0, 0)
	p2 = gt.Point (0, 100)
	p3 = gt.Point (100,100)
	p4 = gt.Point (100, 0)
	
	eps = -0.02
	
	rectangle = Structure([p1,p2,p3,p4])
	# 0: rectangle
	# 1: triangle
	# rectangle is split into four triangles (in the corners) and a rectangle in the center (rotated 45° to the initial rectangle)
	# triangle is split into two triangles and a rectangle
	submat = [[1,1,1,1,0],[1,1,0]]
	sp1 = [0.5-eps, 0.5-eps, eps, eps]
	sp2 = [eps, 0.5-eps, 0.5-eps, eps]
	sp3 = [eps, eps, 0.5-eps, 0.5-eps]
	sp4 = [0.5-eps, eps, eps, 0.5-eps]
	c1 = [1, 0, 0, 0]
	c2 = [0, 1, 0, 0]
	c3 = [0, 0, 1, 0]
	c4 = [0, 0, 0, 1]
	subpoints = [[ # substructures of rectangle:
		[sp1, sp2, c2], # first triangle
		[sp2, sp3, c3], # second triangle 
		[sp3, sp4, c4], # third triangle
		[sp4, sp1, c1], # fourth triangle
		[sp1, sp2, sp3, sp4] # center rectangle
		],[ # substructers of triangles:
		[[1, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5]], # first triangle
		[[0, 1, 0], [0.5, 0.5, 0], [0, 0.5, 0.5]], # second triangle
		[[0,0,1], [0, 0.5, 0.5], [0.5, 0.5, 0], [0.5, 0., 0.5]] # rectangle
		]]
	t = gt.Tiling(rectangle, submat, subpoints)
	t.draw(depth=7, filename='geometric_tilings/test_rect_triang_e'+str(eps)+'.png')
	
def snowflake():
	p1 = gt.Point(0,0)
	p2 = gt.Point(100, 0)
	p3 = gt.Point(50,86)
	
	triangle = Structure([p1, p2, p3])
	submat=[[1,1,1],[1,1]]
	subpoints=[[ # substructures of initial triangle:
	[[1/3, 2/3, 0],[2/3, 1/3, 0],[2/3, 2/3, -1/3]],
	[[0, 1/3, 2/3],[0, 2/3, 1/3],[-1/3, 2/3, 2/3]],
	[[2/3, 0, 1/3],[1/3, 0, 2/3],[2/3, -1/3, 2/3]]
	],[
	[[0, 1/3, 2/3],[0, 2/3, 1/3],[-1/3, 2/3, 2/3]],
	[[2/3, 0, 1/3],[1/3, 0, 2/3],[2/3, -1/3, 2/3]]
	]]
	t = gt.Tiling(triangle, submat, subpoints)
	t.draw(depth=5, filename='geometric_tilings/test_snowflake.png')
	
def chair_tiling():
	# p6 ------ p5
	# I         I
	# I    s8 - s3
	# I    I    I
	# s4 - s9   p4 - s2 - p3
	# I    I         I    I 
	# I    s5 - s6 - s7   I
	# I         I         I
	# p1 ------ s1 ------ p2
	
	p1 = gt.Point(0,0)
	p2 = gt.Point(100,0)
	p3 = gt.Point(100,50)
	p4 = gt.Point(50,50)
	p5 = gt.Point(50,100)
	p6 = gt.Point(0,100)
	
	chair = Structure([p1,p2,p3,p4,p5,p6])
	p1 = [1, 0, 0, 0, 0, 0]
	p2 = [0, 1, 0, 0, 0, 0]
	p3 = [0, 0, 1, 0, 0, 0]
	p4 = [0, 0, 0, 1, 0, 0]
	p5 = [0, 0, 0, 0, 1, 0]
	p6 = [0, 0, 0, 0, 0, 1]
	s1 = [0.5, 0.5, 0, 0, 0, 0]
	s2 = [0, 0, 0.5, 0.5, 0, 0]
	s3 = [0, 0, 0, 0.5, 0.5, 0]
	s4 = [0.5, 0, 0, 0, 0, 0.5]
	s5 = [0.5, 0, 0, 0.5, 0, 0]
	s6 = [0.5, 0, 0.5, 0, 0, 0]
	s7 = [0, 0.5, 0, 0.5, 0, 0]
	s8 = [0, 0, 0, 0.5, 0, 0.5]
	s9 = [0.5, 0, 0, 0, 0.5, 0]
	submat = [[0,0,0,0]]
	subpoints = [[
	[p1, s1, s6, s5, s9, s4],
	[p2, p3, s2, s7, s6, s1],
	[p6, s4, s9, s8, s3, p5],
	[s5, s7, s2, p4, s3, s8]
	]]
	t = gt.Tiling(chair, submat, subpoints)
	t.draw(depth=6, filename='geometric_tilings/chair_1.png')
	
def rhombs_1():
	a = 36.3*1.1
	b = 50*1.1
	p1 = gt.Point(b, 50-a)
	p2 = gt.Point(2*b, 50)
	p3 = gt.Point(b, 50+a)
	p4 = gt.Point(0, 50)
	
	c = (b**2 - a**2)/(2*a)
	d = ((a+c)*a)/(2*b)
	
	bigrhomb = Structure([p1, p2, p3, p4], state=0)
	
	eps = 0.1
	b_p1 = [1, 0, 0, 0]
	b_p2 = [0, 1, 0, 0]
	b_p3 = [0, 0, 1, 0]
	b_p4 = [0, 0, 0, 1]
	b_s1 = [1-(a-(a+c)/2)/(2*a), (b-d)/(2*b), (a-(a+c)/2)/(2*a), -(b-d)/(2*b)]
	b_s2 = [(a+c)/(4*a), d/(2*b), 1-((a+c)/(4*a)), -d/(2*b)]
	b_s3 = [(a+c)/(4*a), -d/(2*b), 1-((a+c)/(4*a)), d/(2*b)]
	b_s4 = [1-(a-(a+c)/2)/(2*a), -(b-d)/(2*b), (a-(a+c)/2)/(2*a), (b-d)/(2*b)]
	b_s5 = [1-((a-c)/(2*a)), 0, (a-c)/(2*a), 0]
	
	e = (a-c)/2
	f = (b-d)-((e*b)/a)
	smallrhomb = Structure([gt.Point(0,b-d), gt.Point(-e, 0), gt.Point(0,-b+d), gt.Point(e,0)], state=1)
	
	s_p1 = [1, 0, 0, 0]
	s_p2 = [0, 1, 0, 0]
	s_p3 = []
	s_p4 = [0, 0, 0, 1]
	s_s1 = [f/(2*(b-d)), 1, -f/(2*(b-d)), 0]
	s_s2 = [1/3, 0, 2/3, 0]
	s_s2 = [1-((2*e*b)/a+f)/(2*(b-d)), 0, ((2*e*b)/a+f)/(2*(b-d)), 0]
	s_s3 = [f/(2*(b-d)), 0, -f/(2*(b-d)), 1]
	s_s4 = [1-(e*b)/(a*(b-d)), 0, (e*b)/(a*(b-d)), 0]
		
	submat = [[0,0,0,1],[0,1,1]]
	#submat = [[0,0,0],[0,1,1]]
	subpoints = [
	[
	[b_s1, b_p2, b_s2, b_s5],
	[b_s2, b_p3, b_s3, b_s5],
	[b_s3, b_p4, b_s4, b_s5],
	[b_s4, s_p1, b_s1, b_s5]
	],[
	[s_s3, s_p1, s_s1, s_s4],
	[s_s1, s_p2, s_s2, s_s4],
	[s_s2, s_p4, s_s3, s_s4]
	]]
	t = gt.Tiling(bigrhomb, submat, subpoints)
	t.draw(depth=7, only_last_it=True, filename='geometric_tilings/rhombtest_2.png')
	
	
if __name__ == '__main__':
	rhombs_1()