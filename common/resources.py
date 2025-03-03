import boto3
from dotenv import load_dotenv
import os

class Boto3Connector(object):
    def __init__(self,aws_access_key_id, aws_secret_access_key, endpoint_url):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.endpoint_url = endpoint_url
        
    def get_client(self):
        session = boto3.Session()
        
        s3_client = session.client(
            service_name="s3",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            endpoint_url=self.endpoint_url,
        )
        
        return s3_client
    
def boto3_connection(context):
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    endpoint_url = os.getenv("ENDPOINT_URL")
    
    return Boto3Connector(aws_access_key_id, aws_secret_access_key, endpoint_url)