import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('job-applications')

def lambda_handler(event, context):
    try:
        params = event.get('queryStringParameters') or {}
        status_filter = params.get('status')
        
        if status_filter:
            response = table.query(
                IndexName='status-dateApplied-index',
                KeyConditionExpression=boto3.dynamodb.conditions.Key('status').eq(status_filter)
            )
        else:
            response = table.scan()
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(response['Items'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
