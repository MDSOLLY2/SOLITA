import os
import json
import time
import random
import asyncio
import logging
import highrise
from highrise import*
from highrise.models import*
from highrise.webapi import*
from dj_file.dance import send_continuous_emotes
from highrise.models import Position

class S_O_L_L_Y(BaseBot):

    def __init__(self):
        self.AREA_MIN_X = 9.5
        self.AREA_MAX_X = 13.5
        self.AREA_MIN_Y = 0.75
        self.AREA_MAX_Y = 1.25
        self.AREA_MIN_Z = 7.5
        self.AREA_MAX_Z = 15.5


    def load_emote_dict(self):
      with open("dj_file/emote.json", "r") as f:
          self.emote_dict = json.load(f)

    async def on_start(self, session_metadata: SessionMetadata) -> None:
            print("SOLLY_DJ")
            self.highrise.tg.create_task(self.highrise.teleport(
                  session_metadata.user_id, Position(x=15.5, y=0.5, z=11.5, facing='FrontLeft')))
            send_continuous_emotes(self)
            try:
              list = [ "dance-tiktok11"]

              while True:
                random_emote = random.choice(list)
                await self.highrise.send_emote(random_emote)
                await asyncio.sleep(10)
            except Exception as e:
              print(f"Error: {e}")


    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        room_users = (await self.highrise.get_room_users()).content
        if user in [target_user for target_user, _ in room_users] and user.username not in ["Bahlol55"]:
            try:
                await self.highrise.react(reaction, user.id)
            except highrise.ResponseError as e:
                print(f"{self} could not send the reaction {reaction} back to {user}: {e}")

    async def on_chat(self, user: User, message: str) -> None:

      if message.startswith("back") and user.username in ["S_O_L_L_Y"]:
        await self.highrise.walk_to(Position(x=15.5, y=0.5, z=11.5, facing='FrontLeft'))
