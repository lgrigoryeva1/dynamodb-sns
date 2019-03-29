import boto3

client = boto3.client('dynamodbstreams')

response = client.get_shard_iterator(
    StreamArn='TABLE STREAM AR',
    ShardId='SHARD ID',
    ShardIteratorType='TRIM_HORIZON',
)


print(response.get('ShardIterator'))