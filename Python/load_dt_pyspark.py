import sys
from random import random
from operator import add

from pyspark.sql import SparkSession
import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp
from pyspark import SparkFiles

current_dir = os.path.dirname(__file__)
relative_path = "data_frame_1.csv"
absolute_file_path = os.path.join(current_dir, relative_path)

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    #spark = SparkSession\
    #    .builder\
    #    .appName("Load two CSV")\
    #    .getOrCreate()

    # Create a SparkConf object to configure the application
    conf = SparkConf().setAppName("SparkContextExample").setMaster("spark://62.84.125.93:7077")

    # Create a SparkContext object
    sc = SparkContext(conf=conf)

    data_file_https_url = "https://gist.githubusercontent.com/aakashjainiitg/dbb668c58839d68d7903f508bf55043c/raw/1feec07802b4f53aceac450fa1aee5a87d9276e0/cities_data_bank.csv"
    sc.addFile(data_file_https_url)
    filePath = 'file://' + SparkFiles.get('cities_data_bank.csv')
    citiesDf = sc.textFile(filePath)
    citiesDf.collect(1,10)

    sc.stop()
