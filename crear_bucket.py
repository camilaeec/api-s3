import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    bucket_name = body['bucket_name']
    
    s3 = boto3.client('s3')
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'us-east-2'}
        )
        return {
            'statusCode': 200,
            'body': json.dumps(f'Bucket {bucket_name} creado exitosamente')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
