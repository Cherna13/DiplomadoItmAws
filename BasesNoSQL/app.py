import boto3

# instanciar un usuario de dinamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

# asignar la tabla a una variable
tabla = dynamodb.Table('tabla-carlos-hernandez')

# asignar el item con id 2 a una variable
response = tabla.get_item(Key={'id':'2'})

# imprimir el item de la variable
print(response['Item'])

# asignar los items de la tabla a una variable
response = tabla.scan()

# imprimir los items
print(response['Items'])


# declaramos el item
item_data = {
    'id': '001',  
    'nombre': 'John Doe',
    'edad': 30,
    'correo': 'johndoe@example.com'
}


# insertar nuevo registro
response = tabla.put_item(
    Item=item_data
)

response = tabla.scan()

print(response['Items'])


#actualizar una tabla
response = tabla.update_item(
    Key={
        'id': '001'  # Asegúrate de que este sea el identificador correcto
    },
    UpdateExpression="SET #nm = :n, #ag = :a, #em = :e",
    ExpressionAttributeNames={
        '#nm': 'nombre',
        '#ag': 'edad',
        '#em': 'correo'
    },
    ExpressionAttributeValues={
        ':n': 'Jane Doe',  # Nuevo nombre
        ':a': 32,          # Nueva edad
        ':e': 'janedoe@example.com'  # Nuevo email
    },
    ReturnValues="UPDATED_NEW"
)