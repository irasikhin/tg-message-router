import asyncio
import json

import requests
from telethon import TelegramClient
from telethon.events import NewMessage
from telethon.tl.custom import Message
from telethon.tl.types import PeerChannel

from properties import Properties


async def main():
    print('start bot')
    properties = Properties()
    print('properties: %s' % json.dumps(vars(properties), indent=4))
    client = TelegramClient(properties.session_path + '/' + properties.session_name,
                            properties.api_id,
                            properties.api_hash)
    await client.start()
    channel_id = await properties.get_channel_id(client)
    print('channel_id: %s' % channel_id)

    @client.on(NewMessage(pattern='.*'))
    async def handler(event: NewMessage.Event):
        print('from channel "%s" rececived message "%s"' % (event.message.peer_id, event.message.message))
        if match_channel(channel_id, event.message):
            await post_message(channel_id, event.message.message, properties)

    # print('message from peer %s received' % json.dumps(vars(event.message), indent=4))

    print('bot started')
    async with client:
        await client.run_until_disconnected()


asyncio.run(main())


def match_channel(channel_id: str, message: Message):
    if not isinstance(message.peer_id, PeerChannel):
        return False
    if not channel_id:
        return False
    if channel_id != message.peer_id.channel_id:
        return False
    return True


async def post_message(channel_id: str, message: str, properties: Properties):
    request = {
        'channel_id': channel_id,
        'message': message
    }
    for hook_url in properties.hook_urls:
        try:
            print('send notify "%s" to url "%s"' % (request, hook_url))
            requests.post(hook_url, json=request)
        except Exception as e:
            print('error occurs during %s hook notification, error %s' % (hook_url, e))
