from telethon import TelegramClient, sync, events
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetHistoryRequest
from ConnectionFactory import *
from storers import *
from telegram import *


def init():
    ClientRoot.connect()

#client = TelegramClient('session_name', api_id, api_hash)
#client.connect()

def get_messages(channel_name):
    channel_entity=client.get_entity(channel_name)
    posts = client(GetHistoryRequest(
        peer=channel_entity,
        limit=100,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))
    return posts.messages
#print(dir(storers))
#print(storers.ChannelStorer)
#ChannelStorer
ChannelStorer("a")
#for i in get_messages("TestChannelForSome"):
#    print(i.message)
    
#with ConnectionFactory.get_connection():
#   pass
#
init()