from slack_sdk import WebClient


def send_file_to_slack_channel(appOAuthToken, channelId, fileName, fileTitle):
    client = WebClient(appOAuthToken)

    client.files_upload_v2(file=fileName, title=fileTitle, channel=channelId)

