import os

from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel

channel_id = os.environ['TELEGRAM_CHANNEL_ID']
api_id = int(os.environ['TELEGRAM_API_ID'])
api_hash = os.environ['TELEGRAM_API_HASH']
hook_url = os.environ['TELEGRAM_ROUTE_HOOK_URL']
session_name = os.environ.get('TELEGRAM_SESSION_NAME', str(api_id))
client = TelegramClient(session_name, api_id, api_hash)
client.start()


@client.on(events.NewMessage(pattern='.*'))
async def handler(event):
    if isinstance(event.message.peer_id, PeerChannel) and event.message.peer_id.channel_id == channel_id:
        print(event.message.peer_id)
        print(event.message.message)


client.run_until_disconnected()
