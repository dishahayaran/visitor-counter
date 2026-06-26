import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("visitor-counter")


def lambda_handler(event, context):
    response = table.get_item(
        Key={
            "id": "homepage"
        }
    )

    item = response.get("Item", {})
    current_count = item.get("count", 0)

    print(f"Current Count: {current_count}")

    updated_count = current_count + 1

    table.update_item(
        Key={
            "id": "homepage"
        },
        UpdateExpression="SET #c = :count",
        ExpressionAttributeNames={
            "#c": "count"
        },
        ExpressionAttributeValues={
            ":count": updated_count
        }
    )

    print(f"Updated Count: {updated_count}")

    return {
        "currentCount": current_count,
        "updatedCount": updated_count
    }