import json
from botocore.vendored import requests

def lambda_handler(event, context):
    response = requests.get('https://ifconfig.me/')
    print ("INFO: external IP:", response.text)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

