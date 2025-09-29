
import boto3

s3 = boto3.client('s3')
bucket_name = 'jyothirmayee-s3-bucket-20250927'
file_name = 'myfile.txt'

s3.delete_object(Bucket=bucket_name, Key=file_name)
print(f'File {file_name} deleted successfully!')
