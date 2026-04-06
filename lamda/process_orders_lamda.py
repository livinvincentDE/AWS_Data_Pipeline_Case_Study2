import json
import boto3
import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    # ✅ Define table INSIDE function
    table = dynamodb.Table('orders_metrics')
    
    bucket = "de-serverless-pipeline"
    key = "raw/orders.json"
    
    obj = s3.get_object(Bucket=bucket, Key=key)
    
    # Handle NDJSON
    lines = obj['Body'].read().decode('utf-8').splitlines()
    data = [json.loads(line) for line in lines]
    
    # Transform
    cleaned = [row for row in data if row["amount"] > 0]
    
    # KPI
    total_sales = sum(row["amount"] for row in cleaned)
    total_orders = len(cleaned)
    
    # ✅ Store in DynamoDB
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    table.put_item(
        Item={
            "date": today,
            "total_sales": total_sales,
            "total_orders": total_orders
        }
    )
    
    # ✅ Partitioned S3 write
    now = datetime.datetime.now()
    
    output_key = f"processed/year={now.year}/month={now.month}/day={now.day}/orders_{now.strftime('%H%M%S')}.json"
    
    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=json.dumps(cleaned)
    )
    
    print(f"Total Sales: {total_sales}, Orders: {total_orders}")
    
    return {
        "statusCode": 200,
        "body": "Success"
    }