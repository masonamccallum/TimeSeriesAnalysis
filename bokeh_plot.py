import pandas as pd
import stumpy
import numpy as np
import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Rect
from bokeh.models.tools import HoverTool


output_file('timeSeriesPlot_example.html')


df = pd.read_csv("USD.csv")
df['date'] = pd.to_datetime(df['date'])

def plotRectWindowLocation(df,idx, window_size):
    window_width = 1000*60*60*24*window_size
    window_height = 6000
    window_x = df['date'][idx]
    window_y = df['open_USD'][idx]+window_height/2
    return [window_x, window_y, window_width, window_height]

window_size=10
#matrix_profile = stumpy.stump(df['open_USD'], m=window_size)
#motif_idx = np.argsort(matrix_profile)[:,0][0]
#nearest_neighbor_idx = matrix_profile[motif_idx,1]


def getDateInterval(df, date, window_size):
    # Rectangle fix TODO: clean and orgainze
    dateIntervalStart=datetime.datetime.strptime('7-1-2020','%d-%m-%Y')
    delta = dateIntervalStart + datetime.timedelta(days=10)
    print(df[(df['date']>dateIntervalStart) & (df['date']<=delta)][['date','open_USD']])


source = ColumnDataSource(df)
p = figure(x_axis_type="datetime")
p.circle(x='date', y='open_USD',source=source,size=2, color='green')
p.line(x='date', y='open_USD',source=source,line_width=2)

#plotLoc = plotRectWindowLocation(df,motif_idx,window_size)
#plotLoc2 = plotRectWindowLocation(df,nearest_neighbor_idx,window_size)
#p.rect(x=plotLoc[0],y=plotLoc[1],width=plotLoc[2],height=plotLoc[3], width_units='data', fill_color="blue", fill_alpha=0.2)
#p.rect(x=plotLoc2[0],y=plotLoc2[1],width=plotLoc2[2],height=plotLoc2[3], width_units='data', fill_color="red", fill_alpha=0.2)

show(p)
