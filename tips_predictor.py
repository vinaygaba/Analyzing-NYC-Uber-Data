import os
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier


filepath = "data/yellow/yellow_tripdata_2015-04.csv";
data = pd.read_csv(filepath, header = 0)
print len(data)

data['tip_bucket'] = pd.cut(data['tip_amount'], bins=[-1, 1, 5, 10, 20, 1000], labels=False)
labels = np.array('Bucket1 Bucket2 Bucket3 Bucket4 Bucket5'.split())
#data['tip_bucket'] = labels[data['tip_bucket']];
Y = data['tip_bucket'];
drop_features = ['tip_amount','tip_bucket','tpep_pickup_datetime', 'tpep_dropoff_datetime', 'store_and_fwd_flag']
data = data.drop(drop_features, axis=1)

dataX = data.as_matrix()
dataY = np.asarray(Y, dtype="|S6")

clf = tree.DecisionTreeClassifier()
clf = clf.fit(dataX, dataY)
