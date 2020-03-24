import boto3, botostubs

client = boto3.client('dynamodb')


response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName':'pet_species',
            'AttributeType': 'S',
        }, 
        {
            'AttributeName':'pet_id',
            'AttributeType':'N'
        }
    ],
    TableName='PetInventory', 
    KeySchema=[
        {
            'AttributeName':'pet_species',
            'KeyType':'HASH'
        },
        {
            'AttributeName':'pet_id',
            'KeyType':'RANGE'
        },
    ],
    BillingMode = 'PAY_PER_REQUEST'
)