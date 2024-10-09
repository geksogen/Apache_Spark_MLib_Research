import pandas as pd
import random
from random import sample
import hashlib

SIZE_DATAFRAME = 1000000
list_index = sample(range(1, SIZE_DATAFRAME + 1), SIZE_DATAFRAME)
list_value_df_2 = ['IT', 'Logistic', 'Legal']

def rowValue(x, y):
    return {'u_id': x,
            'value_1': y
            }

def data_generator_1():
    temp_list = []
    for i in range(0, SIZE_DATAFRAME):
        temp_requestType = random.choice(list_index)
        value = hashlib.sha256((str(i)).encode('UTF-8')).hexdigest()

        temp_list.append(rowValue(temp_requestType, value))

    pd_dataframe_1 = pd.DataFrame(temp_list)
    pd_dataframe_1.info()
    pd_dataframe_1.to_csv('data_frame_1.csv', index=False)
    return pd_dataframe_1

def data_generator_2():
    temp_list = []
    for i in range(0, SIZE_DATAFRAME):
        temp_requestType = random.choice(list_index)
        value = random.choice(list_value_df_2)

        temp_list.append(rowValue(temp_requestType, value))

    pd_dataframe_2 = pd.DataFrame(temp_list)
    pd_dataframe_2.info()
    pd_dataframe_2.to_csv('data_frame_2.csv', index=False)
    return pd_dataframe_2

df_1 = data_generator_1()
df_2 = data_generator_2()

print(df_1)
print(df_2)

