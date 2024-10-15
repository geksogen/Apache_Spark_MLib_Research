from s3fs import S3FileSystem
import pandas as pd

minio_endpoint = "http://89.169.153.72:9000/"
access_key_id = 'u0IafcyUUrIaDfFDkWcA'
secret_access_key = 'Iy4LGM83pPHOTNn4H6fCWw19kiXQNVkkKGLYLfID'


s3 = S3FileSystem(anon=False, endpoint_url=minio_endpoint,
                 key=access_key_id,
                 secret=secret_access_key,
                 use_ssl=False)

bucket_name = 'spark'

#object_list = s3.ls(f's3://{bucket_name}', detail=False)
#print(object_list)

ticker_string = 'data_frame_1.csv'
storage_options={
   'key': access_key_id,
   'secret': secret_access_key,
   'endpoint_url': minio_endpoint,
}
historical_data = pd.read_csv(f's3://{bucket_name}/{ticker_string}', storage_options=storage_options)
print(historical_data.tail(10))
