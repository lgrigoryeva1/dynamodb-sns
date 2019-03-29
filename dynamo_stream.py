import boto3

client = boto3.client('dynamodbstreams')

response = client.describe_stream(
    StreamArn='TABLE STREAM ARN'
)

shard_list = response.get('StreamDescription').get('Shards')
for item in shard_list:
    print(item)
