#!usr/bin/python
# -*- coding: utf-8 -*-import string

import matplotlib.pyplot as plt
import queue

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __mul__(self, scale):
		return Point(self.x*scale, self.y*scale)
		
	def __rmul__(self, scale):
		return self.__mul__(scale)
		
	def __div__(self, div):
		return self.__mul__(1/div)
		
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
		
	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)
	
	def __str__(self):
		return "("+str(self.x)+", "+str(self.y)+")"
	
	def draw_line_to(self, other):
		plt.plot([self.x, other.x], [self.y, other.y], color='black')
		pass

class Structure:
	def __init__(self, points, state=0, color='black', fill=None):
		'''
		Args:
			points: a list of Point
				contains the points that define this structure, in order.
			state: int
				an optional parameter that may identify the class or state of this structure
			color: a color
				defines the line-color for plotting this strucuture. If None, no lines are plotted.
			fill: a color
				defines the fill-color for plotting this structure. If None, interior of structure is transparent.
		'''
		self.points = points
		self.state = state
		
		self.color = color
		self.fill = fill
		
	def __str__(self):
		return '--'.join([str(p) for p in self.points])
	
	def draw(self):
		xs = self.x() + [self.points[0].x]
		ys = self.y() + [self.points[0].y]
		if not self.fill == None:
			plt.fill(xs, ys, color=self.fill)
		if not self.color == None:
			plt.plot(xs, ys, color=self.color, linewidth=0.2)
	
	def x(self):
		return [p.x for p in self.points]
	
	def y(self):
		return [p.y for p in self.points]
	
class Tiling:
	def __init__(self, initial_struct, substitutuin_matrix, substitution_points):
		'''
		Args:
			#n: int
			#	The number_of_structs, i.e. the total number of different structures that appear in this tiling
			initial_struct: Structure
				The initial structure with which the recursice tiling process is started
			substitutuin_matrix: list of lists of integers
				substitutuin_matrix[i] specifies the indices of the substructures that make the tiling of structure i
			substitution_points: a 2d-list (n times n) of matrices of floats
				substitution_points[i][j] defines the linear combinations to construct the points of sub-structure j from the points of base-structure i
		'''
		#self.n = n
		self.initial_struct = initial_struct
		self.substitutuin_matrix = substitutuin_matrix
		self.substitution_points = substitution_points
		#self.maxdepth = maxdepth
	
	def draw(self, depth=10, show=True, filename=None, only_last_it=False):
		'''
		depth: int
			the number of recursive tiling steps
		'''
		q_structs = queue.Queue()
		q_structs.put([self.initial_struct, 0])
		while not q_structs.empty():
			[current_struct, current_depth] = q_structs.get()
			if current_depth < depth:
				#print("current depth", current_depth)
				#print("current struct: "+str(current_struct))
				# draw structure:
				if not only_last_it or current_depth == depth-1:
					current_struct.draw()
				# construct child structures:
				current_struct_id = current_struct.state
				for child_id in range(len(self.substitutuin_matrix[current_struct_id])):#:
					#print ("Consider child "+str(child_id))
					child_points = []
					for child_point_id in range(len(self.substitution_points[current_struct_id][child_id])):
						scales = self.substitution_points[current_struct_id][child_id][child_point_id]
						child_point = Point(0,0)
						for i in range(len(current_struct.points)):
							c_p_i = current_struct.points[i]*scales[i]
							child_point += c_p_i
						#print ("\tadd point "+str(child_point))
						child_points.append(child_point)
					child_state = self.substitutuin_matrix[current_struct_id][child_id]
					q_structs.put([Structure(child_points, state=child_state), current_depth+1])
					
		
		plt.axis('off')
		plt.xticks(range(-5, 105))
		plt.yticks(range(-5, 105))
		if not filename==None:
			plt.savefig(filename, dpi=300)
		if show:
			plt.show()
