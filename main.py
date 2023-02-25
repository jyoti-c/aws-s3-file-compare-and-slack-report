from libs import aws_s3_client,file_utils,slack_integration
import argparse


def read_and_compare_file_results(file_name, s3_bucket_name,new_file,slackAppOAuthToken,slackChannelId,reportName):
    """
    Read file from AWS S3, compare file with local file, generate comparison report and publish it to slack channel
    :param file_name: String file name from AWS S3
    :param s3_bucket_name: String AWS S3 bucket name
    :param new_file: String local file name
    :param slackAppOAuthToken: String Slack app oAuth token
    :param slackChannelId: String Slack channel id
    :param reportName: String comparison report name
    :return:
    """
    print("Read file from S3")
    aws_s3_client.read_from_s3('./resources/' + file_name, s3_bucket_name, file_name)

    print("Get files comparison report")
    report = file_utils.file_compare_and_generate_report(
        './resources/' + file_name,
        "./resources/" + new_file,reportName)

    print("Send report to slack channel")
    slack_integration.send_file_to_slack_channel(slackAppOAuthToken,slackChannelId,report,"Changed assets")

    print("Upload new file to S3")
    aws_s3_client.upload_to_s3('./resources/' + new_file,s3_bucket_name,new_file)

    print("Upload report to S3")
    aws_s3_client.upload_to_s3(report,s3_bucket_name,reportName+'.png')


if __name__ == "__main__":
    print("==========Task Starts===========")
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3BucketName", help="AWS S3 bucket name to store files")
    parser.add_argument("--s3BucketFileName", help="Name of the file stored in AWS S3 bucket")
    parser.add_argument("--slackAppOAuthToken", help="Slack App OAuth token")
    parser.add_argument("--slackChannelId", help="Slack channel id")
    parser.add_argument("--awsAccessKey", help="AWS Access Key")
    parser.add_argument("--awsSecretKey", help="AWS Secret Key")
    args = parser.parse_args()
    new_file_name='new-asset-details.txt'
    reportName='report'
    aws_s3_client = aws_s3_client.AWSS3Client(args.awsAccessKey, args.awsSecretKey)
    read_and_compare_file_results(args.s3BucketFileName, args.s3BucketName,new_file_name,args.slackAppOAuthToken,args.slackChannelId,reportName)
    print("==========Task Ends===========")
