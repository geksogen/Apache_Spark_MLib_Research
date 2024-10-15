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

    url_github_1 = 'http://89.169.153.72:9001/api/v1/download-shared-object/aHR0cDovLzEyNy4wLjAuMTo5MDAwL3NwYXJrL2RhdGFfZnJhbWVfMS5jc3Y_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1LNFM5N0owU0tFS0FJTlRBR1oyWiUyRjIwMjQxMDE1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAxNVQwODI0NTBaJlgtQW16LUV4cGlyZXM9NDMxOTkmWC1BbXotU2VjdXJpdHktVG9rZW49ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmhZMk5sYzNOTFpYa2lPaUpMTkZNNU4wb3dVMHRGUzBGSlRsUkJSMW95V2lJc0ltVjRjQ0k2TVRjeU9UQXhPRFUxTUN3aWNHRnlaVzUwSWpvaWJXbHVhVzloWkcxcGJqRXlNeUo5LnpieWdWTlVveWw0NC15NUZMY1RzTXBLLXl6VEpVaDBrYUtRR2J1dnhaWUFEMDJQZGtfeG1XOGRRamlWdFZBVVltQTVkRXFzMEIyVk1lajh0SUVCTmFBJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZ2ZXJzaW9uSWQ9bnVsbCZYLUFtei1TaWduYXR1cmU9YjAyMDk3ZDVhZTIyMmUwNzA3NDgwZDI0YTAwYjExZmI0ZTgxNWU2ZGM0Yjg2ZWE5ZTUyYjEwYmRhY2ZjZWViMA'
    url_github_2 = 'http://89.169.153.72:9001/api/v1/download-shared-object/aHR0cDovLzEyNy4wLjAuMTo5MDAwL3NwYXJrL2RhdGFfZnJhbWVfMS5jc3Y_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1LNFM5N0owU0tFS0FJTlRBR1oyWiUyRjIwMjQxMDE1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAxNVQwODI0NTBaJlgtQW16LUV4cGlyZXM9NDMxOTkmWC1BbXotU2VjdXJpdHktVG9rZW49ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmhZMk5sYzNOTFpYa2lPaUpMTkZNNU4wb3dVMHRGUzBGSlRsUkJSMW95V2lJc0ltVjRjQ0k2TVRjeU9UQXhPRFUxTUN3aWNHRnlaVzUwSWpvaWJXbHVhVzloWkcxcGJqRXlNeUo5LnpieWdWTlVveWw0NC15NUZMY1RzTXBLLXl6VEpVaDBrYUtRR2J1dnhaWUFEMDJQZGtfeG1XOGRRamlWdFZBVVltQTVkRXFzMEIyVk1lajh0SUVCTmFBJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZ2ZXJzaW9uSWQ9bnVsbCZYLUFtei1TaWduYXR1cmU9YjAyMDk3ZDVhZTIyMmUwNzA3NDgwZDI0YTAwYjExZmI0ZTgxNWU2ZGM0Yjg2ZWE5ZTUyYjEwYmRhY2ZjZWViMA'

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
