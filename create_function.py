import boto3

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')

env_variables = dict()

with open('lambda.zip', 'rb') as lambda_zip:
    zipped_code = lambda_zip.read()

role = iam_client.get_role(RoleName='LambdaBasicExecution')

lambda_client.create_function(
    FunctionName='myLambdaFunction',
    Runtime='python3.6',
    Role=role['Role']['Arn'],
    Handler='main.handler',
    Code=dict(ZipFile=zipped_code),
    Timeout=300,
    Environment=dict(Variables=env_variables),

)
