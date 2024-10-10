import sys
from random import random
from operator import add

from pyspark.sql import SparkSession
import os

current_dir = os.path.dirname(__file__)
relative_path = "data_frame_1.csv"
absolute_file_path = os.path.join(current_dir, relative_path)
petch = "file://data_frame_1.csv"

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession\
        .builder\
        .appName("Load two CSV")\
        .getOrCreate()


    # Load DATA from csv
    #df_sp_1 = spark.read.csv(header=True, inferSchema=True, path=petch)
    #df = spark.read.format("csv").option("header", "true").load("file:///home/sp-user/data_frame_1.csv")
    df = spark.read.csv('file:///home/sp-user/*.csv')
    df.show()
    spark.stop()
