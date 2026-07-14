import boto3

s3 = boto3.client(
    "s3",
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name="ap-south-1"
)

response = s3.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])