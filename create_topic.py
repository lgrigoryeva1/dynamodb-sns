import boto3

sns = boto3.client('sns')
response = sns.create_topic(Name='Topic-name')

print(response)