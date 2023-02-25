# aws-s3-file-compare-and-slack-report

**This code performs the following operations -**

1. Reads the file from your AWS S3 bucket
2. Compares the file with your local file using Python difflib
3. Genrates an HTML and PNG report of the difference
4. Sends the report to a slack channel using Python SLack SDK
5. Uploads the new file and report to AWS S3

**To run the main.py, the following values are to be passed as command line argunments -**

1. AWS account access key
2. AWS account secret key
3. AWS S3 bucket name
4. File name in S3
5. Slack App OAuth Token
6. Slack Channel Id
