from storages.backends.s3boto3 import S3Boto3Storage

MediaRootS3BotoStorage  = lambda: S3Boto3Storage(location='media')

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = True

class StaticStorage(S3Boto3Storage):
    location = 'static'
    file_overwrite = True
