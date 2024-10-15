import sys
from random import random
from operator import add

from pyspark.sql import SparkSession

minio_endpoint = "http://89.169.153.72:9000/"
access_key_id = 'u0IafcyUUrIaDfFDkWcA'
secret_access_key = 'Iy4LGM83pPHOTNn4H6fCWw19kiXQNVkkKGLYLfID'

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession.builder \
    .appName("Minio test") \
    .config("spark.hadoop.fs.s3a.endpoint", minio_endpoint) \
    .config("spark.hadoop.fs.s3a.access.key", access_key_id) \
    .config("spark.hadoop.fs.s3a.secret.key", secret_access_key) \
    .getOrCreate()

    df_spark = spark.read.csv("s3a://spark/data_frame_1.csv")
    df_spark.show(5, truncate=False)

    spark.stop()
