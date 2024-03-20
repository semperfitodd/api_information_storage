import boto3
import json

TABLE_NAME = 'api_poc'
FILE_PATH = 'api_info.json'


def put_data_into_dynamodb(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    for api_name, properties in data.items():
        item = {'API_NAME': api_name}
        if not isinstance(properties, dict):
            print(f"Expected a dictionary for properties, got: {type(properties)}")
            continue
        for prop_key, prop_value in properties.items():
            print(f"Inserting {prop_key}: {prop_value}")  # Debugging print
            item[prop_key] = prop_value

        try:
            table.put_item(Item=item)
            print("Data inserted successfully")
        except Exception as e:
            print(f"Failed to insert data: {e}")


if __name__ == "__main__":
    put_data_into_dynamodb(FILE_PATH)
