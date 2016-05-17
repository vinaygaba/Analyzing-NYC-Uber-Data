import os
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt



# Path for spark source folder
os.environ['SPARK_HOME']="/Users/vinaygaba/Downloads/spark-1.6.0-bin-hadoop2.6/"

# Append pyspark  to Python Path
sys.path.append("/Users/vinaygaba/Downloads/spark-1.6.0-bin-hadoop2.6/python")

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext


from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

sc = SparkContext("local", "Analysis of NYC Cab Rides")
sql_sc = SQLContext(sc)

pandas_df = pd.read_csv('filepath_to_csv.csv')  # assuming the file contains a header
s_df = sql_sc.createDataFrame(pandas_df)

#There are two ways in which you can run spark queries

#First is by using DataFrame operations like the ones you see below
groupByDate = s_df.groupBy(dayofmonth('tpep_pickup_datetime')).count();
count = groupByDate.select("count").toPandas();
count = count.values.tolist();
date = groupByDate.select(dayofmonth('tpep_pickup_datetime').alias('year')).toPandas();

#The second option is to run SQL queries itself. This can be done in the
#following manner

dataframe = sqlContext.sql("Enter query from queries.txt");
print dataframe;


#We used the second option for our analysis and ran each query one by one




# plt.plot(count);
# plt.xticks(range(len(date)), date);
# plt.show();
