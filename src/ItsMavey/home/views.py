from django.shortcuts import render
from .API.twitchAPI import TwitchLiveChecker

# Create your views here.


def home(request):
    twitch = TwitchLiveChecker()
    stream_status, game = twitch.check_twitch_stream_status()

    return render(request, 'index.html' , {'stream_status': stream_status, 'game': game})
