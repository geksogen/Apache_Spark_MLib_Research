import sys
import random
from operator import add
import pandas as pd
from pyspark.sql import SparkSession
from random import sample
import hashlib



if __name__ == "__main__":
    """
        Usage:
    """
    spark = SparkSession\
        .builder\
        .appName("Join two dataframe")\
        .getOrCreate()
    # ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN
    spark.sparkContext.setLogLevel('WARN')

    SIZE_DATAFRAME = 100000
    list_index = sample(range(1, SIZE_DATAFRAME + 1), SIZE_DATAFRAME)
    list_value_df_2 = ['IT', 'Logistic', 'Legal']

    def rowValue(x, y):
        return {'u_id': x,
                'value_1': y
                }

    temp_list_1 = []
    temp_list_2 = []

    for i in range(0, SIZE_DATAFRAME):
        temp_requestType = random.choice(list_index)
        value_1 = hashlib.sha256((str(i)).encode('UTF-8')).hexdigest()
        value_2 = random.choice(list_value_df_2)

        temp_list_1.append(rowValue(temp_requestType, value_1))
        temp_list_2.append(rowValue(temp_requestType, value_2))

        pd_dataframe_1 = pd.DataFrame(temp_list_1)
        pd_dataframe_2 = pd.DataFrame(temp_list_2)



    pd_dataframe_1.iteritems = pd_dataframe_1.items
    pd_dataframe_2.iteritems = pd_dataframe_2.items

    # Create Spark datafram's
    sparkDF_1=spark.createDataFrame(pd_dataframe_1)
    sparkDF_2=spark.createDataFrame(pd_dataframe_2)

    sparkDF_1.show(5)
    sparkDF_2.show(5)

    # Inner join sparkDF_1 + sparkDF_2
    sparkDF_1.join(sparkDF_2,
               sparkDF_1.u_id == sparkDF_2.u_id,
               "inner").show(5)

    spark.stop()
