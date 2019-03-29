import boto3
import json


client = boto3.client('dynamodbstreams')

response = client.get_records(
    ShardIterator='SHARD ITERATOR'
)

records = response.get('Records')
for record in records:
    dynamodb = record.get('dynamodb')
    print(dynamodb)
    