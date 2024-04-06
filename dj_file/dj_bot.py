import os
import json
import time
import random
import asyncio
import logging
import highrise
from fuzzywuzzy import process, fuzz
from highrise import*
from highrise.models import*
from highrise.webapi import*
from dj_file.dance import send_continuous_emotes
from dj_file.loop import ContinuousEmoteHandler

class S_O_L_L_Y(BaseBot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open("dj_file/emote.json", "r") as f:
            self.emote_dict = json.load(f)
        self.continuous_emote_tasks = {}
        self.AREA_MIN_X = 1.5
        self.AREA_MAX_X = 10.5
        self.AREA_MIN_Y = 0.25
        self.AREA_MAX_Y = 1.0
        self.AREA_MIN_Z = 22.5
        self.AREA_MAX_Z = 28.5
        self.users = {}
        self.user_data = {}
        self.user_positions = {}
        self.emote_dict = {}
        self.load_emote_dict()
        self.bot_loop_task = None
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.continuous_emote_handler = ContinuousEmoteHandler(self.emote_dict, self.continuous_emote_tasks, self.logger)


    def load_emote_dict(self):
      with open("dj_file/emote.json", "r") as f:
          self.emote_dict = json.load(f)

    async def on_start(self, session_metadata: SessionMetadata) -> None:
            print("SOLLY_DJ")
            await self.highrise.walk_to(AnchorPosition(entity_id='65df8ed10000000000000b44', anchor_ix=0))
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
        if user in [target_user for target_user, _ in room_users] and user.username not in ["SOLLY_DJ"]:
            try:
                await self.highrise.react(reaction, user.id)
            except highrise.ResponseError as e:
                print(f"{self} could not send the reaction {reaction} back to {user}: {e}")

    async def on_chat(self, user: User, message: str) -> None:
      self.logger.info(f"{user.username}: {message}")

      input_emote = message.strip()
      matched_emote = process.extractOne(input_emote, self.emote_dict.keys(), scorer=fuzz.ratio)

      if matched_emote and matched_emote[1] >= 86:
          emote_name = matched_emote[0]
          emote_id = self.emote_dict[emote_name]
          loop_emote_name = message.strip()
          await self.continuous_emote_handler.start_continuous_emote(self.highrise, loop_emote_name, user.id)
          await asyncio.sleep(5)  # Delay for 5 seconds

      elif input_emote.lower().startswith(("Stop", "stop", "0")):
          await self.continuous_emote_handler.stop_continuous_emote(user.id)

      elif input_emote.lower().endswith(("All", "all")):
          emote_name_all = input_emote[:-4].strip()
          emote_id_all = self.emote_dict.get(emote_name_all)
          if emote_id_all:
              room_users = (await self.highrise.get_room_users()).content
              for target_user, _ in room_users:
                  try:
                      await self.highrise.send_emote(emote_id_all, target_user.id)
                  except highrise.ResponseError as e:
                      print(f"Failed to send emote {emote_id_all} to user {target_user.username}: {e}")

      if message.startswith("back") and user.username in ["S_O_L_L_Y"]:
        await self.highrise.walk_to(AnchorPosition(entity_id='65df8ed10000000000000b44', anchor_ix=0))
    