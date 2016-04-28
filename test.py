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

sc = SparkContext("local", "Wiki Scraper")
sql_sc = SQLContext(sc)

pandas_df = pd.read_csv('uber_data.csv')  # assuming the file contains a header
s_df = sql_sc.createDataFrame(pandas_df)


groupByDate = s_df.groupBy("Date").count();
#count = groupByDate.select("count").rdd.map(lambda l : l ).collect();
#date = groupByDate.select("Date").rdd.map(lambda l : l ).collect();

count = groupByDate.select("count").toPandas();
count = count.values.tolist();
date = groupByDate.select("Date").toPandas();
#date = date.values.tolist();
date = date["Date"];
date = date.str[0:5];
print date;

plt.plot(count);
plt.xticks(range(len(date)), date);
plt.show();
