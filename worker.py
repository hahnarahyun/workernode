import boto3
def fibonacci(n):
    if n <= 0:
        print("incorect input")
    elif n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

sqs = boto3.resource('sqs', region_name='us-west-2')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='celery')

while True:
    for message in queue.receive_messages(MessageAttributeNames=['Fibonacci']):
        print('Hello')
        number_text='0'
        if message.message_attributes is not None:
            number = (message.message_attributes.get('Fibonacci').get('StringValue'))
            if number:
                number_text = '{0}'.format(number)
            number = int(number)
        print(fibonacci(number))
        print('{0}{1}'.format(message.body, number_text))
