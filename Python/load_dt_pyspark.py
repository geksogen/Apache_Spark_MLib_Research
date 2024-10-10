import sys
from random import random
from operator import add

from pyspark.sql import SparkSession
import os

current_dir = os.path.dirname(__file__)
relative_path = "data_frame_1.csv"
absolute_file_path = os.path.join(current_dir, relative_path)

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession\
        .builder\
        .appName("Load two CSV")\
        .getOrCreate()

    print(absolute_file_path)
    # Load DATA from csv
    #df_sp_1 = spark.read.options(inferSchema='True',delimiter=',') \
    #                        .csv("./data_frame_1.csv")
    #
    #df_sp_2 = spark.read.options(inferSchema='True',delimiter=',') \
    #                        .csv("./data_frame_2.csv")

    spark.stop()
