#! /usr/bin/env python3
import boto3
import time
def fibonacci(n):
    if n <= 0:
        print("incorect input")
    elif n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

sqs = boto3.resource('sqs', region_name='us-west-1')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='Worker-Queue')

if __name__ == "__main__":
    count = 0
    while True:
        count = 1 + count
        print("while loop: ", count)
        for message in queue.receive_messages(MessageAttributeNames=['All'], MaxNumberOfMessages=1):
            print("processing message on sqs")
            number_text='0'
            if message.message_attributes is not None:
                number = (message.message_attributes.get('Fibonacci').get('StringValue'))
                if number:
                    number_text = '{0}'.format(number)
                number = int(number)
            print(fibonacci(number))
            print('{0}{1}'.format(message.body, number_text))
            print('deleting message', count)
            message.delete()
        time.sleep(5)