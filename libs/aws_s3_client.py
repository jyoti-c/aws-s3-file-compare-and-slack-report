import boto3
from botocore.exceptions import NoCredentialsError


class AWSS3Client:
    s3 = ''

    def __init__(self, access_key, secret_key):
        self.s3 = boto3.client('s3', aws_access_key_id=access_key,
                               aws_secret_access_key=secret_key)

    def upload_to_s3(self,local_file, bucket, s3_file):
        """
        Uploads local file to AWS S3
        :param local_file: String local file name
        :param bucket: String AWS S3 bucket name
        :param s3_file: String file name in S3
        :return: bool
        """
        try:
            self.s3.upload_file(local_file, bucket, s3_file)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def read_from_s3(self, local_file, bucket, s3_file):
        """
        Read file from AWS S3
        :param local_file: String local file name
        :param bucket: String AWS S3 bucket name
        :param s3_file: String file name in S3
        :return: bool
        """
        try:
            with open(local_file, 'wb') as data:
                self.s3.download_fileobj(bucket, s3_file, data)
            print("Read Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False
