.PHONY : setenv
setenv :
	export SPARK_HOME=/Users/vinaygaba/Downloads/spark-1.6.0-bin-hadoop2.6/
	export PYTHONPATH=/usr/bin/python2.7
	export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.9-src.zip:$PYTHONPATH
