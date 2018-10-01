from telethon import TelegramClient, sync, events
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetHistoryRequest

api_id = 447894
api_hash = 'cc5a0328d85995641668b0beb131e5e6'

class ChannelReader:
    def __init__(self, client):
        self.client = client
        
    def get_last_channel_messages(channel, last_read_message):
        pass
        
    def get_last_message_id(channel):
        pass
        

class TgClient:
    def __init__(self, client):
        self.client = client
        client.connect()
    


class Clients:
    @staticmethod
    def connect():
        ClientRoot.default.connect()
    default = TgClient(TelegramClient('session_name', api_id, api_hash))
    