from django.conf import settings
from django.utils import timezone
from ..models import API

import requests
import datetime


class TwitchLiveChecker:
    TWITCH_CLIENT_ID = settings.TWITCH_CLIENT_ID
    TWITCH_CLIENT_SECRET = settings.TWITCH_CLIENT_SECRET
    TWITCH_STREAMER_NAME = settings.TWITCH_STREAMER_NAME

    def __init__(self):
        self.access_token = self._access_token()

    @staticmethod
    def _query_token():
        api = API.objects.filter(name='twitch').first()

        if api:
            return api.get_decrypted_key() if api.expires_at > timezone.now() else None

        return None

    @staticmethod
    def _save_token(token):

        api = API.objects.filter(name='twitch').first()

        if api:
            api.save(name='twitch', key=token['access_token'], created_at=timezone.now() ,expires_at=timezone.now() + datetime.timedelta(seconds=token['expires_in']))
        else:
            API.objects.create(
                name='twitch',
                key=token['access_token'],
                created_at=timezone.now(),
                expires_at=timezone.now() + datetime.timedelta(seconds=token['expires_in'])
            )

    def _access_token(self):
        token = self._query_token()

        if token:
            return token

        url = "https://id.twitch.tv/oauth2/token"

        payload = {
            'client_id': settings.TWITCH_CLIENT_ID,
            'client_secret': settings.TWITCH_CLIENT_SECRET,
            'grant_type': 'client_credentials'
        }

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            data = response.json()
            self._save_token(data)
            return data['access_token']

        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    def check_twitch_stream_status(self):
        url = f"https://api.twitch.tv/helix/streams?user_login={settings.TWITCH_STREAMER_NAME}"
        headers = {
            'Client-ID': settings.TWITCH_CLIENT_ID,
            'Authorization': f"Bearer {self._access_token()}"
        }
        response = requests.get(url, headers=headers)


        if response.status_code == 200:
            data = response.json()

            if data.get('data'):
                return "true", data['data'][0]['game_name']

            else:
                return "false", None
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return "ERROR"
