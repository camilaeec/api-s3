import boto3
import json
import base64

def lambda_handler(event, context):
    body = json.loads(event['body'])
    bucket_name = body['bucket_name']
    file_path = body['file_path']
    file_content = base64.b64decode(body['file_content'])
    
    s3 = boto3.client('s3')
    try:
        s3.put_object(
            Bucket=bucket_name,
            Key=file_path,
            Body=file_content
        )
        return {
            'statusCode': 200,
            'body': json.dumps(f'Archivo subido a {bucket_name}/{file_path}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
