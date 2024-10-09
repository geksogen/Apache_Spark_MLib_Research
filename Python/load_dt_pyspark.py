import sys
from random import random
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession\
        .builder\
        .appName("Join two dataframe")\
        .getOrCreate()

    # Load DATA from csv
    df_sp_1 = spark.read.options(inferSchema='True',delimiter=',') \
                            .csv("./data_frame_1.csv")

    df_sp_2 = spark.read.options(inferSchema='True',delimiter=',') \
                            .csv("./data_frame_2.csv")

    df.printSchema()

    spark.stop()
