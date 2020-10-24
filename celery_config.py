import os
#env vars used:
#AWS_REGION: specify which region you want to access SQS from.
#SQS_URL: The url of the sqs queue to listen for. The AWS keys are picked up
#         from the environment vars that we'll add later while running the worker.
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'region': os.getenv('AWS_REGION','us-east-1'),
    'predefined_queues': {
        'default': {
            'url': os.getenv('SQS_URL')
        }
    }
}

broker_url="sqs://"
result_backend = 'rpc://'
enable_utc = True