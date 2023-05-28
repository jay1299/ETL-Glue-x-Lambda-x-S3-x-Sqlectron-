# Set up logging
import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import boto3
client = boto3.client('glue')

glueJobName = "Job1"

# Define Lambda function
def lambda_handler(event, context):
    response = client.start_job_run(JobName = glueJobName)
    return response
