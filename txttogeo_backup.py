"""
Created : 20 Aug 2016
Author : T. Devakumar
Descripption :
	From the points in a given text file generate a Gmsh .geo file by
	creating points and connecting them with lines & by creating a surface
"""

point = lambda n, x, y, z, d=0.1: "Point({0}) = {5} {1}, {2}, {3}, {4} {6};".format(n, x, y, z, d, '{', '}')
line = lambda n, p1, p2, nm=3: "Line({0}) = {4} {1}, {2} {5}; Transfinite Line {4} {0} {5} = {3} Using Progression 1;".format(n, p1, p2, nm, '{', '}')
#line = lambda n, p1, p2, nm=2: "Line({0}) = {4} {1}, {2} {5};".format(n, p1, p2, nm, '{', '}')

def main(fName):
	"""
	Print the Gmsh script to console
	"""
	import datetime

	print "// Gmsh file auto created on {0} \n\n ".format(datetime.date.today().ctime())

	with open(fName, 'r') as f:
		points = f.readlines()

	n = len(points)
	previous = 0
	first = False

	loop = []
	for i, p in enumerate(points):
		try :
			xy = p.strip()[1:-1].split(',')
			if i < n-1 :
				print 
				print point(i+1, xy[0].strip(), xy[1].strip(), 0)

				if not first: first = i+1

			if i > 0:
				if i < n-1 : 
					print line(previous, previous, i+1)
				else :
					print line(previous, previous, int(first))
				print 
				loop.append(str(previous))
			previous = i + 1
		except Exception as e:
			print "Could not create {0} th point {1} due to the error {2}".format(i, p, e)
	
	# Previous = index of the last line(airfoil) + 1 = n + 1

	# Create line loop of all points - call it Loop 1 (index : previous )
	print "Line Loop({0}) = {2} {1} {3};\n".format(previous, ', '.join(loop), '{', '}')

	# Call all the lines - "airfoil" (Physical entity definition)
	print "Physical Line(\"airfoil\") = {2} {1} {3};\n".format('', ', '.join(loop), '{', '}')

	# Create a boundary around the airfoil
	# circle about 20 chords away

	# Points for creating the boundary
	print point(previous, -20, 0, 0, 1.0)
	print point(previous + 1, 0, 20, 0, 1.0)

	# Creating a quadrant of a circle
	# If no of points on airfoil are even, point at (0, 0, 0) is already
	# created and its index is (n/2 + 1). Else origin/center of the circle is
	# to be created.

	# Index of the circle is : previous + 1
	if n%2 == 0:
		print "Circle({0}) = {4} {1} {2} {3} {5}\n".format(previous + 1, previous, n/2 + 1, previous + 1, '{', '}')
	else :
		print point(previous + 2, 0, 0, 0, 1.0)
		print "Circle({0}) = {4} {1} {2} {3} {5};\n".format(previous + 1, previous + 0, previous + 2, previous + 1, '{', '}')

	# Rotating this three times to get the rest of the circle
	# Index of the line/circle created earlier = previous + 1
	# The following loop will create 3 extra quadrants with indices :
	# previous + 2, previous + 3, previous + 4
	for i in ["Pi/2.0", "Pi", "3.0*Pi/2.0"]:
		print "Rotate {4} {0}, {1}, {2} {5} {4}\n \tDuplicata {4} Line {4} {3} {5}; {5}\n{5}\n".format('{0, 0, 1}', '{0, 0, 0}', i, previous + 1, '{', '}')

	loop2 = [str(i) for i in [previous + 1, previous + 2, previous + 3, previous + 4]]
	# Mesh size for the circle - definition
	print "Transfinite Line {2} {0} {3} = {1} Using Progression 1;\n".format( ', '.join(loop2), 10, '{', '}')	

	# Index of the line loop : previous + 5 : Loop 2
	print "Line Loop ({1}) = {2} {0} {3};\n".format(', '.join(loop2), previous + 5, '{', '}')	

	# Naming the boundary as farfiled
	# naming the free boundary
	print "Physical Line(\"farfield\") = {2} {1} {3};\n".format('', ', '.join(loop2), '{', '}')

	# Creating surface for the meshing
	# This is bound by the loop-1 : Airfoil & Loop2 : farfiled
	print "Plane Surface({0}) = {3} {1} {2} {4};" .format(previous + 6, previous, previous + 5, '{', '}')

if __name__ == "__main__":
	main('naca0012.txt')
