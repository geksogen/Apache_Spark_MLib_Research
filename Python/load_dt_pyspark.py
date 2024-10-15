import sys
from random import random
from operator import add

from pyspark.sql import SparkSession
import os
import pandas as pd
from pyspark import SparkFiles
from s3fs import S3FileSystem


minio_endpoint = "http://89.169.153.72:9000/"
access_key_id = 'u0IafcyUUrIaDfFDkWcA'
secret_access_key = 'Iy4LGM83pPHOTNn4H6fCWw19kiXQNVkkKGLYLfID'

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession\
        .builder\
        .appName("Load two CSV")\
        .getOrCreate()

    bucket_name = 'spark'
    ticker_string_1 = 'data_frame_1.csv'
    ticker_string_2 = 'data_frame_2.csv'


    storage_options={
       'key': access_key_id,
       'secret': secret_access_key,
       'endpoint_url': minio_endpoint,
    }

    url_github_1 = pd.read_csv(f's3://{bucket_name}/{ticker_string_1}', storage_options=storage_options)
    url_github_2 = pd.read_csv(f's3://{bucket_name}/{ticker_string_2}', storage_options=storage_options)

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

    #spark_df_1.limit(5).show()
    #spark_df_2.limit(5).show()

    spark_df_1.join(spark_df_2,
                   spark_df_1.u_id == spark_df_2.u_id,
                   "inner").show(5)

    spark.stop()
