This documentation is marked with Markdown. I will use rst
in the near future.
This submission is still very experimental. Another version with
better documentation will follow.

# Kopi

## Objective
- To create publication quality graph in pdf format using CSON (CoffeeScript-Object-Notation)
- To generate high fidelity pdf file that is
	- readily editable using Adobe Illustrator or equivalent tool, and
	- readily insertable to my high resolution Keynote slides.
- Originally, I output the graph to postscript (ps), but gave it up to pdf. (Postscript is too old)
- Although it is not the "open source spirit", I would like to use the font that is supported by Adobe.

## Background and usage
-	I have used matlibplot.pyplot and R for my papers for years, but my students and colleagues can not cope with my unfriendly habit.

-	In some occasion, I would like to edit my graph using Adobe Illustrator for artistic rendering.

- To persuade friend to use what I use, I need something that is super easy. That is, all you need to do is :
	- import kopi as kp
	- kp.plot(X,Y) #or
	- kp.plot(X,Y, coffee = "myspecialflavour.cson")
- The properties of the graph, graphs or figures are controlled by the accompanying cson file.
-

## Status
- So far, it is still experimental. I haven't make sure all modules are stable.
- Nevertheless, I have used it to create some figures for my publication. In my field, the publisher still insist on .ps file, so I have to convert it using, e.g. Illustrator, and increase the file size.

## Example
### Basic:
import numpy as np
import kopi as k
x = [1,2,3]
y = [1,4,9]
k.plot(x,y)

or

x = np.array(x)

y = x**2

k.plot(x,y)

### To plot multiple curve in one graph, put the numpy array in list.
k.plot([x, x, x], [x, y, x**3])

### To plot multiple plot in one graph use mplot. It is a little tricky. Bundle the list in a global list
k.mplot([

	[x,y],# 1st plot

	[x,x**3],# 2nd plot

	[[x,x],[y,x**3]]# 3rd plot with two curves
	])

### coffee, latte, sugar and milk:
coffee:	The cson file to adjust the the graph properties in a single plot.

latte:	The cson file to adjust the appearance of multiple plots in a single page (or figure)

sugar : The dictionary to overwrite the content in
		coffee (plot style .cson file )

milk :	The dictionary to overwrite the content in
		latte (multi plot style .cson file )
