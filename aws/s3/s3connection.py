import boto3

s3 = boto3.client(
    "s3",
    aws_access_key_id="AKIAWVLQESP5PBVC7TOB",
    aws_secret_access_key="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",
    region_name="ap-south-1"
)

response = s3.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])