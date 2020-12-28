import os

from telethon import TelegramClient


class Properties:
    def __init__(self):
        self.api_id = int(os.environ['TELEGRAM_API_ID'])
        self.api_hash = os.environ['TELEGRAM_API_HASH']
        self.hook_urls = os.environ['TELEGRAM_ROUTE_HOOK_URLS'].split(",")
        self.session_name = os.environ.get('TELEGRAM_SESSION_NAME', str(self.api_id))
        self.channel_id = os.environ.get('TELEGRAM_CHANNEL_ID')
        self.channel_title = os.environ.get('TELEGRAM_CHANNEL_TITLE')

    async def get_channel_id(self, client: TelegramClient):
        if self.channel_id:
            return self.channel_id
        if self.channel_title:
            async for dialog in client.iter_dialogs():
                if dialog.title == self.channel_title:
                    return self.remove_prefix(str(dialog.id), '-100')

    @staticmethod
    def remove_prefix(text, prefix):
        if text.startswith(prefix):
            return text[len(prefix):]
        return text
