import pandas as pd
import random
import hashlib

requestTypes = ["type1","type2","type3","type"]

def rowValue(x, y):
    return {'request_type': x,
            'u_id': y
            }

def data_generator():
    temp_list = []
    for i in range(0, 5):
        temp_requestType = random.choice(requestTypes)
        uid_value = hashlib.sha256((str(i)).encode('UTF-8')).hexdigest()

        temp_list.append(rowValue(temp_requestType, uid_value))

    return pd.DataFrame(temp_list)

df = data_generator()
print(df)
