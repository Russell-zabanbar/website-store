import boto3
import logging
from django.conf import settings


class Bucket:

    def __init__(self):
        
        session = boto3.session.Session()
        self.connection = session.client(

            service_name = settings.AWS_SERVICE_NAME,
            endpoint_url= settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
 
    def get_object(self):
        result = self.connection.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']
        else:
            return None

     
    def delete_object_bucket(self, key):
        self.connection.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME,Key=key)
        return True

    def download_object_bucket(self, key):
        with open(settings.AWS_LOCAL_STORAGE + key, 'wb') as f: 
            self.connection.download_fileobj(settings.AWS_STORAGE_BUCKET_NAME,key,f)
            return True
