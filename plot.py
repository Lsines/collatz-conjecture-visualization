"""
import 
outputfile -- html
make figure
plor
and output

"""
import new_one
from bokeh.plotting import figure, output_file,show

pairs = new_one.collage_pairs(100000)
x = [x for x in pairs.keys()]
y= [y for y in pairs.values()]

# pairs = new_one.collage_pairs(1000)
# x1 = [x1 for x1 in pairs.keys()]
# y1 = [y1 for y1 in pairs.values()]


output_file("bokeh.html")

p = figure(title = "first",x_axis_label = 'x',y_axis_label = "y")


p.circle(x,y)
# p.line(x,y)
show(p)


