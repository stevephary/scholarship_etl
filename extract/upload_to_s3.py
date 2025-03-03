import logging
from dotenv import load_dotenv
import os
from common.resources import Boto3Connector

def upload_to_s3(data, filename):
    logging.info("Uploading data to S3")
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    endpoint_url = os.getenv("ENDPOINT_URL")
    bucket_name = os.getenv("BUCKET_NAME", "scholarship")
    
    # Initialize the Boto3Connector with credentials from .env
    s3_client = Boto3Connector(
        aws_access_key_id,
        aws_secret_access_key,
        endpoint_url
    ).get_client()
    
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except:
        s3_client.create_bucket(Bucket=bucket_name)
    if data:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=f"{filename}.json",
            Body=data,
        )
        logging.info(f"Data successfully uploaded to S3: {filename}.json")
    else:
        logging.error("No data to upload.")