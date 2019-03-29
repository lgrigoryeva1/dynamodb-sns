import json
import boto3


role_policy_document = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

iam_client = boto3.client('iam')
iam_client.create_role(
  RoleName='LambdaBasicExecution',
  AssumeRolePolicyDocument=json.dumps(role_policy_document),
)