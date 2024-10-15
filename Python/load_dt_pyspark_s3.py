import sys
from random import random
from operator import add

from pyspark.sql import SparkSession
import os
import pandas as pd
from pyspark import SparkFiles
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf


minio_endpoint = "89.169.153.72:9001"
aws_access_key_id = 'u0IafcyUUrIaDfFDkWcA'
aws_secret_access_key = 'Iy4LGM83pPHOTNn4H6fCWw19kiXQNVkkKGLYLfID'


if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    conf = (
    SparkConf()
    .setAppName("MY_APP") # replace with your desired name
    .set("spark.hadoop.fs.s3a.access.key", aws_access_key_id)
    .set("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key)
    .set("spark.hadoop.fs.s3a.endpoin", minio_endpoint)
    )

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    df = spark.read.format('delta').load('s3a://spark/data_frame_2.csv')
    df.show(5, truncate=False)





    #url_github_1 = 'https://raw.githubusercontent.com/geksogen/Apache_Spark_MLib_Research/refs/heads/master/Python/data_frame_1.csv'
    #url_github_2 = 'https://raw.githubusercontent.com/geksogen/Apache_Spark_MLib_Research/refs/heads/master/Python/data_frame_2.csv'

    #pd_df_1 = pd.read_csv(url_github_1)
    #pd_df_1.iteritems = pd_df_1.items

    #pd_df_2 = pd.read_csv(url_github_2)
    #pd_df_2.iteritems = pd_df_2.items

    #spark_df_1 = spark.createDataFrame(pd_df_1)
    #spark_df_2 = spark.createDataFrame(pd_df_2)

    #spark_df_1.limit(5).show()
    #spark_df_2.limit(5).show()

    #spark_df_1.join(spark_df_2,
    #               spark_df_1.u_id == spark_df_2.u_id,
    #               "inner").show(5)

    spark.stop()
