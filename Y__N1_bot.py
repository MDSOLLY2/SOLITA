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
    dances = [ "emote-superpose", "emote-laughing", "emote-kiss", "emote-wave", "emote-teleporting", "emote-hot ", "emote-greedy", "emote-float", "emote-confused", "emote-swordfight", "emote-model", "emote-charging", "emote-snake", "emote-lust", "emote-bow", "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis", "emote-maniac", "emote-energyball", "emote-frog", "emote-cute","emote-pose7 ", "emote-pose8", "emote-pose1", "emote-pose3", "emote-timejump", "emote-sleigh", "emote-punkguitar", "emote-zombierun", "emote-fashionista", "emote-gravity", "emote-shy2",

            "emoji-celebrate", "emoji-cursing", "emoji-gagging","emoji-flex",

              "sit-relaxed",

            "dance-macarena", "dance-weird", "dance-shoppingcart", "dance-tiktok2", "dance-russian", "dance-tiktok8", "dance-blackpink", "dance-pennywise","dance-tiktok9", "dance-tiktok10", "dance-jinglebell", "dance-pinguin", "dance-creepypuppet", "dance-icecream", "dance-wrong", "dance-anime","dance-kawai",

            "idle_singing", "idle-enthusiastic", "idle-dance-casual", "idle-loop-sitfloor", "idle-nervous", "idle-toilet", "idle-uwu", "idle-dance-tiktok4 ",

      # ... (أنواع الرقصات هنا)
  ]

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
          print("Y__N1_bot")
          await self.highrise.walk_to(Position(x=15.0, y=0.0, z=9.5, facing='FrontLeft'))
          await self.highrise.chat("هلا وغلا نورتونا")
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
          await self.highrise.walk_to(Position(x=12.0, y=0.0, z=20.5, facing='FrontRight'))
          await asyncio.sleep(3) 
          await self.highrise.chat(f"تفضل طلبك جاهز ")
          await asyncio.sleep(5)
          await self.highrise.walk_to(Position(x=15.0, y=0.0, z=9.5, facing='FrontLeft'))

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
      if user.username in ["luciferEgypt"]:
        await self.highrise.chat(f"صاحب الروم جااا {user.username}")
      if user.username == "_xA7m3d":
        await self.highrise.chat("دخل صاحب البوت")

      user_privileges = await self.highrise.get_room_privilege(user.id)
      if (user_privileges.moderator):
        await self.highrise.chat(f"دخل المشرف اقوى تحيه♥❤🫡 {user.username}")
      if (user_privileges.designer):
        await self.highrise.chat(f"دخل المصمم اقوى تحيه♥❤🫡 {user.username}")

      if user.username not in ["_xA7m3d","luciferEgypt"]:
        await self.highrise.send_whisper(user.id, "ولكم اتمنى منك دعوه لاخوتنا في فلسطين🇵🇸🖤🇬") 
        await self.highrise.chat(f"هلا حتا تخلي الكل يرقص اعطيني 10g {user.username}")
        await self.highrise.chat(f"للأوامر اكتب (اوامر) {user.username}")
        await self.highrise.react("wave", user.id)

      # تشغيل رقصة للبوت عند دخول المستخدم
      try:
            emote_id = random.choice(self.dances)
            await self.highrise.send_emote(emote_id)
      except Exception as e:
            print(f"Error: {e}")
      # تشغيل رقصة للاعب عند دخول المستخدم
      try:
           emote_id = random.choice(self.dances)
           await self.highrise.send_emote(emote_id, user.id)
      except Exception as e:
           print(f"Error: {e}")

    async def on_user_leave(self, user: User) -> None:
        await self.highrise.chat(f"راح {user.username} مع الرياح")
        await self.highrise.send_emote("emote-sad")

        if user.username == "_xA7m3d":
          await  self.highrise.chat(f"خرج {user.username} صاحب البوت💔💔")
          await self.highrise.send_emote("emote-sad")

        if user.username in ["luciferEgypt"]:
          await self.highrise.chat(f"خرج {user.username} صاحب الروم💔😔")
          await self.highrise.send_emote("emote-sad")
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator):
          await self.highrise.chat(f"خرج {user.username} مشرف الروم💔😔")
          await self.highrise.send_emote("emote-sad")
        if (user_privileges.designer):
          await self.highrise.chat(f"خرج {user.username} مصمم الروم💔😔")
          await self.highrise.send_emote("emote-sad")

        try:
            emote_id = random.choice(self.dances)
            await self.highrise.send_emote(emote_id, user.id)
        except:
              print(f"{emote_id}")


    #لو عايز الهوست ينقل حد بيراكت
    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:

      if reaction == "thumbs":
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","_xA7m3d","luciferEgypt"] and user.username not in ["Y__N1_bot"]):
          target_username = receiver.username
          await self.teleport_user_next_to(target_username, user)


    #لو عايز ينقلك لما تدفع للبوت
    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
      if tip.amount == 10 and receiver.username in ["Y__N1_bot"]:
        await asyncio.sleep(1)
      try:
          emote_id = random.choice(self.dances)
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:       
            await self.highrise.send_emote(emote_id, roomUser.id)
      except:
          print(f"{emote_id}")

      if tip.amount == 5 and receiver.username in ["Y__N1_bot"]:
        await asyncio.sleep(1)
        await self.highrise.teleport(sender.id, Position(2.5, 19.0, 0.5, 'FrontRight'))


    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
      response = await self.highrise.get_messages(conversation_id)
      if isinstance(response, GetMessagesRequest.GetMessagesResponse):
          message = response.messages[0].content
      print (message)
      if message == "You got a tip!":
          await self.highrise.send_message(conversation_id, "شكرا على التيبس 🌚")


    async def handel_send_message(self, user: User, message: str):
      response = await self.highrise.get_messages(conversation_id)
      if isinstance(response, GetMessagesRequest.GetMessagesResponse):
          message = response.messages[0].content
      print (message)
      if message == "You got a tip!":
          await self.highrise.send_message(conversation_id, "شكرا على التيبس 🌚")
      if message in ["اهلا", "هلا"]:
        await self.highrise.send_message(conversation_id, "اهلا بك 🌚")
      if message == "مساعدة":
        await self.highrise.send_message(conversation_id, "اكتب /help لمعرفة الاوامر")
        if message == "/help":
          await self.highrise.send_message(conversation_id, "لشراء روبوت اكتب /buy للأوامر اكتب /اوامر شراء بوت دائم /24h")
          if message == "/اوامر":
              await self.highrise.send_message(conversation_id, "المنيو-يا بوت-اوامر-رقصات من 1 الي 32-صعدني-نزلني-رقصني-ويت اضافة المزيد😊")
              if message == "/buy":
                await self.highrise.send_message(conversation_id, "هناك الكثير من الروبتات الذي يمكنني صنعها مثل : روبوت رقص فقط لمعرفة سعره اكتب(بوت رقص) -- روبوت ترحيب اكتب (بوت ترجيب) -- بوت ترحيب ورقص(بوت ترحيب ورقص)--بوت يودع ويرحب(بوت يودع ويرحب)--بوت كامل(super)-- والمزيد")
                if message == "بوت رقص":
                  await self.highrise.send_message(conversation_id, "السعر: 500")
                  if message == "بوت ترحيب":
                    await self.highrise.send_message(conversation_id, "السعر: 200")
                    if message == "بوت ترحيب ورقص":
                      await self.highrise.send_message(conversation_id, "السعر: 700")
                      if message == "بوت يودع ويرحب":
                        await self.highrise.send_message(conversation_id, "السعر: 200")
                        if message == "بوت كامل":
                          await self.highrise.send_message(conversation_id, "السعر: 5k")
                          if message == "/24":
                            await self.highrise.send_message(conversation_id, "السعر اليوم: 500 ,, سعر الاسبوع :1k ,, سعر الشهر : 2.5k ,, سعر السنة : 10k")


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

      if message.startswith(("React", "react", "وزع")) and user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]:
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
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
          wallet = (await self.highrise.get_wallet()).content
          await self.highrise.send_whisper(user.id,f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

      #كم واحد برومك
      if message.startswith("users"):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} users in the room")

      if message.startswith("ارجع مكانك"):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
          await self.highrise.walk_to(Position(x=15.0, y=0.0, z=9.5, facing='FrontLeft'))

      if message.startswith(("vip","Vip")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
          await self.highrise.teleport(user.id, Position(2.5, 19.0, 0.5, 'FrontRight'))

      if message.startswith(("جيبلي","اسحب")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
          target_username = message.split("@")[-1].strip()
          if target_username not in ["S_O_L_L_Y"]:
            await self.teleport_user_next_to(target_username, user)

      if message in ["نزلني","دور 1","نزلنى"]:
        try:
            await self.highrise.teleport(f"{user.id}", Position(x=16.5, y=0.25, z=29.5, facing='FrontRight'))
        except:
          print("error 3")

      if  message in ["طلعني","صعدني","صعدنى","طلعنى"]:
        try:
            await self.highrise.teleport(f"{user.id}", Position(x=16.5, y=8.350000381469727, z=29.5, facing='FrontRight'))
        except:
          print("error 3")

      if message in ["طيرنى","طيرني"]:
        await self.highrise.teleport(f"{user.id}", Position(2.5, 19.0, 0.5, 'FrontRight'))
        await asyncio.sleep (3)
        await self.highrise.teleport(f"{user.id}", Position(x=16.5, y=8.350000381469727, z=29.5, facing='FrontRight'))
        await asyncio.sleep (3)
        await self.highrise.teleport(f"{user.id}", Position(x=16.5, y=0.25, z=29.5, facing='FrontRight'))
        await asyncio.sleep(3)
        await self.highrise.teleport(f"{user.id}", Position(x=15.0, y=0.0, z=9.5, facing='FrontLeft'))
        await asyncio.sleep(3)
        await self.highrise.teleport(f"{user.id}", Position(x=14.0, y=0.0, z=14.5, facing='FrontLeft'))
        await asyncio.sleep(3)
        await self.highrise.teleport(f"{user.id}", Position(x=7.5, y=0.25, z=6.5, facing='FrontRight'))

      elif message in ["طولي"]:
          try:
              height_cm = random.randint(150, 190)
              await self.highrise.chat(f"                              {user.username} {height_cm} Cm 💖")
          except Exception as e:
              print(f"Error: {e}")
      elif message in ["وزني"]:
          try:
              weight_kg = random.randint(60, 99)
              await self.highrise.chat(f"                              {user.username} {weight_kg} Kg 💖")
          except Exception as e:
              print(f"Error: {e}")
      elif message in ["عمري"]:
          try:
              weight_kg = random.randint(8, 30)
              await self.highrise.chat(f"                              {user.username} {weight_kg} Years 💖")
          except Exception as e:
              print(f"Error: {e}")

      if message in ["أوامر","اوامر","الاوامر","الأوامر"]:
        try:
          await self.highrise.chat(f"اوامر البوت 👇👇👇")
          await self.highrise.chat(f"المنيو -يا بوت -اسعار -اوامر! -رقصات من 1 الى 100 ك -رقصات بلعربي -ترقص الناس -اكتب اعطيني+طلبك -رقصني -صعدني -نزلني -طيرني.")
        except Exception as e:
            print(f"Error: {e}")


      #لو عايز ترقص رقصه عشوائيه 
      if message in ["Dance","dance","!Dance","!dance","رقصنى","رقصني","0"]:
        try:
            emote_id = random.choice(self.dances)
            await self.highrise.send_emote(emote_id, user.id)
        except Exception as e:
            print(f"Error: {e}")
      #لو عايز الروم كلها ترقص رقصه عشوائيه
      if message.startswith(("Dance all","dance all","!Dance all","!dance all","رقصنا","All 0","all 0","0 All","0 all")):
          emote_id = random.choice(self.dances)
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
            await self.highrise.send_emote(emote_id, roomUser.id)

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
      if message.startswith("33"):
        await self.highrise.send_emote("emote-creepycute", user.id)  
      if message.startswith("34"):
        await self.highrise.send_emote("emote-pose5", user.id)

      if "ريلاكس" in message:
        try:
          emote_id = "emote-Relaxing"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print("error 3")

      if "جاذبية" in message:
        try:
          emote_id = "emote-gravity"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print("error 3")

      if "فاشون" in message:
        try:
          emote_id = "emote-fashionista"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print("error 3")

      if "اهز" in message:
        try:
          emote_id = "dance-blackpink"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print("error 3")

      if "مح" in message:
        try:
          emote_id = "emote-kiss"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print("error 3")

      if "هلا" in message:
        try:
          emote_id = "emote-hello"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print("error 3")

      if "وينزداي" in message:
        try:
          emote_id = "dance-weird"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print("error 3")

      if "مح" in message:
        try:
          emote_id = "emote-kiss"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "شكرا" in message:
        try:
          emote_id = "emote-kiss"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "راب" in message:
        try:
          emote_id = "idle-dance-casual"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "لا" in message:
        try:
          emote_id = "emote-no"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print("error 3")

      if "تيليبورت" in message:
        try:
          emote_id = "emote-teleporting"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "قاتل" in message:
        try:
          emote_id = "emote-swordfight"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "You got a tip!" in message:
        try:
          emote_id = "dance-tiktok2"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "غني" in message:
        try:
          emote_id = "idle_singing"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "حارة" in message:
        try:
          emote_id = "emote-hot"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "تسس" in message:
        try:
          emote_id = "emote-snake"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "😂" in message:
        try:
          emote_id = "emote-laughing"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "يس" in message:
        try:
          emote_id = "emote-yes"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "ولكم" in message:
        try:
          emote_id = "emote-bow"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if "اوف" in message:
        try:
          emote_id = "emote-sad"
          await self.highrise.send_emote(emote_id, user.id)
        except:
          print(f"{emote_id}")

      if message.startswith("بوسة"):
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
           await self.highrise.send_emote("emote-kiss", roomUser.id)

      if message.startswith("زومبي"):
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-zombierun", roomUser.id)

      if message.startswith("ضفدع"):
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-frog", roomUser.id)


      if message.lstrip().startswith(("add","!tele","انقل")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
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
            'vip': Position(2.5, 19.0, 0.5, 'FrontRight'),
            'up': Position(x=16.5, y=8.350000381469727, z=29.5, facing='FrontRight'),
            'down' : Position(x=16.5, y=0.25, z=29.5, facing='FrontRight'),
          }
          dest = destinations.get(position_name.lower())
          if dest is None:
            return await self.highrise.send_whisper(user.id, f"The site is wrong ")
          user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
          if not user_id:
            await self.higrise.send_whisper(user.id, f"User {args[0][1:]} unavailable ")
            return

          await self.highrise.teleport(user_id, dest)
          await self.highrise.send_whisper(user.id, f"تم")
        else:
          await self.highrise.send_whisper(user.id, "You can't use this command")
      else:
          pass


      if message.startswith("تبرع"):
        try:
            tip_amount = int(message.split(" ")[1])
        except IndexError:
            await self.highrise.chat("يرجى تحديد الكمية المراد إرسالها.")
            return
        except ValueError:
            await self.highrise.chat("الرجاء إدخال رقم صحيح.")
            return
        if user.username in ["luciferEgypt","S_O_L_L_Y","_xA7m3d"]:
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


      #لو عايز يتبع حد
      if message.lower().startswith(("اتبع @","الحق @")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
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


      #لو عايز تطرد حد
      if message.startswith(('Kick','kick','!Kick','!kick')):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
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


      #لو عايز تبند حد
      if message.startswith(('Ban','ban','!Ban','!ban')):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
              parts = message.split()
              if len(parts) != 3:
                  await self.highrise.chat("Invalid Ban command format.")
                  return

              if "@" not in parts[1]:
                  username = parts[1]
              else:
                  username = parts[1][1:]

              user = await self.webapi.get_users(username = username, limit=1)
              if user:
                  user_id = user.users[0].user_id
              else:
                  await self.highrise.chat("User not found, please specify a valid user")
                  return

              action_length = parts[2]
              if action_length not in ["300","900","3600"]:
                  await self.highrise.chat("Please input a valid duration.")
                  return

              try:
                  await self.highrise.moderate_room(user_id, "ban", action_length)
              except Exception as e:
                  await self.highrise.chat(str(e))
                  return

              await self.highrise.chat(f"{username} has been banned from the room.")


      #لو عايز تشيل بان عن حد
      if message.startswith(('Unban','unban','!Unban','!unban')):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
            parts = message.split()
            if len(parts) != 2:
                await self.highrise.chat("Invalid Unban command format.")
                return

            if "@" not in parts[1]:
                username = parts[1]
            else:
                username = parts[1][1:]

            user = await self.webapi.get_users(username = username, limit=1)
            if user:
                user_id = user.users[0].user_id
            else:
                await self.highrise.chat("User not found, please specify a valid user")
                return

            try:
                await self.highrise.moderate_room(user_id, "unban")
            except Exception as e:
                await self.highrise.chat(str(e))
                return

            await self.highrise.chat(f"{username} has been unbanned from the room.")


      #لو عايز تعمل ميوت لحد
      if message.startswith(('Mute','mute','!Mute','!mute')):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","luciferEgypt","_xA7m3d"]):
              parts = message.split()
              if len(parts) != 3:
                  await self.highrise.chat("Invalid Mute command format.")
                  return

              if "@" not in parts[1]:
                  username = parts[1]
              else:
                  username = parts[1][1:]

              room_users = (await self.highrise.get_room_users()).content
              user_id = None
              for room_user, pos in room_users:
                  if room_user.username.lower() == username.lower():
                      user_id = room_user.id
                      break

              if user_id is None:
                  await self.highrise.chat("User not found, please specify a valid user.")
                  return

              action_length = parts[2]
              if action_length not in ["300", "900", "3600"]:
                  await self.highrise.chat("Please input a valid duration.")
                  return

              try:
                  await self.highrise.moderate_room(user_id, "mute", action_length)
              except Exception as e:
                  await self.highrise.chat(str(e))
                  return

              await self.highrise.chat(f"{username} has been muted for {action_length} from the room.")