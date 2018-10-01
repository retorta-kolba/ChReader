from telethon import TelegramClient, sync, events
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetHistoryRequest

api_id = 447894
api_hash = 'cc5a0328d85995641668b0beb131e5e6'

class ChannelReader:
    def __init__(self, client):
        self.client = client
        
        

class TgClient:
    def __init__(self, client):
        self.client = client
        client.connect()
        
    def get_last_message_id(self, channel_name):
        channel_entity = self.client.get_entity(channel_name)
        posts = self.client(GetHistoryRequest(
            peer=channel_entity,
            limit=1,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))
        try:
            return posts.messages[0].id
        except:
            return 0
        
    def get_messages(self, channel_name, min_id=0):
        channel_entity = self.client.get_entity(channel_name)
        print(channel_entity)
        posts = self.client(GetHistoryRequest(
            peer=channel_entity,
            limit=100,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=min_id,
            add_offset=0,
            hash=0))
        return posts.messages
    


class Clients:
    @staticmethod
    def connect():
        ClientRoot.default.connect()
    default = TgClient(TelegramClient('session_name', api_id, api_hash))
    