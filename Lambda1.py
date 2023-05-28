import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import boto3
client = boto3.client('glue')

def lambda_handler(event, context):
    response=client.start_crawler(Name='TargetS3')
    return response