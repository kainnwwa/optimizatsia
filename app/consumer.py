import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class TimerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('action') == 'start':
            seconds = int(data.get('seconds', 0))
            if seconds > 0:
                asyncio.create_task(self.run_timer(seconds))

    async def run_timer(self, seconds):
        for i in range(seconds, -1, -1):
            await self.send(text_data=json.dumps({
                'time_left': i
            }))
            if i > 0:
                await asyncio.sleep(1)