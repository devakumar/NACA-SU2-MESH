"""
Generate profile for a given naca airfoil series and saveit by the same name

Copyright (C) 2016 by Thammisetty Devakumar <deva.aerospace@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

def naca(profile,number):
	"""
		Generate NACA (profile) with (number) of points and write the results
		to naca(profile).dat
	"""
	from numpy import arange
	c = 1
	x = arange(0, c, number)

	max_thickness = 
	yt= [

def main():
	import os
	from argparse import ArgumentParser, RawDescriptionHelpFormatter
	from textwrap import dedent

	parser = ArgumentParser(\
			fmt_class 	= RawDescriptionHelpFormatter, \
			description = dedent('''\
				This is a python script to create profiles for NACA 4 and 5
				series airfoils. If no arguments are provided the default
				help is displayed'''),\
			epilog		= dedent('''\
				Examples :
					To generate profile for NACA 2412 with 200 points
						$ python {0} -p 2412 -n 200
				'''.format(os.path.basename(__file__))))
	parser.add_argument('-p', '--profile', type = str, default='2412'\
			help = 'Profile name e.g. 2412, default is NACA2412')
	parser.add_argument('-n', '--number', type = str, default = 200,\
			help = 'number of points on the airfoil default is 200')

	args = parser.parse_args()

	naca(args.profile,args.number)

if __name__ == "__main__":
    main()
