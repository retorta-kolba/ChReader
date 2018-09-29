from telethon import TelegramClient, sync, events
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetHistoryRequest


api_id = 447894
api_hash = 'cc5a0328d85995641668b0beb131e5e6'

client = TelegramClient('session_name', api_id, api_hash)
client.connect()
#client.run_until_disconnected()


@client.on(events.NewMessage)
async def my_event_handler(event):
    print(event)

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
    

for i in get_messages("TestChannelForSome"):
    print(i.message)