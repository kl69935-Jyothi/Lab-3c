import boto3

bucket_name = 'jyothirmayee-s3-bucket-20250927'  

session = boto3.session.Session()
region = session.region_name or 'us-east-1'
s3 = session.client('s3', region_name=region)

if region == 'us-east-1':
    s3.create_bucket(Bucket=bucket_name)
else:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )

print(f'Bucket {bucket_name} created successfully in region {region}!')
