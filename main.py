import boto3

# Create a Boto3 S3 client
s3_client = boto3.client('s3')

# Specify the bucket and object key
bucket_name = 'avs-sagemaker-test-bucket'
object_key = 'data/mobile_price_classification/test-V-1.csv'

# Download the object from S3
s3_client.download_file(bucket_name, object_key, 'test-V-1.csv')
print("File downloaded successfully.")
import pandas as pd
print(pd.read_csv("test-V-1.csv"))
