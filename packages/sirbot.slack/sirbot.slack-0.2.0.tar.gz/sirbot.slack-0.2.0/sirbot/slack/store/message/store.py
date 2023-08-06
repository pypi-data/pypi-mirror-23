import logging

from sirbot.core import registry

from .message import SlackMessage
from ... import database

logger = logging.getLogger(__name__)


class MessageStore:

    def __init__(self, client):

        self._client = client

    async def thread(self, message, limit=20):
        db = registry.get('database')

        thread_ts = message.thread or message.timestamp
        raw_msgs = await database.__dict__[db.type].message.get_thread(
            db, thread_ts, limit)
        messages = await self._create_object(raw_msgs)
        return messages

    async def channel(self, channel_id, since, until, limit=20, fetch=False):
        db = registry.get('database')
        raw_msgs = await database.__dict__[db.type].message.get_channel(
            db, channel_id, since, until)
        messages = await self._create_object(raw_msgs)
        return messages

    async def _create_object(self, raw_msgs):
        slack = registry.get('slack')
        messages = list()
        for raw_msg in raw_msgs:
            message = await SlackMessage.from_raw(
                data=raw_msg['raw'],
                slack=slack
            )
            messages.append(message)

        return messages
