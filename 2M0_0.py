from highrise import BaseBot, Position
from highrise import __main__
from highrise.models import Item
from highrise.models import AnchorPosition
import requests
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import BaseBot
from collections import UserDict
from highrise.models import SessionMetadata, User
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
import random
from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task
import discord
from discord.ext import commands
from discord.ext.commands import Bot

class _2M0(BaseBot):
  dancs = [
    "idle-loop-sitfloor", "emote-tired", "emoji-thumbsup", "emoji-angry",
    "dance-macarena", "emote-hello", "dance-weird", "emote-superpose",
    "idle-lookup", "idle-hero", "emote-wings", "emote-laughing", "emote-kiss",
    "emote-wave", "emote-hearteyes", "emote-theatrical", "emote-teleporting",
    "emote-slap", "emote-ropepull", "emote-think", "emote-hot",
    "dance-shoppingcart", "emote-greedy", "emote-frustrated", "emote-float",
    "emote-baseball", "emote-yes", "idle_singing", "idle-floorsleeping",
    "idle-enthusiastic", "emote-confused", "emoji-celebrate", "emote-no",
    "emote-swordfight", "emote-shy", "dance-tiktok2", "emote-model",
    "emote-charging", "emote-snake", "dance-russian", "emote-sad",
    "emote-lust", "emoji-cursing", "emoji-flex", "emoji-gagging",
    "dance-tiktok8", "dance-blackpink", "dance-pennywise", "emote-bow",
    "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis",
    "emote-maniac", "emote-energyball", "emote-frog", "emote-cute",
    "dance-tiktok9", "dance-tiktok10", "emote-pose7", "emote-pose8",
    "idle-dance-casual", "emote-pose1", "emote-pose3", "emote-pose5",
    "emote-cutey", "emote-Relaxing", "emote-model", "emote-fashionista",
    "emote-gravity", "emote-zombierun", "emoji-ceilebrate", "emoji-floss",
    "emote-Relaxing ", "emote-punkguitar", "dance-tiktok9", "dance-weird",
    "emote-punkguitar", "idle-uwu"
    "emote-bow", "emote-cursty", "dance-breakdance", "emote-creepycute","emote-headblowup","idle-guitar"
  ]

  def __init__(self):
    self.following_username = None
    self.food_prices = {
        "همبرغر": 30,
        "تاكو": 25,
        "نودلز": 15,
        "سوشي": 100,
        "بيتزا": 5,
        "فلافل": 3,
        "الهوت دوج": 35,
        "الارز": 25,
        "بوبا": 50,
        "تحليه": 45,
    }
    super().__init__()
    self.user_positions = {}
    self.is_dancing = False

  async def on_start(self, SessionMetadata: SessionMetadata) -> None:
    try:
        await self.highrise.walk_to(Position(11,0,5, "FrontLeft"))
        await self.highrise.chat("انا جييييييت ")
    except Exception as e:
        print(f"error : {e}")

    print("2M0")

  async def teleport_user_next_to(self, target_username: str, requester_user: User):

      room_users = await self.highrise.get_room_users()
      requester_position = None

      for user, position in room_users.content:
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


  async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
    await self.highrise.send_whisper(user.id, " رقصات من 1 الى 100 ✨📣") 
    await self.highrise.chat(f"وصل الحلو {user.username} 💖")
    await self.highrise.chat(f"للأوامر اكتب (اوامر) {user.username}")
    await self.highrise.react("wave", user.id)
  async def on_user_leave(self, user: User) -> None:
    await self.highrise.chat(f"راح للاسف{user.username}💔")
    await self.highrise.send_emote("emote-wave")



  async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
    try:
        await self.highrise.react(reaction, user.id) 
    except:
        pass




    try:
        emote_id = random.choice(self.dancs)
        await self.highrise.send_emote(emote_id, user.id)
    except:
        print(f"{emote_id}")







  async def handle_order(self, user: User, message: str):
    food_prices = {
        "همبرغر": 30,
        "تاكو": 25,
        "نودلز": 15,
        "سوشي": 100,
        "بيتزا": 5,
        "فلافل": 3,
        "الهوت دوج": 35,
        "الارز": 25,
        "بوبا": 50,
        "تحليه": 45,
    }
    items = message.split()[1:]
    items = [item for item in items if item != "و"]
    total_price = 0
    ordered_items = []
    for item in items:
        item_price = food_prices.get(item)
        if item_price:
            total_price += item_price
            ordered_items.append(item)
        else:
            await self.highrise.chat(f"العنصر {item} غير موجود في قائمة الطعام.")


    if total_price > 0:
        await self.highrise.chat(f"تم حساب مجموع الطلب: ${total_price}")

        await asyncio.sleep(5) 
        await self.highrise.walk_to(Position(17, 0, 5))
        await asyncio.sleep(4) 


        await self.highrise.walk_to(Position(18, 0, 17))
        await asyncio.sleep(5)
        await self.highrise.walk_to(Position(17, 0, 5))
        await asyncio.sleep(3) 
        await self.highrise.chat(f"تفضل طلبك جاهز ")

    else:
          await self.highrise.chat("الطلب فارغ أو لا يحتوي على عناصر صالحة.")





  async def follow_user(self, target_username: str):
    while self.following_username == target_username:
        # ابحث عن موقع المستخدم المستهدف في الغرفة
        response = await self.highrise.get_room_users()
        target_user_position = None
        for user_info in response.content:
            if user_info[0].username.lower() == target_username.lower():
                target_user_position = user_info[1]
                break

        if target_user_position:
            nearby_position = Position(target_user_position.x + 1.0, target_user_position.y, target_user_position.z)
            await self.highrise.walk_to(nearby_position)

            await asyncio.sleep(1)  # انتظر 5 ثواني مثلاً

  async def on_user_move(self, user: User, pos: Position) -> None:
     self.user_positions[user.username] = pos



  async def on_chat(self, user: User, message: str) -> None:


    if message.lower().startswith("الحق @"):
      if user.username in ["2M30","Y__N1", "2M0"]:
        target_username = message.split("@")[1].strip()

        if target_username.lower() == self.following_username:
            await self.highrise.chat(f"I am already following {user.username}.")
        else:
            self.following_username = target_username
            await self.highrise.chat(f"بتبعه لعيونك يا قمر🌚❤{target_username}.")
            # بمجرد تعيين المستخدم الذي يجب متابعته، استدعِ وظيفة follow_user
            await self.follow_user(target_username)
    elif message.lower() == "توقف":
        self.following_username = None
        await self.highrise.chat("تم التوقف عن التتبع.")


    elif "اوامر" in message:
      await self.highrise.send_whisper(user.id, "اوامر البوت 👇👇👇")
      await self.highrise.chat(f"المنيو-يا بوت-اسعار - اوامر!- رقصات من 1 الى 100 ك-رقصات بلعربي-رقصات بلأنجليزي -ترقص الناس-اكتب اعطيني +طلبك-رقصني-صعدني-نزلني-ويتم اضافة-الساعة {user.username}")

    elif "يا بوت" in message:
      await self.highrise.chat(f"شو تريد 🌚 {user.username}")
    elif "الساعة" in message:
          await self.highrise.chat(f"الساعة هي {datetime.now().strftime('%H:%M:%S')}")


    if message.startswith("المنيو"):
        food_menu = (
            "🍔 همبرغر\n"
            "🌯 تاكو\n"
            "🍜 نودلز\n"
            "🍣 سوشي\n"
            "🥘 بيتزا\n"
            "🧆🥙 فلافل\n"
            "🌭 هوت دوج\n"
            "🍚 ارز\n"
            "🧋 بوبا\n"
            "🍬🍫🍪🍩🍭🧁 تحليه\n"
            "اكتب اسعار الوجبات  عشان تجيك الاسعار\n"
            "اكتب اعطيني + طلبك عشان احضر لك الطلب"
        )
        await self.highrise.chat(food_menu)

    if message.startswith("اسعار"):
        food_prices = (
            "همبرغر بي $30\n"
            "تاكو بي $25\n"
            "نودلز بي $15\n"
            "سوشي بي $100\n"
            "بيتزا بي $5\n"
            "فلافل بي $3\n"
            "الهوت دوج بي $35\n"
            "الارز بي $25\n"
            "بوبا بي $50\n"
            "تحليه بي $45"
        )
        await self.highrise.chat(food_prices)

    if message.startswith("اعطيني"):
      await self.handle_order(user, message)



    if message.startswith("سحب"):
      if user.username in ["2M30","Y__N1", "2M0", "S_O_L_L_Y","irai.i","9.as","A_c1","Shima2007","juju_123356","_.ioy","8ni_","7.0sh","H_3F","R0__aa","oowowowi"]:
       target_username = message.split("@")[-1].strip()
       if target_username not in ["2M0", "Y__N1","2M30"]:
          await self.teleport_user_next_to(target_username, user)

    if message.startswith("جيبلي"):
      if user.username in ["2M30","Y__N1", "2M0", "S_O_L_L_Y","irai.i","9.as","A_c1","Shima2007","juju_123356","_.ioy","8ni_","7.0sh","H_3F","R0__aa","oowowowi"]:
       target_username = message.split("@")[-1].strip()
       if target_username not in ["2M0", "Y__N1"]:
          await self.teleport_user_next_to(target_username, user)

    dance_emotes = {
      "float": "emote-float",
      "pose1": "dance-tiktok2",
      "pose1": "emote-pose1",
      "shoppingcart": "dance-shoppingcart",
      "russian": "dance-russian",
      "sing": "idle_singing",
      "enthused": "idle-enthusiastic",
      "casual": "idle-dance-casual",
      "sit": "idle-loop-sitfloor",
      "lust": "emote-lust",
      "greedy": "emote-greedy",
      "bow": "emote-bow",
      "crusty": "emote-curtsy",
      "snowball": "emote-snowball",
      "snowangel": "emote-snowangel",
      "confused": "emote-confused",
      "teleporting": "emote-teleporting",
      "sword": "emote-swordfight",
      "energyball": "emote-energyball",
      "tiktok8": "dance-tiktok8",
      "kpop": "dance-blackpink",
      "model": "emote-model",

      "wise": "dance-pennywise",
      "tiktok10": "dance-tiktok10",
      "telekinesis": "emote-telekinesis",
      "hot": "emote-hot",
      "weird": "dance-weird",
      "pose7": "emote-pose7",
      "pose8": "emote-pose8",
      "penguin": "dance-pinguin",
      "pose3": "emote-pose3",
      "blush": "emote-shy2",
      "pose5": "emote-pose5"
    }

    if message.startswith("Loop") and not self.is_dancing:
      dance_number = message.split(" ")[1]
      dance_emote = dance_emotes.get(dance_number)
      if dance_emote:
          self.is_dancing = True
          while self.is_dancing:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote(dance_emote, user.id)
      else:
          await self.highrise.chat("الرقم غير صالح")
    elif message.startswith("وقف رقص"):
      self.is_dancing = False
      await self.highrise.chat("تم إيقاف الرقص")
    if message.startswith("0"):
      await self.highrise.send_emote("emote-float", user.id)
    if message.startswith("1"):
      await self.highrise.send_emote("emote-snowball", user.id)
    if message.startswith("2"):
      await self.highrise.send_emote("dance-tiktok2", user.id)   
    if message.startswith("3"):
      await self.highrise.send_emote("emote-pose1", user.id)
    if message.startswith("4"):
      await self.highrise.send_emote("dance-shoppingcart", user.id)
    if message.startswith("5"):
      await self.highrise.send_emote("dance-russian", user.id)
    if message.startswith("6"):
      await self.highrise.send_emote("idle_singing", user.id)
    if message.startswith("7"):
      await self.highrise.send_emote("idle-enthusiastic", user.id)   
    if message.startswith("8"):
      await self.highrise.send_emote("idle-dance-casual", user.id)   
    if message.startswith("9"):
      await self.highrise.send_emote("idle-loop-sitfloor", user.id)
    if message.startswith("10"):
      await self.highrise.send_emote("emote-lust", user.id)
    if message.startswith("11"):
      await self.highrise.send_emote("emote-greedy", user.id)
    if message.startswith("12"):
      await self.highrise.send_emote("emote-bow", user.id)
    if message.startswith("13"):
      await self.highrise.send_emote("emote-curtsy", user.id)
    if message.startswith("14"):
      await self.highrise.send_emote("emote-lust", user.id)
    if message.startswith("15"):
      await self.highrise.send_emote("emote-snowangel", user.id)
    if message.startswith("16"):
      await self.highrise.send_emote("emote-confused", user.id)
    if message.startswith("17"):
      await self.highrise.send_emote("emote-teleporting", user.id)
    if message.startswith("18"):
      await self.highrise.send_emote("emote-swordfight", user.id)
    if message.startswith("19"):
      await self.highrise.send_emote("emote-energyball", user.id)
    if message.startswith("20"):
      await self.highrise.send_emote("dance-tiktok8", user.id)
    if message.startswith("21"):
      await self.highrise.send_emote("dance-blackpink", user.id)
    if message.startswith("22"):
      await self.highrise.send_emote("emote-model", user.id)
    if message.startswith("23"):
      await self.highrise.send_emote("dance-pennywise", user.id)
    if message.startswith("24"):
      await self.highrise.send_emote("dance-tiktok10", user.id)
    if message.startswith("25"):
      await self.highrise.send_emote("emote-telekinesis", user.id)
    if message.startswith("26"):
      await self.highrise.send_emote("emote-hot", user.id)
    if message.startswith("27"):
      await self.highrise.send_emote("dance-weird", user.id)
    if message.startswith("28"):
      await self.highrise.send_emote("emote-pose7", user.id)
    if message.startswith("29"):
      await self.highrise.send_emote("emote-pose8", user.id)
    if message.startswith("30"):
      await self.highrise.send_emote("emote-pose3", user.id)
    if message.startswith("31"):
      await self.highrise.send_emote("emote-pose5", user.id)  
    if message.startswith("32"):
      await self.highrise.send_emote("emoji-flex", user.id)  
    if message.startswith("31"):
      await self.highrise.send_emote("emote-creepycute", user.id)  
    if message.startswith("31"):
      await self.highrise.send_emote("emote-pose5", user.id)   

    if message.startswith("tip "):
              try:
                  tip_amount = int(message.split(" ")[1])
              except IndexError:
                  await self.highrise.chat("يرجى تحديد الكمية المراد إرسالها.")
                  return
              except ValueError:
                  await self.highrise.chat("الرجاء إدخال رقم صحيح.")
                  return
              if user.username in [ "sll0", "Y__N1" ]:
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
                      await self.highrise.chat("ليس لدي الذهب الكافي لمنح الجميع")

    if "نزلني" in message or "نزلني" in message:
            try:
                await self.highrise.teleport(f"{user.id}", Position(x=0.5, y=0.0, z=4.5, facing='FrontRight'))
            except:
                print("error 3")

    if "صعدني" in message or "طلعني" in message:
      try:
          await self.highrise.teleport(f"{user.id}", Position(1, 6.6, 5))
      except:
          print("error 3")

    if "vip" in message or "vip" in message:
      if user.username in ["2M30","Y__N1", "2M0", "S_O_L_L_Y","irai.i","9.as","A_c1","Shima2007","juju_123356","_.ioy","8ni_","7.0sh","H_3F","R0__aa","oowowowi"]:
        try:
          await self.highrise.teleport(f"{user.id}", Position(x=9.5, y=15.75, z=9.5, facing='FrontLeft'))
        except:
          print("error 3")



    if message.startswith("Kick"):
            if user.username == ["2M0","2M30"]:
                pass
            else:
                await self.highrise.chat("You do not have permission to use this command.")
                return
            #separete message into parts
            parts = message.split()
            #check if message is valid "kick @username"
            if len(parts) != 2:
                await self.highrise.chat("Invalid kick command format.")
                return
            #checks if there's a @ in the message
            if "@" not in parts[1]:
                username = parts[1]
            else:
                username = parts[1][1:]
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #kick user
            try:
                await self.highrise.moderate_room(user_id, "kick")
            except Exception as e:
                await self.highrise.chat(f"{e}")
                return
            #send message to chat
            await self.highrise.chat(f"{username} has been kicked from the room.")

    if message.startswith("move"):
            room_dictionary = {"room_1":"<>",
                               "room_2":"<>",}
            if user.username != "2M0":
                await self.highrise.chat("You do not have permission to use this command.")
                return
            parts = message.split()
            if len(parts) != 3:
                await self.highrise.chat("Invalid move command format.")
                return
            command, username, room = parts
            if "@" not in username:
                username = username
            else:
                username = username[1:]
            if room not in room_dictionary:
                await self.highrise.chat("Invalid room, please specify a valid room.")
                return
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #move user
            try:
                await self.highrise.move_user_to_room(user_id, room_dictionary[room])
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
                return

    if message.startswith("users"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} users in the room")

    if message.startswith("محفظتك"):
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.chat(f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

    if message.lower().startswith("/voiceremove "):
            try:
                command, username = message.split(" ")
            except:
                await self.highrise.chat("Invalid command, please use /voiceremove <username>")
                return
            #gets room users and check if the user is in the room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, position in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat(f"User '{username}' not found.")
                return

            #checks if the user is already in the voice list
            voice_list = (await self.highrise.get_voice_status()).users
            if user_id not in voice_list:
                await self.highrise.chat(f"User '{username}' is not in the voice list.")
                return

            await self.highrise.remove_user_from_voice(user_id)
            await self.highrise.chat(f"Removed '{username}' from the voice list.")

    if message.lstrip().startswith("add"):
      if user.username.lower() in [ "" , "Y__N1"]:
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]
              usernames = [user.username.lower() for user in users]

              parts = message[1:].split()
              args = parts[1:]

              if len(args) < 2:
                      await self.highrise.send_whisper(user.id, "Use: Command > Name > Place ")
                      return
              elif args[0][0] != "@":
                      await self.highrise.send_whisper(user.id, f" Incorrect format  '@username'.")
                      return
              elif args[0][1:].lower() not in usernames:
                      await self.highrise.send_whisper(user.id, f"{args[0][1:]}Not in the room.")
                      return

              position_name = " ".join(args[1:])
              if position_name == 'VIP2':
                      dest = Position(19, 4.5, 17)

              elif position_name == 'VIP1':
                      dest = Position(16, 10.5, 9)

              elif position_name == 'DJ':
                      dest = Position(17, 12, 3)

              elif position_name == 'Y__N1':
                      dest = Position(15, 7, 6)  

              elif position_name == 'down':
                      dest = Position(5, 0, 6)  

              else:
                      return await self.highrise.send_whisper(user.id, f"  The site is wrong ")
              user_id = next ((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
              if not user_id:
                      await self.highrise.send_whisper(user.id, f"User {args[0][1:]} unavailable ")
                      return

              await self.highrise.teleport(user_id, dest)
              await self.highrise.send_whisper(user.id, f" move  {args[0][1:]} to ({dest.x}, {dest.y}, {dest.z})")
      else:
              await self.highrise.send_whisper(user.id, " You can't fix this ")
    else:
          pass

    if message.lower().startswith("/equip"):
      await self.highrise.set_outfit(outfit=[
            Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
            Item(type='clothing', amount=1, id='hair_front-n_malenew09', account_bound=False, active_palette=1),
            Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows17', account_bound=False, active_palette=1),
            Item(type='clothing', amount=1, id='mouth-basic2018vampteeth', account_bound=False, active_palette=3),
            Item(type='clothing', amount=1, id='nose-n_basic2018newnose20',),
            Item(type='clothing', amount=1, id='shirt-f_marchingband', account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id='pants-n_room12019rippedpantsblack', account_bound=False, active_palette=-1),
            Item(type='clothing',amount=1, id='shoes-n_room32019socksneakersblack', account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id='eye-n_basic2018maleround', account_bound=False, active_palette=7),
            Item(type='clothing', amount=1, id='hair_back-n_malenew09', account_bound=False, active_palette=-1),
            ])



    if "جاذبية" in message:
      try:
        emote_id = "emote-gravity"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "رقصني" in message:
      try:
        emote_id = random.choice(self.dancs)
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "You got a tip!" in message:
      try:
        emote_id = "dance-tiktok2"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if message.startswith("زومبي"):
      if user.username in ["2M30","Y__N1", "2M0", "S_O_L_L_Y","irai.i","9.as","A_c1","Shima2007","juju_123356","_.ioy","8ni_","7.0sh","H_3F","R0__aa","oowowowi"]:
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-zombierun", roomUser.id)

    if "طيرني" in message:
      try:
        await self.highrise.send_emote('emote-float', user.id)
      except Exception as e:
        print(f"Error: {e}")



    if message.startswith("wallet"):
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.chat(f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

    if message.startswith("users"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} users in the room")

    if message.lower().startswith("/getoutfit"):
            response = await self.highrise.get_my_outfit()
            for item in response.outfit:
                await self.highrise.chat(item.id)

  async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
    response = await self.highrise.get_messages(conversation_id)
    if isinstance(response, GetMessagesRequest.GetMessagesResponse):
        message = response.messages[0].content
    print (message)
    if message == "You got a tip!":
        await self.highrise.send_message(conversation_id, "شكرا على التيبس 🌚")



  async def grant_gold_to_all(self, amount):
          bot_wallet = await self.highrise.get_wallet()
          bot_amount = bot_wallet.content[0].amount
          response = await self.highrise.get_room_users()
          num_users = len(response.content)
          total_gold = amount * num_users
          if bot_amount >= total_gold:
              for content in response.content:
                  user_id = content[0].id
                  await self.highrise.tip_user(user_id, f"gold_bar_{amount}")
          else:
              await self.highrise.chat("ليس لدي الذهب الكافي لمنح الجميع")
