# Monitoring data in AWS DynamoDB table with DynamoDB streams and Lambda + setting up SNS notifications (using Python3)
A short example on how to set up Lambda to read DynamoDB streams in AWS and send e-mails upon detecting specific data

DynamoDB is a great option for storing sensor data (or any kind of data, really). For one of the projects I was involved with, I was working on simulating sensor dataflow with AWS and DynamoDB. At some point the customer wanted to add the feature where he could receive an e-mail or SMS from AWS that would inform if the simulated device was outside a certain geographical area. 

AWS provides a great service called [DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html), which you can enable through your console for any of the DynamoDB tables. This service provides a time-ordered sequence of item-level modifications in the table. So whenever you update, insert or remove items in the table, there will be a stream record containing information about these modifications. 

DynamoDB Streams update the information near real-time, which is handy for building applications that can track your data changes. 
In this tutorial I am using Lambda to read those record streams and to send an e-mail if it detects strange data values (in my case it's the latitude/longitude values outside a certain area).

#### Note: 
I am using Python's [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), an SDK for the AWS stack. This guide assumes you already have created a DynamoDB table with data (if you don't know how, use this guide written by me [here](https://github.com/lgrigoryeva1/aws-iot-dynamodb). If you are more comfortable using node.js, AWS documentation has a great tutorial [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.Tutorial.html)

#### Enabling DynamoDB Streams
First, enable DynamoDB streams for your table. You can do it through the console: Under the `Overview` tab click `Manage stream`. You can choose what kind of stream records you want to obtain.

#### Capturing the streams
1. *get_shard.py*  prints the shard iterator
2. Substitute the shard ID that is returned from running the previous script
3. *get_records.py* prints the records in the shard
4. Substitute the shard iterator that is returned from running the previous script
5. Note: you might need to iterate over the shards a few times before being able to retrieve data
   - Useful [source](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html) on stream records, shards, etc. 

#### Setting up SNS (the notifications service)
1. Run *create_topic.py*
2. Store topic arn for the next step
3. Run *sns_subscribe.py*
4. Modify protocol, endpoint if needed

#### Create a Lambda function
1. Source code of Lambda handler: *main.py*
2. Substitute topic arn
3. Zip *main.py* to *lambda.zip*
4. Run *lambda_execution_role.py*
5. Run *create_function.py*
   - If this is confusing, [here](https://codeburst.io/aws-lambda-functions-made-easy-1fae0feeab27) is a great tutorial on Lambdas.

#### Sample data for testing Lambda
Sample data can be found in *sample-data-git.json*. This is sample data that can be used for testing Lambda. Real-time code will be uploaded soon.

#### Useful sources: 
* DynamoDB Streams documentation: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html
* Lambda: https://aws.amazon.com/lambda/
* SNS: https://docs.aws.amazon.com/sns/latest/dg/sns-how-it-works.html 







