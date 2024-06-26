import boto3

# instanciar un usuario de dinamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')


response = dynamodb.delete_table(
        TableName='tabla-carlos-hernandez-2'
        )

print(response)