import pandas as pd
import stumpy
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

output_file('timeSeriesPlot_example.html')


df = pd.read_csv("USD.csv")
df['date'] = pd.to_datetime(df['date'])

window_size=500
matrix_profile = stumpy.stump(df['open_USD'], m=window_size)
print(matrix_profile.shape)
print(matrix_profile)

source = ColumnDataSource(df)

p = figure(x_axis_type="datetime")
p.circle(x='date', y='open_USD',source=source,size=2, color='green')
p.line(x='date', y='open_USD',source=source,line_width=2)

#show(p)


'''
x=[1,3,4,6]
y=[2,4,6,8]

p = figure()
p.circle(x,y,size=10, color='red', legend='circle')
p.line(x,y,color='blue', legend='line')
p.triangle(y,x,color='gold', size=10, legend='triangle')
p.legend.click_policy='hide'

show(p)
'''
