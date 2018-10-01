from telethon import TelegramClient, sync, events
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetHistoryRequest
from ConnectionFactory import *
from storers import *
from telegram import *


def init():
    pass

def add_channel(channel_name):
    with ConnectionFactory.get_connection() as conn:
        channel = Clients.default.client.get_entity(channel_name)
        last_message_id = Clients.default.get_last_message_id(channel_name)
        ChannelStorer(conn).add_channel(channel.id, channel.username, channel.title, last_message_id)

#client = TelegramClient('session_name', api_id, api_hash)
#client.connect()

add_channel("TestChannelForSome")
#Clients.default.get_messages("TestChannelForSome", 3)
#print(dir(storers))
#print(storers.ChannelStorer)
#ChannelStorer
#ChannelStorer("a")
#for i in get_messages("TestChannelForSome"):
#    print(i.message)
    
#with ConnectionFactory.get_connection():
#   pass
#
init()