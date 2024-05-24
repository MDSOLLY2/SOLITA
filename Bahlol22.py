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
import datetime

class S_O_L_L_Y(BaseBot):

    message_count = {}
    def check_level(self, user_id):
        level = self.message_count.get(user_id, 0) // 10
        return level

    def __init__(self):
      self.is_dancing = False
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

    async def on_start(self, session_metadata: SessionMetadata) -> None:
      try:
          print("Bahlol22")
          await self.highrise.walk_to(AnchorPosition(entity_id='1de73a3dbbc469f77a06ad6e', anchor_ix=0))
          await self.highrise.chat("هلا وغلا تحب تشرب ايه ؟")
      except Exception as e:
          print(f"error : {e}")


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
              await self.highrise.chat(f"العنصر {item} غير موجود في المنيو.")


      if total_price > 0:
          await self.highrise.chat(f"تم حساب مجموع الطلب: ${total_price}")

          await asyncio.sleep(5)
          await self.highrise.walk_to(Position(x=16.0, y=9.0, z=1.5, facing='FrontRight'))
          await asyncio.sleep(3) 
          await self.highrise.chat(f"تفضل طلبك جاهز ")
          await asyncio.sleep(5)
          await self.highrise.walk_to(AnchorPosition(entity_id='1de73a3dbbc469f77a06ad6e', anchor_ix=0))

      else:
            await self.highrise.chat("الطلب فارغ أو لا يحتوي على عنصر في المنيو.")


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


    async def on_user_join(self, user: User, position: Position) -> None:
      await self.highrise.chat(f"ولكم اتمنى منك دعوه لاخوتنا في فلسطين🇵🇸🖤")
      await self.highrise.chat("هلا وغلا تحب تشرب ايه ؟")
      await self.highrise.react("wave", user.id)

    async def on_user_leave(self, user: User) -> None:
      await self.highrise.chat(f"راح {user.username} مع الرياح")
      await self.highrise.send_emote("emote-sad")

      if user.username in ["youssef1230"]:
        await self.highrise.chat(f"خرج {user.username} صاحب الروم💔😔")
        await self.highrise.send_emote("emote-sad")


    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
      response = await self.highrise.get_messages(conversation_id)
      if isinstance(response, GetMessagesRequest.GetMessagesResponse):
          message = response.messages[0].content
      print (message)
      if message == "You got a tip!":
          await self.highrise.send_message(conversation_id, "شكرا على التيبس 🌚")


    async def on_chat(self, user: User, message: str) -> None:
      if user.id not in self.message_count:
        self.message_count[user.id] = 0
    # ... (باقي الأوامر هنا)

      if "منيو" in message:
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
            "تحليه بي $45\n"
        )
        await self.highrise.chat(food_prices)

      if message.startswith("اعطيني"):
        await self.handle_order(user, message)

      if "يا بوت" in message:
          await self.highrise.chat(f"مش فاضي {user.username}")
      if "الساعة" in message:
        await self.highrise.chat(f"الساعة هي {datetime.datetime.now().strftime('%H:%M:%S')}")


      if message.startswith("move"):
            room_dictionary = {"room_1":"<>",
                               "room_2":"<>",}
            if user.username != "Xx_mohamd_xX":
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

      if message.lower().startswith("/getoutfit"):
        response = await self.highrise.get_my_outfit()
        for item in response.outfit:
            await self.highrise.chat(item.id)

      if message.startswith(("React", "react", "وزع")) and user.username in ["S_O_L_L_Y"]:
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
          await self.highrise.chat(f"مش فاضي {user.username}")
          await self.highrise.react("heart", user.id)

      #محفظة البوت
      if message.startswith(("محفظتك","wallet")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
          wallet = (await self.highrise.get_wallet()).content
          await self.highrise.send_whisper(user.id,f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

      #كم واحد برومك
      if message.startswith("users"):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} users in the room")

      if message.startswith("back") and user.username in ["S_O_L_L_Y"]:
        await self.highrise.walk_to(AnchorPosition(entity_id='1de73a3dbbc469f77a06ad6e', anchor_ix=0))

      if message in ["طيرنى","طيرني"]:
        await self.highrise.teleport(f"{user.id}", Position(x=3.0, y=0.0, z=4.0, facing='FrontRight'))
        await asyncio.sleep (3)
        await self.highrise.teleport(f"{user.id}", Position(x=14.5, y=9.0, z=23.5, facing='FrontLeft'))
        await asyncio.sleep (3)
        await self.highrise.teleport(f"{user.id}", Position(x=15.5, y=17.75, z=7.0, facing='FrontRight'))
        await asyncio.sleep(3)
        await self.highrise.teleport(f"{user.id}", Position(x=8.0, y=9.100000381469727, z=6.5, facing='FrontLeft'))
        await asyncio.sleep(3)
        await self.highrise.teleport(f"{user.id}", Position(x=11.0, y=0.75, z=11.0, facing='FrontRight'))

      if message in ["أوامر","اوامر","الاوامر","الأوامر"]:
        try:
          await self.highrise.chat(f"اوامر البوت 👇👇👇")
          await self.highrise.chat(f"المنيو -يا بوت -اسعار -اوامر! -رقصات من 1 الى 100 ك -رقصات بلعربي -ترقص الناس -اكتب اعطيني+طلبك -رقصني -صعدني -نزلني -طيرني.")
        except Exception as e:
            print(f"Error: {e}")

      if "😂" in message:
        try:
          emote_id = "emote-laughing"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")


      #لو عايز يتبع حد
      if message.lower().startswith(("اتبع @","الحق @")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
          target_username = message.split("@")[1].strip()

          if target_username.lower() == self.following_username:
              await self.highrise.chat(f"I am already following {user.username}.")
          else:
              self.following_username = target_username
              await self.highrise.chat(f"بلحقه لعيونك{target_username}.")
              # بمجرد تعيين المستخدم الذي يجب متابعته، استدعِ وظيفة follow_user
              await self.follow_user(target_username)
      elif message.lower() == "توقف":
          self.following_username = None
          await self.highrise.chat("حاضر")