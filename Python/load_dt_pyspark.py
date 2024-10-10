import sys
from random import random
from operator import add

from pyspark.sql import SparkSession
import os
import pandas as pd
from pyspark import SparkFiles

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
    #df = spark.read.csv('https://raw.githubusercontent.com/geksogen/Apache_Spark_MLib_Research/refs/heads/master/Python/data_frame_1.csv')
    #df.show(10)

    url_github_1 = 'https://raw.githubusercontent.com/geksogen/Apache_Spark_MLib_Research/refs/heads/master/Python/data_frame_1.csv'
    url_github_2 = 'https://raw.githubusercontent.com/geksogen/Apache_Spark_MLib_Research/refs/heads/master/Python/data_frame_2.csv'

    pd_df_1 = pd.read_csv(url_github_1)
    pd_df_1.iteritems = pd_df_1.items

    pd_df_2 = pd.read_csv(url_github_2)
    pd_df_2.iteritems = pd_df_2.items

    spark_df_1 = spark.createDataFrame(pd_df_1)
    spark_df_2 = spark.createDataFrame(pd_df_2)

    spark_df_1.limit(5).show()
    spark_df_2.limit(5).show()

    spark.stop()
