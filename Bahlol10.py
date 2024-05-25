from highrise import (
    BaseBot,
    ChatEvent,
    Highrise,
    __main__,
    UserJoinedEvent,
    UserLeftEvent,
    GetMessagesRequest,
)
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
from asyncio import run as arun
import asyncio
import random
import os
import json
import time
import logging
import highrise
from fuzzywuzzy import process, fuzz
from highrise import*
from highrise.models import*
from highrise.webapi import*
from dj_file.dance import send_continuous_emotes
from dj_file.loop import ContinuousEmoteHandler

class S_O_L_L_Y(BaseBot):
    greetings = [ "منور الروم يا صديقي",
                 "نورت الروم يا حبيبي",


        # ... (ترحيبات أخرى هنا)
    ]

    message_count = {}

    def check_level(self, user_id):
        level = self.message_count.get(user_id, 0) // 10
        return level

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open("dj_file/emote.json", "r") as f:
            self.emote_dict = json.load(f)
        self.continuous_emote_tasks = {}
        self.users = {}
        self.user_data = {}
        self.user_positions = {}
        self.emote_dict = {}
        self.load_emote_dict()
        self.bot_loop_task = None
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.continuous_emote_handler = ContinuousEmoteHandler(self.emote_dict, self.continuous_emote_tasks, self.logger)
        self.is_dancing = False
        self.following_username = None


    def load_emote_dict(self):
      with open("dj_file/emote.json", "r") as f:
          self.emote_dict = json.load(f)

    async def on_start(self, session_metadata: SessionMetadata) -> None:
      print("Bahlol10")
      self.highrise.tg.create_task(self.highrise.teleport(
          session_metadata.user_id, Position(x=15.5, y=0.0, z=20.0, facing='FrontRight')))
      send_continuous_emotes(self)
      try:
        list = [ "dance-tiktok11"]

        while True:
          random_emote = random.choice(list)
          await self.highrise.send_emote(random_emote)
          await asyncio.sleep(10)
      except Exception as e:
            print(f"Error: {e}")


    async def follow_user(self, target_username: str):
      while self.following_username == target_username:
          # ابحث عن موقع المستخدم المستهدف في الغرفة
          response = await self.highrise.get_room_users()
          target_user_position = None
          for user_info in response.content:
              if user_info[0].username.lower() == target_username.lower():
                  target_user_position = user_info[1]
                  break

          if target_user_position and type(target_user_position) != AnchorPosition:
              await self.highrise.walk_to(Position(target_user_position.x , target_user_position.y, target_user_position.z -1))

              await asyncio.sleep(1)  # انتظر 5 ثواني مثلاً


    async def teleport_user_next_to(self, target_username: str, requester_user: User):
      room_users = await self.highrise.get_room_users()
      requester_position = None
      for user, position in room_users.content:
        if isinstance(position, AnchorPosition):
            return
        if user.id == requester_user.id:
          requester_position = position
          break
      for user, position in room_users.content:
        if user.username.lower() == target_username.lower(): 
          z = requester_position.z 
          new_z = z + 1 

          user_dict = {
            "id": user.id,
            "position": Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
       }
          await self.highrise.teleport(user_dict["id"], user_dict["position"])


    async def on_user_join(self, user: User, position: Position) -> None:
    #يحيك
      greeting = random.choice(self.greetings)
      await self.highrise.chat(f"                              {greeting} {user.username} 💖")
      await self.highrise.chat(f"اكتب رقم من 1 ل 87 او رقصني عشان ترقص. 0 توقف رقص.")
      await self.highrise.chat(f"اكتب اوامر لمعرفه الاوامر.")
      await self.highrise.react("heart", user.id)


    #لو عايز الهوست ينقل حد بيراكت
    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        room_users = (await self.highrise.get_room_users()).content
        if user in [target_user for target_user, _ in room_users] and user.username not in ["Bahlol10"]:
            try:
                await self.highrise.react(reaction, user.id)
            except highrise.ResponseError as e:
                print(f"{self} could not send the reaction {reaction} back to {user}: {e}")


    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
      response = await self.highrise.get_messages(conversation_id)
      if isinstance(response, GetMessagesRequest.GetMessagesResponse):
          message = response.messages[0].content
      print (message)
      if message == "You got a tip!":
          await self.highrise.send_message(conversation_id, "Tysm for ur lovely tips, CEREATED BY @S_O_L_L_Y.")


    async def on_chat(self, user: User, message: str) -> None:
      if user.id not in self.message_count:
        self.message_count[user.id] = 0
    # ... (باقي الأوامر هنا)

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

      elif message.startswith(("React", "react", "وزع")) and user.username in ["S_O_L_L_Y"]:
          command_parts = message.split()
          num_reactions = 1
          reaction_name = None

          if len(command_parts) > 1:
              try:
                  num_reactions = int(command_parts[1])
              except ValueError:
                  await self.highrise.send_whisper(user.id, "Invalid number of reactions. Please provide a valid integer.")
                  return
          if len(command_parts) > 2:
              # Check if a specific reaction name is provided
              reaction_name = command_parts[2].lower()
          response = await self.highrise.get_room_users()
          room_users = response.content if hasattr(response, 'content') else []
          reactions = ["heart", "thumbs", "wink", "wave", "clap"]
          delay_between_reactions = 0
          for target_user, _ in room_users:
              if target_user.id != self:
                  for _ in range(num_reactions):
                      if reaction_name:
                          if reaction_name in reactions:
                              selected_reaction = reaction_name
                          else:
                              await self.highrise.send_whisper(user.id, f"Invalid reaction name: {reaction_name}. Available reactions: {', '.join(reactions)}")
                              return
                      else:
                          selected_reaction = random.choice(reactions)
                      try:
                          await self.highrise.react(selected_reaction, target_user.id)
                          await asyncio.sleep(delay_between_reactions)
                      except Exception as e:
                          print(f"{self} could not send the reaction {selected_reaction} to {target_user}: {e}")


      #لو عايز البوت يعمل ريأكت لحد
      if message.startswith(("Hi bot","هاي بوت")):
              await self.highrise.react("heart", user.id)

      if message.lower().startswith("tip ") and user.username in ["S_O_L_L_Y"]:
        parts = message.split(" ")
        if len(parts) != 2:
            await self.highrise.send_message(user.id, "Invalid command")
            return
        #checks if the amount is valid
        try:
            amount = int(parts[1])
        except:
            await self.highrise.chat("Invalid amount")
            return
        #checks if the bot has the amount
        bot_wallet = await self.highrise.get_wallet()
        bot_amount = bot_wallet.content[0].amount
        if bot_amount <= amount:
            await self.highrise.chat("Not enough funds")
            return
        #converts the amount to a string of bars and calculates the fee
        """Possible values are: "gold_bar_1",
        "gold_bar_5", "gold_bar_10", "gold_bar_50", 
        "gold_bar_100", "gold_bar_500", 
        "gold_bar_1k", "gold_bar_5000", "gold_bar_10k" """
        bars_dictionary = {10000: "gold_bar_10k", 
                           5000: "gold_bar_5000",
                           1000: "gold_bar_1k",
                           500: "gold_bar_500",
                           100: "gold_bar_100",
                           50: "gold_bar_50",
                           10: "gold_bar_10",
                           5: "gold_bar_5",
                           1: "gold_bar_1"}
        fees_dictionary = {10000: 1000,
                           5000: 500,
                           1000: 100,
                           500: 50,
                           100: 10,
                           50: 5,
                           10: 1,
                           5: 1,
                           1: 1}
        #loop to check the highest bar that can be used and the amount of it needed
        tip = []
        total = 0
        for bar in bars_dictionary:
            if amount >= bar:
                bar_amount = amount // bar
                amount = amount % bar
                for i in range(bar_amount):
                    tip.append(bars_dictionary[bar])
                    total = bar+fees_dictionary[bar]
        if total > bot_amount:
            await self.highrise.chat("Not enough funds")
            return
        for bar in tip:
            await self.highrise.tip_user(user.id, bar)

      #محفظة البوت
      if message in ["Wallet","wallet","!Wallet","!wallet"] and user.username in ["S_O_L_L_Y"]:
        wallet = (await self.highrise.get_wallet()).content
        await self.highrise.send_whisper(user.id,f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

      #كم واحد برومك
      if message in ["Players","players","!Players","!players"] and user.username in ["S_O_L_L_Y"]:
          room_users = (await self.highrise.get_room_users()).content
          await self.highrise.send_whisper(user.id,f"There are {len(room_users)} users in the room")

      if message.startswith("back") and user.username in ["S_O_L_L_Y"]:
        await self.highrise.walk_to(Position(x=15.5, y=0.0, z=20.0, facing='FrontRight'))

      if message in ["Vip","vip","!Vip","!vip"]:
        try:
          await self.highrise.teleport(f"{user.id}", Position(x=15.5, y=16.0, z=5.0, facing='FrontLeft'))
        except:
          print("error 3")

      if message in ["Dance","dance","!Dance","!dance","رقصنى","رقصني"]:
        try:
            emote_id = random.choice(self.dances)
            await self.highrise.send_emote(emote_id, user.id)
        except Exception as e:
            print(f"Error: {e}")

      if message.startswith(("Get","get","!Get","!get")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
         target_username = message.split("@")[-1].strip()
         if target_username not in ["S_O_L_L_Y"]:
            await self.teleport_user_next_to(target_username, user)

      if message in ["Up","up","!Up","!up","طلعني","طلعنى","صعدني","صعدنى","فوق"]:
        try:
            await self.highrise.teleport(f"{user.id}", Position(x=12.0, y=6.25, z=1.5, facing='FrontRight'))
        except:
          print("error 3")

      if message in ["Down","down","!Down","!down","نزلني","نزلنى","تحت"]:
        try:
            await self.highrise.teleport(f"{user.id}", Position(x=10.5, y=0.0, z=9.5, facing='FrontRight'))
        except:
          print("error 3")

      elif message in ["طولي","My height"]:
          try:
              height_cm = random.randint(150, 190)
              await self.highrise.chat(f"                              {user.username} {height_cm} Cm 💖")
          except Exception as e:
              print(f"Error: {e}")
      elif message in ["وزني" ,"My weight"]:
          try:
              weight_kg = random.randint(60, 99)
              await self.highrise.chat(f"                              {user.username} {weight_kg} Kg 💖")
          except Exception as e:
              print(f"Error: {e}")
      elif message in ["عمري" ,"My age"]:
          try:
              weight_kg = random.randint(8, 30)
              await self.highrise.chat(f"                              {user.username} {weight_kg} Years 💖")
          except Exception as e:
              print(f"Error: {e}")

      if message in ["أوامر","اوامر","الاوامر","الأوامر"]:
        try:
          await self.highrise.send_whisper(user.id, "اوامر البوت 👇👇👇")
          await self.highrise.chat("رقصني 👉 ترقص رقصة عشوائي.")
          await self.highrise.chat("رقم من (1 to 87) 👉 عشان ترقص رقصه معينه.")
          await self.highrise.chat("vip 👉 ينقلك للفي اي بي.")
          await self.highrise.chat("طلعني 👉 يطلعك.")
          await self.highrise.chat("نزلني 👉 ينزلك.")
        except Exception as e:
            print(f"Error: {e}")


      if message in ["Help","help","!Help","!help"]:
        try:
          await self.highrise.send_whisper(user.id, "Bot Commands 👇👇👇")
          await self.highrise.chat("Dance 👉 for random emote.")
          await self.highrise.chat("Dance all 👉 for random emote to all room.")
          await self.highrise.chat("Number from (1 to 68) 👉 to dance specific emote.")
          await self.highrise.chat("emote name or Number from (1 to 68) + aLL 👉 to dance with others specific emote.Ex: All 5 or Repose all")
          await self.highrise.chat("!emotes 👉 to get emotes list.")
          await self.highrise.chat("!down 👉 to go down.")
          await self.highrise.chat("!mod 👉 only for mods.")
          await self.highrise.chat("!owner 👉 only for owner.")
        except Exception as e:
            print(f"Error: {e}")

      if message in ["Mod","mod","!Mod","!mod"]:
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
          try:
            await self.highrise.send_whisper(user.id, "Mod Commands 👇👇👇")
            await self.highrise.send_whisper(user.id, "!vip 👉 tele u to vip.")
            await self.highrise.send_whisper(user.id, "!tele + @usename + vip,down or start 👉 tele player to this spot. Ex.(!tele @S_O_L_L_Y vip)")
            await self.highrise.send_whisper(user.id, "!get + @username 👉 tele player to ur spot. Ex.(!get @S_O_L_L_Y)")
            await self.highrise.send_whisper(user.id, "Tele ppl by react them 👉 Thumb to vip, wave to down.")
            await self.highrise.send_whisper(user.id, "kick + @username.")
            await self.highrise.send_whisper(user.id, "ban + @username + (300,900 or 3600).")
            await self.highrise.send_whisper(user.id, "unban + @username.")
            await self.highrise.send_whisper(user.id, "mute + @username + (300,900 or 3600).")
          except Exception as e:
              print(f"Error: {e}")

      if message in ["Owner","owner","!Owner","!owner"]:
        if user.username in ["S_O_L_L_Y"]:
          await self.highrise.send_whisper(user.id, "Owner Commands 👇👇👇")
          await self.highrise.send_whisper(user.id, "!tip + gold 👉 to tip all room.")
          await self.highrise.send_whisper(user.id, "tip 3 1g 👉 to tip 3 random 1g each.")
          await self.highrise.send_whisper(user.id, "Wallet 👉 bot wallet.")
          await self.highrise.send_whisper(user.id, "follow + @username 👉 bot follow him.")


      if message.lstrip().startswith("!tele"):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
          response = await self.highrise.get_room_users()
          users = [content[0] for content in response.content]
          usernames = [user.username.lower() for user in users]

          parts = message[1:].split()
          args = parts[1:]
          if len(args) < 2:
            await self.highrise.send_whisper(user.id, "Use: Command > Name > Place")
            return
          elif args[0][0] != "@":
            await self.highrise.send_whisper(user.id, "Incorrect format '@username'.")
            return
          elif args[0][1:].lower() not in usernames:
            await self.highrise.send_whisper(user.id, f"{args[0][1:]} not in the room.")
            return
          position_name = "".join(args[1:])
          destinations = {
              'vip': Position(x=15.5, y=16.0, z=5.0, facing='FrontLeft'),
              'up': Position(x=12.0, y=6.25, z=1.5, facing='FrontRight'),
              'down': Position(x=10.5, y=0.0, z=9.5, facing='FrontRight'),
              'start' : Position(x=15.5, y=0.0, z=20.0, facing='FrontRight'),
          }
          dest = destinations.get(position_name.lower())
          if dest is None:
            return await self.highrise.send_whisper(user.id, f"The site is wrong ")
          user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
          if not user_id:
            await self.higrise.send_whisper(user.id, f"User {args[0][1:]} unavailable ")
            return

          await self.highrise.teleport(user_id, dest)
          await self.highrise.send_whisper(user.id, f"Done")
        else:
          await self.highrise.send_whisper(user.id, "You can't use this command")
      else:
          pass

      #لو عايز توزع جولد عشوائي
      if message == ("tip 3 1g") and user.username in ["S_O_L_L_Y"]:
        roomUsers = (await self.highrise.get_room_users()).content
      #shuffle the list to ensure randomnesss
        random.shuffle(roomUsers)
      #select the first three users
        selected_users = roomUsers[:3]
        for roomUser, _ in selected_users:
           await self.highrise.tip_user(roomUser.id, "gold_bar_1")
           await self.highrise.chat(f"S_O_L_L_Y tipped {roomUser.username} 1 Gold! 💰")

      if message == ("tip 1 1g") and user.username in ["S_O_L_L_Y"]:
        roomUsers = (await self.highrise.get_room_users()).content
      #shuffle the list to ensure randomnesss
        random.shuffle(roomUsers)
      #select the first three users
        selected_users = roomUsers[:1]
        for roomUser, _ in selected_users:
           await self.highrise.tip_user(roomUser.id, "gold_bar_1")
           await self.highrise.chat(f"S_O_L_L_Y tipped {roomUser.username} 1 Gold! 💰")

      if message == ("tip 2 1g") and user.username in ["S_O_L_L_Y"]:
        roomUsers = (await self.highrise.get_room_users()).content
      #shuffle the list to ensure randomnesss
        random.shuffle(roomUsers)
      #select the first three users
        selected_users = roomUsers[:2]
        for roomUser, _ in selected_users:
           await self.highrise.tip_user(roomUser.id, "gold_bar_1")
           await self.highrise.chat(f"S_O_L_L_Y tipped {roomUser.username} 1 Gold! 💰")

      if message == ("tip 1 5g") and user.username in ["S_O_L_L_Y"]:
        roomUsers = (await self.highrise.get_room_users()).content
      #shuffle the list to ensure randomnesss
        random.shuffle(roomUsers)
      #select the first three users
        selected_users = roomUsers[:1]
        for roomUser, _ in selected_users:
           await self.highrise.tip_user(roomUser.id, "gold_bar_5")
           await self.highrise.chat(f"S_O_L_L_Y tipped {roomUser.username} 5 Gold! 💰")


      if message.startswith("!tip "):
        try:
            tip_amount = int(message.split(" ")[1])
        except IndexError:
            await self.highrise.send_whisper(user.id, "Spesify a tip amount.")
            return
        except ValueError:
            await self.highrise.send_whisper(user.id, "Invalid amount.")
            return
        if user.username in ["S_O_L_L_Y"]:
            response = await self.highrise.get_room_users()
            num_users = len(response.content)
            total_gold = tip_amount * num_users

            bot_wallet = await self.highrise.get_wallet()
            bot_amount = bot_wallet.content[0].amount

            if bot_amount >= total_gold:
                for content in response.content:
                    user_id = content[0].id
                    await self.highrise.tip_user(user_id, f"gold_bar_{tip_amount}")
            else:
                await self.highrise.send_whisper(user.id, "Not enough funds")


      #لو عايز يتبع حد
      if message.lower().startswith(('Follow @','follow @','!Follow @','!follow @')):
        if user.username in ["S_O_L_L_Y"]:
          target_username = message.split("@")[1].strip()

          if target_username.lower() == self.following_username:
              await self.highrise.chat(f"I am already following {user.username}.")
          else:
              self.following_username = target_username
              await self.highrise.chat(f"okay ❤")
              # بمجرد تعيين المستخدم الذي يجب متابعته، استدعِ وظيفة follow_user
              await self.follow_user(target_username)
      elif message.lower() == "stop" and user.username in ["S_O_L_L_Y"]:
          self.following_username = None
          await self.highrise.chat("okay ❤")