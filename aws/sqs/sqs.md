# install 
    pip install boto3

# SQS Client

    import boto3

    sqs = boto3.client('sqs', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    queue_url = '<form_aws_sqs_dashboard>'

# send sms to SQS

def send_sqs_data(message):
    message_data = {
        'MessageBody': message,
        'MessageAttributes': {
            'Author': {
                'StringValue': '<any_meaningful_name>',
                'DataType': 'String'
            }
        }
    }

    # Send the message to the SQS queue
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_data['MessageBody'], MessageAttributes=message_data['MessageAttributes'])

    # Print the response
    print("MessageId:", response['MessageId'])