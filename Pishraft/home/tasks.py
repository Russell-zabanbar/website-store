from bucket import Bucket
from celery import shared_task


def bucket_list_objects():
    instanse = Bucket()
    return instanse.get_object()


@shared_task
def bucket_delete_object(key):
    instanse = Bucket()
    instanse.delete_object_bucket(key)


@shared_task
def bucket_download_object(key):
    instans = Bucket()
    instans.download_object_bucket(key)






    