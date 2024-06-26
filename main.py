import boto3

# Create a Boto3 S3 client
s3_client = boto3.client('s3')

# Specify the bucket and object key
bucket_name = 'avs-sagemaker-test-bucket'
object_key = 'data/mobile_price_classification/test-V-1.csv'

# Download the object from S3
s3_client.download_file(bucket_name, object_key, 'test-V-1.csv')
print("File downloaded successfully.")
print("This line is added")
import pandas as pd
df=pd.read_csv("test-V-1.csv")
print(df)
print("df.shape", df.shape)

print("now uploading the dataset to s3")
df['newcol']="Akshay Sawant"
df.to_csv("toupload.csv", index=False)
s3_client.upload_file("toupload.csv", bucket_name, "uploaded_from_ec2.csv")
print(df)
print(df.shape)
print("successfully uploaded to s3")
