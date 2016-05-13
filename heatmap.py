import os
import sys
import re
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
from ggplot import *
from ggplot import diamonds


filepath = "data/yellow/yellow_tripdata_2015-04.csv";
#filepath = "data/yellow/small_data.csv";
dataX = pd.read_csv(filepath, header = 0)

dataX = dataX[['pickup_longitude','pickup_latitude']]

dataX= dataX.round({'pickup_longitude': 4, 'pickup_latitude': 4})


#pd.options.display.mpl_style = 'default' #Better Styling
#new_style = {'grid': False} #Remove grid
#matplotlib.rc('axes', **new_style)
#from matplotlib import rcParams
#rcParams['figure.figsize'] = (17.5, 17) #Size of figure
#rcParams['figure.dpi'] = 250
#P = plt.subplot()
#plt.subplot().set_axis_bgcolor('black') #Background Color
#P = data.plot(kind='scatter', x='pickup_longitude', y='pickup_latitude',color='white',xlim=(-74.06,-73.77),ylim=(40.61, 40.91),s=.02,alpha=.6)

myplot = ggplot(aes(x='pickup_longitude',y='pickup_latitude'),data=dataX)

ggsave('test.png',
myplot + \
geom_point( size = 0.2,alpha=0.2,color='white') + \
theme(plot_background = element_rect(fill = 'black', colour = 'black')) + \
xlim(-74.2, -73.7) + ylim(40.56, 40.93)
  )




#print ggplot(data,aes(x='pickup_longitude',y='pickup_latitude')) + \
#    geom_point(size=0.01, alpha=0.2) + xlim(-74.025, -73.78) + ylim(40.64, 40.9)
