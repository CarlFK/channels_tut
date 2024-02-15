# pistat/send.py
# sends a message to the pistat websocket thing

import sys
sys.path.insert(0, '..' )

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()
async_to_sync(channel_layer.group_add)("chat_lobby", 'cli')
async_to_sync(channel_layer.group_send)( 'chat_lobby', {"type": "chat.message", "message": "send.py"} )
