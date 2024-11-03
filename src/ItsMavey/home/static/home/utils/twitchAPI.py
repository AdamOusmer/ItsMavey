import requests
from django.conf import settings

def check_twitch_stream_status():
    url = f'https://api.twitch.tv/helix/streams?user_login={settings.TWITCH_STREAMER_NAME}'
    headers = {
        'Client-ID': settings.TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {settings.TWITCH_ACCESS_TOKEN}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['data']:
            return f"{settings.TWITCH_STREAMER_NAME} is LIVE!"
        else:
            return f"{settings.TWITCH_STREAMER_NAME} is offline."
    else:
        return "Error fetching stream status"
