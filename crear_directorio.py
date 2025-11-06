import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    bucket_name = body['bucket_name']
    directory_name = body['directory_name']
    
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=bucket_name, Key=f"{directory_name}/")
        return {
            'statusCode': 200,
            'body': json.dumps(f'Directorio {directory_name} creado en {bucket_name}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
