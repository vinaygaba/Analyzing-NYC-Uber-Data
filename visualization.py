import os
import sys
import re
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
from ggplot import *



filepath = "path_to_file.csv";

dataX = pd.read_csv(filepath, header = 0)

#dataX = dataX[['pickup_longitude','pickup_latitude']]

#dataX= dataX.round({'pickup_longitude': 4, 'pickup_latitude': 4})




#Used to create the scatter plot of trip pickups which entually recreates
# the map
ggsave('test.png',
ggplot(aes(x='pickup_longitude',y='pickup_latitude'),data=dataX) + \
geom_point( size = 0.2,alpha=0.2) + \
xlim(-74.2, -73.7) + ylim(40.56, 40.93)
 )


#For creating a series of image that were eventually merged to create the
#animated gif
#Used to create the animated gif without the airport in the corner
for i in range(0,24):
    ggsave(
        'taxi%02i.png' % i,
        ggplot(
            aes(x='long',y='lat',color='dist'),data = dataX[dataX.hour==i].reset_index()
        ) + geom_point(size = 0.2,alpha=0.2) + xlim(-74.018, -73.95) + ylim(40.7, 40.8) \
          + ggtitle('NYC taxi pickups %02i:00' % i) \
          + theme(axis_text_x=element_text(angle=90))
    )


#For creating a series of image that were eventually merged to create the
#animated gif
#Used to create the animated gif with the airport in the corner
for i in range(0,24):
    ggsave(
        'taxi%02i.png' % i,
        ggplot(
            aes(x='long',y='lat',color='dist'),data = dataX[dataX.hour==i].reset_index()
        ) + geom_point(size = 0.2,alpha=0.2) + xlim(-74.025, -73.78) + ylim(40.64, 40.9) \
          + ggtitle('NYC taxi pickups %02i:00' % i) \
          + theme(axis_text_x=element_text(angle=90))
    )



#matplotlib code that we eventually never used

#pd.options.display.mpl_style = 'default' #Better Styling
#new_style = {'grid': False} #Remove grid
#matplotlib.rc('axes', **new_style)
#from matplotlib import rcParams
#rcParams['figure.figsize'] = (17.5, 17) #Size of figure
#rcParams['figure.dpi'] = 250
#P = plt.subplot()
#plt.subplot().set_axis_bgcolor('black') #Background Color
#P = data.plot(kind='scatter', x='pickup_longitude', y='pickup_latitude',color='white',xlim=(-74.06,-73.77),ylim=(40.61, 40.91),s=.02,alpha=.6)



#print ggplot(data,aes(x='pickup_longitude',y='pickup_latitude')) + \
#    geom_point(size=0.01, alpha=0.2) + xlim(-74.025, -73.78) + ylim(40.64, 40.9)
