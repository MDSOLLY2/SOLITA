import asyncio
import logging
from highrise import *
from highrise.models import *

class ContinuousEmoteHandler:
    def __init__(self, emote_dict, continuous_emote_tasks, logger):
        self.emote_dict = emote_dict
        self.continuous_emote_tasks = continuous_emote_tasks
        self.logger = logger

    async def start_continuous_emote(self, highrise, emote_name, user_id, delay=10):
        emote_id = self.emote_dict.get(emote_name)
        if emote_id is not None:
            # Stop the previous continuous emote loop if it's already running for the user
            await self.stop_continuous_emote(user_id)

            task = asyncio.create_task(self.send_continuous_emote(highrise, emote_id, user_id, delay))
            self.continuous_emote_tasks[user_id] = task
            self.logger.info(f"Started continuous emote loop for user {user_id} with emote {emote_name}")
        else:
            self.logger.warning(f"Emote '{emote_name}' not found in the emote_dict.")

    async def send_continuous_emote(self, highrise, emote_id, user_id, delay):
        try:
            while True:
                await highrise.send_emote(emote_id, user_id)
                await asyncio.sleep(delay)
        except asyncio.CancelledError:
            # Emote was cancelled, restart it immediately
            self.logger.info(f"Continuous emote loop for user {user_id} cancelled. Restarting...")

    async def stop_continuous_emote(self, user_id):
        if user_id in self.continuous_emote_tasks:
            task = self.continuous_emote_tasks.pop(user_id)
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
            self.logger.info(f"Stopped continuous emote loop for user {user_id}")
          