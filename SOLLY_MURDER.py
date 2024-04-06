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

    async def on_start(self, session_metadata: SessionMetadata) -> None:
      print("SOLLY_MURDER")
      self.highrise.tg.create_task(self.highrise.teleport(
          session_metadata.user_id, Position(x=14.5, y=1.0, z=5.5, facing='FrontLeft')))


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
      await self.highrise.chat(f"رمضان كريم وكل سنه وانتم طيبين 💖 اهلا بيكم بمسابقة سولي الرمضانيه. المسابقه هي سؤال و أنت تحاول تجاوب صح بعد ما تتابع سولي.")
      await self.highrise.react("heart", user.id)

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


    async def on_whisper(self, user: User, message: str) -> None:

          #لو عايز تنقل الروم كله
          if message.startswith("in all"):
              roomUsers = (await self.highrise.get_room_users()).content
              for roomUser, _ in roomUsers:
                await self.highrise.teleport(f"{roomUser.id}", Position(x=10.5, y=0.0, z=5.5, facing='FrontRight'))

          if message.startswith("out all"):
              roomUsers = (await self.highrise.get_room_users()).content
              for roomUser, _ in roomUsers:
                await self.highrise.teleport(f"{roomUser.id}", Position(x=8.5, y=7.25, z=1.5, facing='FrontRight'))


    #لو عايز الهوست ينقل حد بيراكت
    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:

      user_privileges = await self.highrise.get_room_privilege(user.id)
      if (user_privileges.moderator and user.username not in ["SOLLY_MURDER"]) or (user.username in ["S_O_L_L_Y"]):
            if reaction == "heart":
              target_username = receiver.username
              await self.teleport_user_next_to(target_username, user)

      room_users = (await self.highrise.get_room_users()).content
      if user in [target_user for target_user, _ in room_users] and user.username not in ["SOLLY_MURDER"]:
          try:
              await self.highrise.react(reaction, user.id)
          except Exception as e:
              print(f"{self} could not send the reaction {reaction} back to {user}: {e}")


    #لو عايز ينقلك لما تدفع للبوت
    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
      if tip.amount > 99 and receiver.username in ["S_O_L_L_Y","SOLLY_MURDER"]:
          await self.highrise.teleport(sender.id, Position(x=12.5, y=8.25, z=14.5, facing='FrontLeft'))


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
      if any(keyword in message for keyword in ["المسابقة","المسابقه","مسابقه","مسابقة"]):
        await self.highrise.chat(f"رمضان كريم وكل سنه وانتم طيبين 💖 اهلا بيكم بمسابقة سولي الرمضانيه. المسابقه هي سؤال و أنت تحاول تجاوب صح بعد ما تتابع سولي.")

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

      #محفظة البوت
      if message in ["Wallet","wallet","!Wallet","!wallet"] and user.username in ["S_O_L_L_Y"]:
        wallet = (await self.highrise.get_wallet()).content
        await self.highrise.send_whisper(user.id,f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

      #كم واحد برومك
      if message in ["Players","players","!Players","!players"] and user.username in ["S_O_L_L_Y"]:
          room_users = (await self.highrise.get_room_users()).content
          await self.highrise.send_whisper(user.id,f"There are {len(room_users)} users in the room")

      if message.startswith("back") and user.username in ["S_O_L_L_Y"]:
        await self.highrise.walk_to(Position(x=14.5, y=1.0, z=5.5, facing='FrontLeft'))

      if message.startswith(("Get","get","!Get","!get")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
         target_username = message.split("@")[-1].strip()
         if target_username not in ["S_O_L_L_Y"]:
            await self.teleport_user_next_to(target_username, user)

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
          await self.highrise.chat("رقم من (1 to 68) 👉 عشان ترقص رقصه معينه.")
          await self.highrise.chat("All + رقم من (1 to 68) 👉 ترقص روم كلها نفس رقصتك .مثال: All 5 .")
          await self.highrise.chat("الرقصات 👉 يجبلك اسم الرقصات.")
        except Exception as e:
            print(f"Error: {e}")

      elif "الرقصات" in message:
        try:
            await self.highrise.chat(f"                              اكتب وزني, عمري, اوامر, رقصني, رقصنا, طيرنا, طيرني, نيمني, مشيني, مرجحني, مز, بطل, ايس كريم, مكرونا, جامد, شخلعني, وحش, مسطول, سقف, كيوت, فوق, مواه, ضحك, اوف, قلبي.")
            await self.highrise.chat(f"                              اكتب فخم, زومبي, اخفيني, بشتري, حرامي, اخشع, وجاهه, طرب, هز, عقباوي, في ايه, بتقول ايه, هييه, نططني, خود, مكسوف, هز يبط, هز يوز, مودل, عااا, مساج, دلعني, بتكسف, ماشي, عصبني, شوف دي, بطني.")
            await self.highrise.chat(f"                              اكتب عبيط, وسع, اجري, اتفضل, شكرا, اتفو, بموت, سحر, جنني, تمام, بخ, قعدني, مش شايف, عالمه, يفضحتي, مزنوق, اشطا, باي, سيو, عفريت.")
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

      elif message in ["Emotes","emotes","!Emotes","!emotes"]:
        try:
            await self.highrise.chat(f"Dance, Dance all, Fly,  Sleigh, Fashionista, Icecreamdance, Macarena, Superpose, Weirddance, Cute, Wave, Kiss, Laugh, Sweating, Cursing, Wrong, Tummyache, Gravity, Zombierun, Enthused.")
            await self.highrise.chat(f"Cutey, Teleporting, Letsgoshopping, Greedy, Punkguitar, Singing, Casualdance, Confusion, Raisetheroof, Animedance, Swordfight, Advancedshy, Dontstartnow, Model, Charging, Snake, Russiandance, Uwu, Flirtywave.")
            await self.highrise.chat(f"Savagedance, Kpopdance, Pennysdance, Bow, Curtsy, Snowballfight, Snowangel, Telekinesis, Maniac, Energyball, Frog, Sit, Hyped, Jinglebell, Nervous, Toilet, Astronaut, Timejump, Penguindance, Creepypuppet.")
            await self.highrise.chat(f"Kawaii, Repose, Flex, T4, T9, T10,  P1, P3,  P5, P7, P8.")
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
      #لو عايز الروم كلها ترقص نفس رقصتك
      if message.startswith(("Fly all","fly all","All fly","all fly","طيرنا","All 1","all 1","1 All","1 all")):
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
            await self.highrise.send_emote("emote-float", roomUser.id)
      #لو عايز انت بس ترقص
      if message in ["Fly","fly","!Fly","!fly","Float","float","!Float","!float","طيرني","طيرنى","1"]:
        try:
          await self.highrise.send_emote('emote-float', user.id)
        except Exception as e:
              print(f"Error: {e}")
      #باقي الرقصات
      if message.startswith(("Sleigh all","sleigh all","All sleigh","all sleigh","مشيني","All 2","all 2","2 All","2 all")):
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
              await self.highrise.send_emote("emote-sleigh", roomUser.id)

      if message in ["Sleigh","sleigh","!Sleigh","!sleigh","مشيني","2"]:
          try:
               await self.highrise.send_emote('emote-sleigh', user.id)
          except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Fashionista all","fashionista all","All fashionista","all fashionista","مز","All 3","all 3","3 All","3 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)

      if message in ["Fashionista","fashionista","!Fashionista","!fashionista","مز","3"]:
            try:
                await self.highrise.send_emote('emote-fashionista', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("P8 all","p8 all","All p8","all p8","بطل","All 4","all 4","4 All","4 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose8", roomUser.id)

      if message in ["Pose 8","pose 8","!Pose 8","!pose 8","P8","p8","بطل","4"]:
            try:
                await self.highrise.send_emote('emote-pose8', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Icecreamdance all","icecreamdance all","All icecreamdance","all icecreamdance","ايس كريم","All 5","all 5","5 All","5 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-icecream", roomUser.id)

      if message in ["Icecreamdance","icecreamdance","!Icecreamdance","!icecreamdance","ايس كريم","5"]:
            try:
                await self.highrise.send_emote('dance-icecream', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Macarena all","macarena all","All macarena","all macarena","مكرونا","All 6","all 6","6 All","6 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-macarena", roomUser.id)

      if message in ["Macarena","macarena","!Macarena","!macarena","مكرونا","6"]:
            try:
                await self.highrise.send_emote('dance-macarena', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("P7 all","p7 all","All p7","all p7","جامد","All 7","all 7","7 All","7 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose7", roomUser.id)

      if message in ["Pose 7","pose 7","!Pose 7","!pose 7","P7","p7","جامد","7"]:
            try:
                await self.highrise.send_emote('emote-pose7', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("T10 all","t10 all","All t10","all t10","شخلعني","All 8","all 8","8 All","8 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok10", roomUser.id)

      if message in ["Tiktokdance 10","tiktokdance 10","!Tiktokdance 10","!tiktokdance 10","T10","t10","شخلعني","8"]:
            try:
                await self.highrise.send_emote('dance-tiktok10', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Superpose all","superpose all","All superpose","all superpose","وحش","All 9","all 9","9 All","9 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-superpose", roomUser.id)

      if message in ["Superpose","superpose","!Superpose","!superpose","وحش","9"]:
            try:
                await self.highrise.send_emote('emote-superpose', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Weirddance all","weirddance all","All weirddance","all weirddance","مسطول","All 10","all 10","10 All","10 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)

      if message in ["Weirddance","weirddance","!Weirddance","!weirddance","مسطول","10"]:
            try:
                await self.highrise.send_emote('dance-weird', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("T9 all","t9 all","All t9","all t9","سقف","All 11","all 11","11 All","11 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)

      if message in ["Tiktokdance 9","tiktokdance 9","!Tiktokdance 9","!tiktokdance 9","T9","t9","سقف","11"]:
            try:
                await self.highrise.send_emote('dance-tiktok9', user.id)
            except Exception as e:
                print(f"Error: {e}") 

      if message.startswith(("Cute all","cute all","All cute","all cute","كيوت","All 12","all 12","12 All","12 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cute", roomUser.id)

      if message in ["Cute","cute","!Cute","!cute","كيوت","12"]:
            try:
                await self.highrise.send_emote('emote-cute', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Wave all","wave all","All wave","all wave","فوق","All 13","all 13","13 All","13 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-wave", roomUser.id)

      if message in ["Wave","wave","!Wave","!wave","فوق","3"]:
            try:
                await self.highrise.send_emote('emote-wave', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Kiss all","kiss all","All kiss","all kiss","مواه","All 14","all 14","14 All","14 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kiss", roomUser.id)

      if message in ["Kiss","kiss","!Kiss","!kiss","مواه","14"]:
            try:
                await self.highrise.send_emote('emote-kiss', user.id)
            except Exception as e:
                print(f"Error: {e}") 

      if message.startswith(("Laugh all","laugh all","All laugh","all laugh","ضحك","All 15","all 15","15 All","15 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-laughing", roomUser.id)

      if message in ["Laugh","laugh","!Laugh","!laugh","ضحك","15"]:
            try:
                await self.highrise.send_emote('emote-laughing', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Sweating all","sweating all","All sweating","all sweating","اوف","All 16","all 16","16 All","16 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)

      if message in ["Sweating","sweating","!Sweating","!sweating","اوف","16"]:
            try:
                await self.highrise.send_emote('emote-hot', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Cutey all","cutey all","All cutey","all cutey","قلبي","All 17","all 17","17 All","17 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutey", roomUser.id)

      if message in ["Cutey","cutey","!Cutey","!cutey","قلبي","17"]:
            try:
                await self.highrise.send_emote('emote-cutey', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("P5 all","p5 all","All p5","all p5","فخم","All 18","all 18","18 All","18 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose5", roomUser.id)

      if message in ["Pose 5","pose 5","!Pose 5","!pose 5","P5","p5","فخم","18"]:
            try:
                await self.highrise.send_emote('emote-pose5', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Teleporting all","teleporting all","All teleporting","all teleporting","اخفيني","All 19","all 19","19 All","19 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)

      if message in ["Teleporting","teleporting","!Teleporting","!teleporting","اخفيني","19"]:
            try:
                await self.highrise.send_emote('emote-teleporting', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Letsgoshopping all","letsgoshopping all","All letsgoshopping","all letsgoshopping","بشتري","All 20","all 20","20 All","20 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-shoppingcart", roomUser.id)

      if message in ["Letsgoshopping","letsgoshopping","!Letsgoshopping","!letsgoshopping","بشتري","20"]:
            try:
                await self.highrise.send_emote('dance-shoppingcart', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Greedy all","greedy all","All greedy","all greedy","حرامي","All 21","all 21","21 All","21 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-greedy", roomUser.id)

      if message in ["Greedy","greedy","!Greedy","!greedy","حرامي","21"]:
            try:
                await self.highrise.send_emote('emote-greedy', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("P3 all","p3 all","All p3","all p3","اخشع","All 22","all 22","22 All","22 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose3", roomUser.id)

      if message in ["Pose 3","pose 3","!Pose 3","!pose 3","P3","p3","اخشع","22"]:
            try:
                await self.highrise.send_emote('emote-pose3', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("P1 all","p1 all","All p1","all p1","وجاهه","All 23","all 23","23 All","23 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose1", roomUser.id)

      if message in ["Pose 1","pose 1","!Pose 1","!pose 1","P1","p1","وجاهه","23"]:
            try:
                await self.highrise.send_emote('emote-pose1', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Punkguitar all","punkguitar all","All punkguitar","all punkguitar","طرب","All 24","all 24","24 All","24 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id)

      if message in ["Punkguitar","punkguitar","!Punkguitar","!punkguitar","طرب","24"]:
            try:
                await self.highrise.send_emote('emote-punkguitar', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Singing all","singing all","All singing","all singing","هز","All 25","all 25","25 All","25 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)

      if message in ["Singing","singing","!Singing","!singing","هز","25"]:
            try:
                await self.highrise.send_emote('idle_singing', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Casualdance all","casualdance all","All casualdance","all casualdance","عقباوي","All 26","all 26","26 All","26 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)

      if message in ["Casualdance","casualdance","!Casualdance","!casualdance","عقباوي","26"]:
            try:
                await self.highrise.send_emote('idle-dance-casual', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Confusion all","confusion all","All confusion","all confusion","بتقول ايه","All 27","all 27","27 All","27 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-confused", roomUser.id)

      if message in ["Confusion","confusion","!Confusion","!confusion","بتقول ايه","27"]:
            try:
                await self.highrise.send_emote('emote-confused', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Raisetheroof all","raisetheroof all","All raisetheroof","all raisetheroof","هييه","All 28","all 28","28 All","28 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)

      if message in ["Raisetheroof","raisetheroof","!Raisetheroof","!raisetheroof","هييه","28"]:
            try:
                await self.highrise.send_emote('emoji-celebrate', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Animedance all","animedance all","All animedance","all animedance","نططني","All 29","all 29","29 All","29 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)

      if message in ["Animedance","animedance","!Animedance","!animedance","نططني","29"]:
            try:
                await self.highrise.send_emote('dance-anime', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Swordfight all","swordfight all","All swordfight","all swordfight","خود","All 30","all 30","30 All","30 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-swordfight", roomUser.id)

      if message in ["Swordfight","swordfight","!Swordfight","!swordfight","خود","30"]:
            try:
                await self.highrise.send_emote('emote-swordfight', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Advancedshy all","advancedshy all","All advancedshy","all advancedshy","مكسوف","All 31","all 31","31 All","31 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)

      if message in ["Advancedshy","advancedshy","!Advancedshy","!advancedshy","مكسوف","31"]:
            try:
                await self.highrise.send_emote('emote-shy2', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("T4 all","t4 all","All t4","all t4","هز يبط","All 32","all 32","32 All","32 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

      if message in ["Tiktokdance 4","tiktokdance 4","!Tiktokdance 4","!tiktokdance 4","T4","t4","هز يبط","32"]:
            try:
                await self.highrise.send_emote('idle-dance-tiktok4', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Dontstartnow all","dontstartnow all","All dontstartnow","all dontstartnow","هز يوز","All 33","all 33","33 All","33 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)

      if message in ["Dontstartnow","dontstartnow","!Dontstartnow","!dontstartnow","هز يوز","33"]:
            try:
                await self.highrise.send_emote('dance-tiktok2', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Model all","model all","All model","all model","مودل","All 34","all 34","34 All","34 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-model", roomUser.id)

      if message in ["Model","model","!Model","!model","مودل","34"]:
            try:
                await self.highrise.send_emote('emote-model', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Charging all","charging all","All charging","all charging","عا","All 35","all 35","35 All","35 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-charging", roomUser.id)

      if message in ["Charging","charging","!Charging","!charging","عا","35"]:
            try:
                await self.highrise.send_emote('emote-charging', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Snake all","snake all","All snake","all snake","مساج","All 36","all 36","36 All","36 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snake", roomUser.id)

      if message in ["Snake","snake","!Snake","!snake","مساج","36"]:
            try:
                await self.highrise.send_emote('emote-snake', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Russiandance all","russiandance all","All russiandance","all russiandance","دلعني","All 37","all 37","37 All","37 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-russian", roomUser.id)

      if message in ["Russiandance","russiandance","!Russiandance","!russiandance","دلعني","37"]:
            try:
                await self.highrise.send_emote('dance-russian', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Uwu all","uwu all","All uwu","all uwu","بتكسف","All 38","all 38","38 All","38 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)

      if message in ["Uwu","uwu","!Uwu","!uwu","بتكسف","38"]:
            try:
                await self.highrise.send_emote('idle-uwu', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Flirtywave all","flirtywave all","All flirtywave","all flirtywave","ماشي","All 39","all 39","39 All","39 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)

      if message in ["Flirtywave","flirtywave","!Flirtywave","!flirtywave","ماشي","39"]:
            try:
                await self.highrise.send_emote('emote-lust', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Cursing all","cursing all","All cursing","all cursing","عصبني","All 40","all 40","40 All","40 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-cursing", roomUser.id)

      if message in ["Cursing","cursing","!Cursing","!cursing","عصبني","40"]:
            try:
                await self.highrise.send_emote('emoji-cursing', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Wrong all","wrong all","All wrong","all wrong","شوف دي","All 41","all 41","41 All","41 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)

      if message in ["Wrong","wrong","!Wrong","!wrong","شوف دي","41"]:
            try:
                await self.highrise.send_emote('dance-wrong', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Tummyache all","tummyache all","All tummyache","all tummyache","بطني","All 42","all 42","42 All","42 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-gagging", roomUser.id)

      if message in ["Tummyache","tummyache","!Tummyache","!tummyache","بطني","42"]:
            try:
                await self.highrise.send_emote('emoji-gagging', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Savagedance all","savagedance all","All savagedance","all savagedance","عبيط","All 43","all 43","43 All","43 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok8", roomUser.id)

      if message in ["Savagedance","savagedance","!Savagedance","!savagedance","عبيط","43"]:
            try:
                await self.highrise.send_emote('dance-tiktok8', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Kpopdance all","kpopdance all","All kpopdance","all kpopdance","وسع","All 44","all 44","44 All","44 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-blackpink", roomUser.id)

      if message in ["Kpopdance","kpopdance","!Kpopdance","!kpopdance","وسع","44"]:
            try:
                await self.highrise.send_emote('dance-blackpink', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Pennysdance all","pennysdance all","All pennysdance","all pennysdance","اجري","All 45","all 45","45 All","45 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pennywise", roomUser.id)

      if message in ["Pennysdance","pennysdance","!Pennysdance","!pennysdance","اجري","45"]:
            try:
                await self.highrise.send_emote('dance-pennywise', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Bow all","bow all","All bow","all bow","اتفضل","All 46","all 46","46 All","46 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-bow", roomUser.id)

      if message in ["Bow","bow","!Bow","!bow","اتفضل","46"]:
            try:
                await self.highrise.send_emote('emote-bow', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Curtsy all","curtsy all","All curtsy","all curtsy","شكرا","All 47","all 47","47 All","47 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-curtsy", roomUser.id)

      if message in ["Curtsy","curtsy","!Curtsy","!curtsy","شكرا","47"]:
            try:
                await self.highrise.send_emote('emote-curtsy', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Snowballfight all","snowballfight all","All snowballfight","all snowballfight","اتفو","All 48","all 48","48 All","48 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowball", roomUser.id)

      if message in ["Snowballfight","snowballfight","!Snowballfight","!snowballfight","اتفو","48"]:
            try:
                await self.highrise.send_emote('emote-snowball', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Snowangel all","snowangel all","All snowangel","all snowangel","بموت","All 49","all 49","49 All","49 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowangel", roomUser.id)

      if message in ["Snowangel","snowangel","!Snowangel","!snowangel","بموت","49"]:
            try:
                await self.highrise.send_emote('emote-snowangel', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Telekinesis all","telekinesis all","All telekinesis","all telekinesis","سحر","All 50","all 50","50 All","50 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-telekinesis", roomUser.id)

      if message in ["Telekinesis","telekinesis","!Telekinesis","!telekinesis","سحر","50"]:
            try:
                await self.highrise.send_emote('emote-telekinesis', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Maniac all","maniac all","All maniac","all maniac","جنني","All 51","all 51","51 All","51 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-maniac", roomUser.id)

      if message in ["Maniac","maniac","!Maniac","!maniac","جنني","51"]:
            try:
                await self.highrise.send_emote('emote-maniac', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Energyball all","energyball all","All energyball","all energyball","تمام","All 52","all 52","52 All","52 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-energyball", roomUser.id)

      if message in ["Energyball","energyball","!Energyball","!energyball","تمام","52"]:
            try:
                await self.highrise.send_emote('emote-energyball', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Frog all","frog all","All frog","all frog","بخ","All 53","all 53","53 All","53 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-frog", roomUser.id)

      if message in ["Frog","frog","!Frog","!frog","53","بخ"]:
            try:
                await self.highrise.send_emote('emote-frog', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Sit all","sit all","All sit","all sit","قعدني","All 54","all 54","54 All","54 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-loop-sitfloor", roomUser.id)

      if message in ["Sit","sit","!Sit","!sit","قعدني","54"]:
            try:
                await self.highrise.send_emote('idle-loop-sitfloor', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Hyped all","hyped all","All hyped","all hyped","مش شايف","All 55","all 55","55 All","55 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)

      if message in ["Hyped","hyped","!Hyped","!hyped","مش شايف","55"]:
            try:
                await self.highrise.send_emote('emote-hyped', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Jinglebell all","jinglebell all","All jinglebell","all jinglebell","عالم","All 56","all 56","56 All","56 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)

      if message in ["Jinglebell","jinglebell","!Jinglebell","!jinglebell","عالم","56"]:
            try:
                await self.highrise.send_emote('dance-jinglebell', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Nervous all","nervous all","All nervous","all nervous","يفضحتي","All 57","all 57","57 All","57 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-nervous", roomUser.id)

      if message in ["Nervous","nervous","!Nervous","!nervous","يفضحتي","57"]:
            try:
                await self.highrise.send_emote('idle-nervous', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Toilet all","toilet all","All toilet","all toilet","مزنوق","All 58","all 58","58 All","58 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)

      if message in ["Toilet","toilet","!Toilet","!toilet","مزنوق","58"]:
            try:
                await self.highrise.send_emote('idle-toilet', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Astronaut all","astronaut all","All astronaut","all astronaut","اشطا","All 59","all 59","59 All","59 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)

      if message in ["Astronaut","astronaut","!Astronaut","!astronaut","اشطا","59"]:
            try:
                await self.highrise.send_emote('emote-astronaut', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Timejump all","timejump all","All timejump","all timejump","باي","All 60","all 60","60 All","60 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)

      if message in ["Timejump","timejump","!Timejump","!timejump","باي","60"]:
            try:
                await self.highrise.send_emote('emote-timejump', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Penguindance all","penguindance all","All penguindance","all penguindance","سيو","All 61","all 61","61 All","61 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)

      if message in ["Penguindance","penguindance","!Penguindance","!penguindance","سيو","61"]:
            try:
                await self.highrise.send_emote('dance-pinguin', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Creepypuppet all","creepypuppet all","All creepypuppet","all creepypuppet","عفريت","All 62","all 62","62 All","62 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-creepypuppet", roomUser.id)

      if message in ["Creepypuppet","creepypuppet","!Creepypuppet","!creepypuppet","عفريت","62"]:
            try:
                await self.highrise.send_emote('dance-creepypuppet', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Gravity all","gravity all","All gravity","all gravity","مرجحني","All 63","all 63","63 All","63 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gravity", roomUser.id)

      if message in ["Gravity","gravity","!Gravity","!gravity","63","مرجحني"]:
            try:
                await self.highrise.send_emote('emote-gravity', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith(("Zombierun all","zombierun all","All zombierun","all zombierun","زومبي","All 64","all 64","64 All","64 all")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)

      if message in ["Zombierun","zombierun","!Zombierun","!zombierun","زومبي","64"]:
            try:
                await self.highrise.send_emote('emote-zombierun', user.id)
            except Exception as e:
                print(f"Error: {e}")


      if message.startswith(("Enthused all","enthused all","All enthused","all enthused","في ايه","All 65","all 65","65 All","65 all","سولي","مستفز")):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)

      if message in ["Enthused","enthused","!Enthused","!enthused","في ايه","65","سولي","مستفز"]:
          try:
              await self.highrise.send_emote('idle-enthusiastic', user.id)
          except Exception as e:
              print(f"Error: {e}")

      if message.startswith(("Kawaii all","kawaii all","All kawaii","all kawaii","هاي","All 66","all 66","66 All","66 all")):
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
              await self.highrise.send_emote("dance-kawai", roomUser.id)

      if message in ["Kawaii","kawaii","!Kawaii","!kawaii","هاي","66"]:
           try:
               await self.highrise.send_emote('dance-kawai', user.id)
           except Exception as e:
               print(f"Error: {e}")

      if message.startswith(("Repose all","repose all","All repose","all repose","نيمني","All 67","all 67","67 All","67 all")):
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
              await self.highrise.send_emote("sit-relaxed", roomUser.id)

      if message in ["Repose","repose","!Repose","!repose","نيمني","67"]:
           try:
              await self.highrise.send_emote('sit-relaxed', user.id)
           except Exception as e:
              print(f"Error: {e}")

      if message.startswith(("Flex all","flex all","All flex","all flex","اه","All 68","all 68","68 All","68 all")):
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
              await self.highrise.send_emote("emoji-flex", roomUser.id)

      if message in ["Flex","flex","!Flex","!flex","اه","68"]:
           try:
               await self.highrise.send_emote('emoji-flex', user.id)
           except Exception as e:
              print(f"Error: {e}")


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
            'start' : Position(x=14.5, y=1.0, z=5.5, facing='FrontLeft'),
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


      #لو عايز تطرد حد
      if message.startswith(('Kick','kick','!Kick','!kick')):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
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
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
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
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
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
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
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