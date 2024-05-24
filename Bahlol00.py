import asyncio
import datetime
import json
import multiprocessing
import os
import random
import time
from datetime import timedelta
from json import dump, load
from time import sleep, time

from highrise import *
from highrise import AnchorPosition, BaseBot, Position, User, __main__
from highrise.__main__ import SessionMetadata
from highrise.models import *
from highrise.models import (
  AnchorPosition,
  ChannelEvent,
  ChannelRequest,
  ChatEvent,
  ChatRequest,
  CurrencyItem,
  EmoteEvent,
  EmoteRequest,
  Error,
  FloorHitRequest,
  GetRoomUsersRequest,
  GetWalletRequest,
  IndicatorRequest,
  Item,
  Position,
  Reaction,
  ReactionEvent,
  ReactionRequest,
  SessionMetadata,
  TeleportRequest,
  TipReactionEvent,
  User,
  UserJoinedEvent,
  UserLeftEvent,
)
from highrise.models_webapi import *
from highrise.webapi import *

dancs = [
    "emote-lust",
    "emote-superpose",
    "dance-tiktok10",
    "dance-weird",
    "emote-charging",
    "emote-snowball",
    "emote-hot",
    "emote-snowangel",
    "dance-russian",
    "emote-curtsy",
    "emote-bow",
    "dance-pennywise",
    "dance-blackpink",
    "emote-model",
    "dance-tiktok8",
    "dance-tiktok2",
    "dance-macarena",
    "emoji-gagging",
    "emoji-flex",
    "emoji-celebrate",
    "emoji-cursing",
    "idle-loop-sitfloor",
    "emote-yes",
    "emote-sad",
    "emote-no",
    "emote-laughing",
    "emote-kiss",
    "emote-hello",
    "emote-zombierun",
    "emote-pose8",
    "emote-pose7",
    "emote-pose5",
    "emote-pose3",
    "emote-pose1",
    "idle-dance-casual",
    "emote-cutey",
    "emote-astronaut",
    "idle-dance-tiktok4",
    "emote-punkguitar",
    "dance-icecream",
    "emote-gravity",
    "emote-fashionista",
    "idle-uwu",
    "dance-wrong",
    "dance-anime",
    "emote-shy2",
    "emote-creepycute",
    "emote-celebrationstep",
    "emote-pose6",
    "emote-iceskating",
    "idle-wild",
    "dance-kawai",
    "idle-dance-tiktok4",
    "emote-pose10",
    "emote-boxer",
    "emote-headblowup",
    "dance-employee",
    "emote-gift",
    'idle-guitar',
    'dance-touch',
    'emote-pose9',
    "dance-pinguin",
    "idle-toilet",
    "idle-enthusiastic"
]
valuesss = ""
user_ad = ["Mahrael","Y_o_u_ss_e_f","youssef1230","M_E_D_O._._","T0ll","MASA_O","Fofaa_A","ISTP_14","19sb","Rouzi00","A_ndrew","DARK20MARO","H_E_R_O_","__KING_0_","franso","MR_TOMAS"]
class S_O_L_L_Y(BaseBot):

  def __init__(self):
    self.dances = {
      "emote-lust": 4,
      "emote-superpose": 0,
      "dance-tiktok10": 8,
      "dance-weird": 21,
      "emote-charging": 7,
      "emote-snowball": 4,
      "emote-hot": 4,
      "emote-snowangel": 5,
      "dance-russian": 10,
      "emote-curtsy": 2,
      "emote-bow": 3,
      "dance-pennywise": 1,
      "dance-blackpink": 7,
      "emote-model": 5,
      "dance-tiktok8": 10.2,
      "dance-tiktok2": 10,
      "emoji-gagging": 5.5,
      "emoji-flex": 1.6,
      "emoji-celebrate": 2.6,
      "emoji-cursing": 2,
      "emote-yes": 2,
      "emote-sad": 4.3,
      "emote-laughing": 2.5,
      "emote-kiss": 3.2,
      "emote-hello": 2.3,
      "emote-zombierun": 9,
      "emote-pose8": 4,
      "emote-pose7": 4.3,
      "emote-pose5": 4.2,
      "emote-pose3": 4,
      "emote-pose1": 2.5,
      "idle-dance-casual": 9,
      "emote-cutey": 2.5,
      "emote-astronaut": 12.2,
      "idle-dance-tiktok4": 15,
      "emote-punkguitar": 8.1,
      "dance-icecream": 14.3,
      "emote-gravity": 6,
      "emote-fashionista": 5,
      "dance-wrong": 12.3,
    }
    self.in_area_users = set()
    self.dance_event = asyncio.Event()
    self.ord = None
    self.ter = []
    self.run = False
    self.d = []
    self.current_dance = None
  async def on_start(self, SessionMetadata: SessionMetadata) -> None:
    try:
        print("on")
        asyncio.create_task(self.send_continuous_dances())
    except Exception as e:
        print(f"error : {e}")
  async def send_continuous_dances(self):
    while True:
        valid_users =[]
        users_positions = await self.highrise.get_room_users(user_id=self.user.id)
        for user, position in users_positions.content:
            if isinstance(position, Position):
                x_range = (0, 8)
                y_range = (0, 0)
                z_range = (0, 6)
                if (
                    x_range[0] <= position.x <= x_range[1]
                    and y_range[0] <= position.y <= y_range[1]
                    and z_range[0] <= position.z <= z_range[1]
                ):
                    valid_users.append("user_id")

        random_dance, duration = random.choice(list(self.dances.items()))
        duration = float(duration)

        async def send_emote_safely(user):
            try:
                await self.highrise.send_emote(random_dance, user.id)
            except Exception as e:
                print(f"Error sending dance to {user.id}: {e}")

        tasks = [asyncio.create_task(send_emote_safely(user)) for user in valid_users]
        await asyncio.gather(*tasks)
        await asyncio.sleep(duration - 0)
        valid_users = ["user_id"]

  async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
    if user.username=="any_body":
        await self.highrise.send_whisper("user.id","")
    pass

  async def print_message(self, message: str, user: User) -> None:
    try:
        dance_number = int(message.split()[0])
        if 1 <= dance_number <= len(dancs):
            current_dance = dancs[dance_number - 1]
            while True:
                try:
                    await self.highrise.send_emote(current_dance, user.id)
                    await asyncio.sleep(12)
                except Exception as e:
                    print(f"Chat Error: {e}")
                    break
    except ValueError:
        print("Invalid dance number format")

  async def on_chat(self, user: User, message: str) -> None:
    global valuesss
    if message.startswith("الحق") and user.username in user_ad:
      values = message.split()
      valuesss = values[1].replace("@", "")
    elif message.startswith("توقف") and user.username in user_ad:
      await self.highrise.chat("حاضر")
      valuesss = "user_id"
      self.stopped = True
      return

    if message.startswith("رقصنا") and user.username in user_ad:
                random_dans = random.sample(dancs, 1)[0]
                list = await self.highrise.get_room_users()
                for user, position in list.content:
                    try:
                        await self.highrise.send_emote(random_dans, user.id)
                    except:
                        print("erorr")

    if message.isdigit() and len(message.split()) > 0:
        if not hasattr(self, 'print_tasks'):
            self.print_tasks = {}

        if hasattr(self, 'print_tasks') and user.id in self.print_tasks and not self.print_tasks[user.id].done():
            self.print_tasks[user.id].cancel()
            await asyncio.sleep(12)

        self.print_tasks[user.id] = asyncio.create_task(self.print_message(message, user))

    if message.startswith(("توقف", "stop","ايقاف")):
        try:
          if hasattr(self, 'print_tasks') and user.id in self.print_tasks and not self.print_tasks[user.id].done():
            self.print_tasks[user.id].cancel()
            await asyncio.sleep(12)
        except ValueError:
            print("Invalid dance number format")


    if message.startswith("انتقال") and user.username in user_ad:
        if user.username not in self.ter:
            self.ter.append(user.username)
        else:
            print("u r in")
    if message.startswith("تحت") and user.username in user_ad:
        if user.username in self.ter:
            self.ter.remove(user.username)
        else:
            print("u r not ")
    if message.startswith("...") : #and user.username in user_ad:
      await self.highrise.teleport(user.id, Position(x='13.5', y='11.2', z='17'))
    if message.startswith("927373829") and user.username == "" :
        list = await self.highrise.get_room_users()
        for user, position in list.content:
            try:
                await self.highrise.move_user_to_room(user.id, '661a23c6249b86137bd771b4')
            except Exception as e:
                print(f"حدث خطأ: {e}")
    if user.username in user_ad:
        if message.startswith(("حظر", "بلوك","اطرد")):
            try:
                name_to_add = message1.split('@')[1]
                room_users = await self.highrise.get_room_users()
                username_targ = name_to_add
                for user, position in room_users.content:
                    if user.username == username_targ:
                        id_user = user.id
                        await self.highrise.moderate_room(id_user, "ban", action_length=1440)
            except Exception as e:
                print(f"Chat Error: {e}")
        if message.startswith("ميوت"):
            try:
                name_to_add = message1.split('@')[1]
                room_users = await self.highrise.get_room_users("تحت")
                username_targ = name_to_add
                for user, position in room_users.content:

                    if user.username == username_targ:
                        id_user = user.id
                        await self.highrise.moderate_room(id_user, "mute", action_length=1440)
            except Exception as e:
                print(f"Chat Error: {e}")

  async def on_user_move(self, user: User, destination: Position | AnchorPosition) -> None :
      if user.username=="Y_o_u_ss_e_f":
          print(destination)
      try:
          if user.username==valuesss:
                self.x = destination.x
                self.y = destination.y
                self.z = destination.z
                await self.highrise.walk_to(Position(self.x, self.y, self.z - 1))
          if user.username in self.ter:
              if isinstance(destination, AnchorPosition):
                  print(f"AnchorPosition(entity_id={destination.entity_id}, anchor_ix={destination.anchor_ix}")
              else:
                  await self.highrise.teleport(user.id, Position(x=destination.x, y=destination.y, z=destination.z))
      except Exception as e:
          print(f"Error : {e}")
  async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
    if user.username == ["Y_o_u_ss_e_f", ""]:
        if reaction == "thumbs" :
            try:
                await self.highrise.move_user_to_room(receiver.id, '')
                await self.highrise.chat("لم نتشرف بك ضيفا فلا تكرر زيارتنا ، لقد تم طرد المستخدم  {user.username}")
            except Exception as e:
                print(f"حدث خطأ: {e}")
    if user.username in user_ad:
      if reaction == "wave" :
            try:
                r_username = receiver.username
                print(f"receiver: {r_username}")
                list = await self.highrise.get_room_users()
                username_targ = user.username
                for user, position in list.content:
                    if user.username == username_targ:
                        print(f"User: {user.username}")
                        print(f"id: {user.id}")
                        positions = f"{position.x}, {position.y}, {position.z}"
                        await self.highrise.teleport(receiver.id, Position(x=position.x, y=position.y, z=position.z - 1))
            except Exception as e:
                print(f"حدث خطأ: {e}")