import boto3

client = boto3.client('dynamodb',
                      endpoint_url='http://localhost:8000/ ')

client.list_tables( )

