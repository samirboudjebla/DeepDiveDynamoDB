""" 
    this code is trying to update a dynamodb table using a file but it has a bug
"""

import json

import boto3

dynamodb = boto3.resource('dynamodb')

table= dynamodb.Table('PetInventory')

with open('update.json') as myfile: 
    data = json.load(myfile)

with open('C:/Users/Samir/source/repos/DeepDiveDynamoDB/02_Table_IO/023_Lab_Table_IO/update.json') as myfile: 
    data = json.load(myfile)



mylist = data['PetInventory']

for i in mylist:
    putrequest = i['PutRequest']
    itemjson = putrequest['Item']

    table.update_item(
        Key={
            'pet_species': itemjson['pet_species'],
            'pet_id': itemjson['pet_id']
            },
        UpdateExpression='SET pet_availability = :val1',
        ExpressionAttributeValues={
            ':val1': itemjson['pet_availability']
            }
        )



