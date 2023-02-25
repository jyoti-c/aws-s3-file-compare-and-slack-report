from slack_sdk import WebClient


def send_file_to_slack_channel(appOAuthToken, channelId, fileName, fileTitle):
    """
    Sends file to slack channel
    :param appOAuthToken: String Slack app oauth token
    :param channelId: String Slack channel id
    :param fileName: String file name to be sent
    :param fileTitle: String file title
    :return:
    """
    client = WebClient(appOAuthToken)
    client.files_upload_v2(file=fileName, title=fileTitle, channel=channelId)

