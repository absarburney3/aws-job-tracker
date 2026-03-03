import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('job-applications')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:787257787428:job-tracker-alerts'

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))

        item = {
            'applicationId': str(uuid.uuid4()),
            'dateApplied': body.get('dateApplied', datetime.now().strftime('%Y-%m-%d')),
            'company': body.get('company', ''),
            'jobTitle': body.get('jobTitle', ''),
            'status': body.get('status', 'Applied'),
            'notes': body.get('notes', '')
        }

        table.put_item(Item=item)

        # Send SNS alert only for Interview or Offer status
        if item['status'] in ['Interview', 'Offer']:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject=f"🎉 Job Update: {item['status']} at {item['company']}!",
                Message=f"""
Great news! Your application status update:

🏢 Company:   {item['company']}
💼 Job Title: {item['jobTitle']}
📊 Status:    {item['status']}
📅 Date:      {item['dateApplied']}
📝 Notes:     {item['notes']}

Keep going — you're doing great!
                """
            )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Application saved successfully!',
                'applicationId': item['applicationId']
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
