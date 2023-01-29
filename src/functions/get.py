import json
import uuid


def blobs(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
        "blob_id": str(uuid.uuid4()),
        "test": event['pathParameters']['id']
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
