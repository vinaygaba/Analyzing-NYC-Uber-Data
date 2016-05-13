import os
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import subprocess


filepath = "data/yellow/yellow_tripdata_2015-04.csv";
testfilepath = "testdata.csv";
data = pd.read_csv(filepath, header = 0)
testdata = pd.read_csv(testfilepath, header = 0)
print len(data)

data['tip_bucket'] = pd.cut(data['tip_amount'], bins=[-1, 1, 5, 10, 20, 1000], labels=False)
labels = np.array('Bucket1 Bucket2 Bucket3 Bucket4 Bucket5'.split())
#data['tip_bucket'] = labels[data['tip_bucket']];
Y = data['tip_bucket'];
drop_features1 = ['tip_amount','tip_bucket','tpep_pickup_datetime', 'tpep_dropoff_datetime', 'store_and_fwd_flag']
drop_features2 = ['tip_amount','tpep_pickup_datetime', 'tpep_dropoff_datetime', 'store_and_fwd_flag']
data = data.drop(drop_features1, axis=1)
testdata = testdata.drop(drop_features2, axis=1)

data = data._get_numeric_data()
testdata = testdata._get_numeric_data()

dataX = data.as_matrix()
testdataX = testdata.as_matrix()
dataY = np.asarray(Y, dtype="|S6")

clf = tree.DecisionTreeClassifier()
clf = clf.fit(dataX, dataY)
output = clf.predict(testdataX)
print output;


with open("dt.dot", 'w') as f:
    export_graphviz(clf, out_file=f)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")
