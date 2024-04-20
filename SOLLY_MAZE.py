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
      print("SOLLY_MAZE")
      self.highrise.tg.create_task(self.highrise.teleport(
          session_metadata.user_id, Position(19.5, 4, 13.5, "FrontLeft")))


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

      #يرجعك للباب
      await self.highrise.teleport(user.id, Position(19.5, 4,12.5, "FrontLeft"))

      await self.highrise.chat(f"اهلا بيك بمتاهات سولي ، للعب ادفع 10 جولد للبوت ، الفائز يأخذ 50 جولد ، بتمنالكم الفوز والاستمتاع ، حظ سعيد ي {user.username} 💓")
      await self.highrise.chat(f"لو فزت خود سكرين شوت وورهاني عشان تاخد الجايزة ✨📣")
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
                await self.highrise.teleport(f"{roomUser.id}", Position(19.5, 0,18, "FrontLeft"))

          if message.startswith("out all"):
              roomUsers = (await self.highrise.get_room_users()).content
              for roomUser, _ in roomUsers:
                await self.highrise.teleport(f"{roomUser.id}", Position(19.5, 4,12.5, "FrontLeft"))


    #لو عايز الهوست ينقل حد بيراكت
    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:

      if reaction =="heart"and user.username in ["S_O_L_L_Y","SOLLY_MAZE"]:
          target_username = receiver.username
          await self.teleport_user_next_to(target_username, user)

      user_privileges = await self.highrise.get_room_privilege(user.id)
      if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
              if reaction == "clap":
                await self.highrise.teleport(receiver.id, Position(x=18.5, y=0.0, z=1.5, facing='FrontLeft'))
              if reaction == "thumbs":
                await self.highrise.teleport(receiver.id, Position(x=15.5, y=0.0, z=18.5, facing='FrontLeft'))
              if reaction == "wave":
                await self.highrise.teleport(receiver.id, Position(19.5, 4,12.5, "FrontLeft"))
              if reaction == "wink":
                await self.highrise.teleport(receiver.id, Position(x=19.0, y=0.0, z=17.5, facing='FrontLeft'))

      room_users = (await self.highrise.get_room_users()).content
      if user in [target_user for target_user, _ in room_users] and user.username not in ["SOLLY_MAZE"]:
          try:
              await self.highrise.react(reaction, user.id)
          except Exception as e:
              print(f"{self} could not send the reaction {reaction} back to {user}: {e}")


    #لو عايز ينقلك لما تدفع للبوت
    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
      if tip.amount > 9 and receiver.username in ["S_O_L_L_Y","SOLLY_MAZE"]:
          await self.highrise.teleport(sender.id, Position(x=15.5, y=0.0, z=18.5, facing='FrontLeft'))


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
        await self.highrise.walk_to(Position(19.5, 4, 13.5, "FrontLeft"))

      if message in ["Host","host","!Host","!host","هوست"]:
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
          try:
            await self.highrise.teleport(f"{user.id}", Position(x=19.0, y=0.0, z=17.5, facing='FrontLeft'))
          except:
            print("error 3")

      if message in ["in","play","In","Play","لعبني"]:
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
          try:
            await self.highrise.teleport(f"{user.id}",Position(x=15.5, y=0.0, z=18.5, facing='FrontLeft'))
          except Exception as e:
            print(f"Error: {e}")

      if message.startswith(("Get","get","!Get","!get")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y"]):
         target_username = message.split("@")[-1].strip()
         if target_username not in ["S_O_L_L_Y"]:
            await self.teleport_user_next_to(target_username, user)

      if message in ["خرجني","door","Door","Out","out"]:
        try:
            await self.highrise.teleport(f"{user.id}", Position(19.5, 4,12.5, "FrontLeft"))
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
          await self.highrise.chat("رقصني 👉 تروح لمكان الرقص.")
          await self.highrise.chat("رقم من (1 to 68) 👉 عشان ترقص رقصه معينه.")
          await self.highrise.chat("All + رقم من (1 to 68) 👉 ترقص روم كلها نفس رقصتك .مثال: All 5 .")
          await self.highrise.chat("الرقصات 👉 يجبلك اسم الرقصات.")
          await self.highrise.chat("خرجني 👉 يخرجك.")
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
      #لو عايز انت بس ترقص
      if message in ["Fly","fly","!Fly","!fly","Float","float","!Float","!float","طيرني","طيرنى","1"]:
        try:
          await self.highrise.send_emote('emote-float', user.id)
        except Exception as e:
              print(f"Error: {e}")
      #باقي الرقصات

      if message in ["Sleigh","sleigh","!Sleigh","!sleigh","مشيني","2"]:
          try:
               await self.highrise.send_emote('emote-sleigh', user.id)
          except Exception as e:
                print(f"Error: {e}")


      if message in ["Fashionista","fashionista","!Fashionista","!fashionista","مز","3"]:
            try:
                await self.highrise.send_emote('emote-fashionista', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Pose 8","pose 8","!Pose 8","!pose 8","P8","p8","بطل","4"]:
            try:
                await self.highrise.send_emote('emote-pose8', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Icecreamdance","icecreamdance","!Icecreamdance","!icecreamdance","ايس كريم","5"]:
            try:
                await self.highrise.send_emote('dance-icecream', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Macarena","macarena","!Macarena","!macarena","مكرونا","6"]:
            try:
                await self.highrise.send_emote('dance-macarena', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Pose 7","pose 7","!Pose 7","!pose 7","P7","p7","جامد","7"]:
            try:
                await self.highrise.send_emote('emote-pose7', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Tiktokdance 10","tiktokdance 10","!Tiktokdance 10","!tiktokdance 10","T10","t10","شخلعني","8"]:
            try:
                await self.highrise.send_emote('dance-tiktok10', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Superpose","superpose","!Superpose","!superpose","وحش","9"]:
            try:
                await self.highrise.send_emote('emote-superpose', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Weirddance","weirddance","!Weirddance","!weirddance","مسطول","10"]:
            try:
                await self.highrise.send_emote('dance-weird', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Tiktokdance 9","tiktokdance 9","!Tiktokdance 9","!tiktokdance 9","T9","t9","سقف","11"]:
            try:
                await self.highrise.send_emote('dance-tiktok9', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Cute","cute","!Cute","!cute","كيوت","12"]:
            try:
                await self.highrise.send_emote('emote-cute', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Wave","wave","!Wave","!wave","فوق","3"]:
            try:
                await self.highrise.send_emote('emote-wave', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Kiss","kiss","!Kiss","!kiss","مواه","14"]:
            try:
                await self.highrise.send_emote('emote-kiss', user.id)
            except Exception as e:
                print(f"Error: {e}") 

      if message in ["Laugh","laugh","!Laugh","!laugh","ضحك","15"]:
            try:
                await self.highrise.send_emote('emote-laughing', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Sweating","sweating","!Sweating","!sweating","اوف","16"]:
            try:
                await self.highrise.send_emote('emote-hot', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Cutey","cutey","!Cutey","!cutey","قلبي","17"]:
            try:
                await self.highrise.send_emote('emote-cutey', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Pose 5","pose 5","!Pose 5","!pose 5","P5","p5","فخم","18"]:
            try:
                await self.highrise.send_emote('emote-pose5', user.id)
            except Exception as e:
                print(f"Error: {e}") 

      if message in ["Teleporting","teleporting","!Teleporting","!teleporting","اخفيني","19"]:
            try:
                await self.highrise.send_emote('emote-teleporting', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Letsgoshopping","letsgoshopping","!Letsgoshopping","!letsgoshopping","بشتري","20"]:
            try:
                await self.highrise.send_emote('dance-shoppingcart', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Greedy","greedy","!Greedy","!greedy","حرامي","21"]:
            try:
                await self.highrise.send_emote('emote-greedy', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Pose 3","pose 3","!Pose 3","!pose 3","P3","p3","اخشع","22"]:
            try:
                await self.highrise.send_emote('emote-pose3', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Pose 1","pose 1","!Pose 1","!pose 1","P1","p1","وجاهه","23"]:
            try:
                await self.highrise.send_emote('emote-pose1', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Punkguitar","punkguitar","!Punkguitar","!punkguitar","طرب","24"]:
            try:
                await self.highrise.send_emote('emote-punkguitar', user.id)
            except Exception as e:
                print(f"Error: {e}")

      

      if message in ["Singing","singing","!Singing","!singing","هز","25"]:
            try:
                await self.highrise.send_emote('idle_singing', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Casualdance","casualdance","!Casualdance","!casualdance","عقباوي","26"]:
            try:
                await self.highrise.send_emote('idle-dance-casual', user.id)
            except Exception as e:
                print(f"Error: {e}")

      

      if message in ["Confusion","confusion","!Confusion","!confusion","بتقول ايه","27"]:
            try:
                await self.highrise.send_emote('emote-confused', user.id)
            except Exception as e:
                print(f"Error: {e}")


      if message in ["Raisetheroof","raisetheroof","!Raisetheroof","!raisetheroof","هييه","28"]:
            try:
                await self.highrise.send_emote('emoji-celebrate', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Animedance","animedance","!Animedance","!animedance","نططني","29"]:
            try:
                await self.highrise.send_emote('dance-anime', user.id)
            except Exception as e:
                print(f"Error: {e}")


      if message in ["Swordfight","swordfight","!Swordfight","!swordfight","خود","30"]:
            try:
                await self.highrise.send_emote('emote-swordfight', user.id)
            except Exception as e:
                print(f"Error: {e}")

      

      if message in ["Advancedshy","advancedshy","!Advancedshy","!advancedshy","مكسوف","31"]:
            try:
                await self.highrise.send_emote('emote-shy2', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Tiktokdance 4","tiktokdance 4","!Tiktokdance 4","!tiktokdance 4","T4","t4","هز يبط","32"]:
            try:
                await self.highrise.send_emote('idle-dance-tiktok4', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Dontstartnow","dontstartnow","!Dontstartnow","!dontstartnow","هز يوز","33"]:
            try:
                await self.highrise.send_emote('dance-tiktok2', user.id)
            except Exception as e:
                print(f"Error: {e}")


      if message in ["Model","model","!Model","!model","مودل","34"]:
            try:
                await self.highrise.send_emote('emote-model', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Charging","charging","!Charging","!charging","عا","35"]:
            try:
                await self.highrise.send_emote('emote-charging', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Snake","snake","!Snake","!snake","مساج","36"]:
            try:
                await self.highrise.send_emote('emote-snake', user.id)
            except Exception as e:
                print(f"Error: {e}")


      if message in ["Russiandance","russiandance","!Russiandance","!russiandance","دلعني","37"]:
            try:
                await self.highrise.send_emote('dance-russian', user.id)
            except Exception as e:
                print(f"Error: {e}")


      if message in ["Uwu","uwu","!Uwu","!uwu","بتكسف","38"]:
            try:
                await self.highrise.send_emote('idle-uwu', user.id)
            except Exception as e:
                print(f"Error: {e}")


      if message in ["Flirtywave","flirtywave","!Flirtywave","!flirtywave","ماشي","39"]:
            try:
                await self.highrise.send_emote('emote-lust', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Cursing","cursing","!Cursing","!cursing","عصبني","40"]:
            try:
                await self.highrise.send_emote('emoji-cursing', user.id)
            except Exception as e:
                print(f"Error: {e}")


      if message in ["Wrong","wrong","!Wrong","!wrong","شوف دي","41"]:
            try:
                await self.highrise.send_emote('dance-wrong', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Tummyache","tummyache","!Tummyache","!tummyache","بطني","42"]:
            try:
                await self.highrise.send_emote('emoji-gagging', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Savagedance","savagedance","!Savagedance","!savagedance","عبيط","43"]:
            try:
                await self.highrise.send_emote('dance-tiktok8', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Kpopdance","kpopdance","!Kpopdance","!kpopdance","وسع","44"]:
            try:
                await self.highrise.send_emote('dance-blackpink', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Pennysdance","pennysdance","!Pennysdance","!pennysdance","اجري","45"]:
            try:
                await self.highrise.send_emote('dance-pennywise', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Bow","bow","!Bow","!bow","اتفضل","46"]:
            try:
                await self.highrise.send_emote('emote-bow', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Curtsy","curtsy","!Curtsy","!curtsy","شكرا","47"]:
            try:
                await self.highrise.send_emote('emote-curtsy', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Snowballfight","snowballfight","!Snowballfight","!snowballfight","اتفو","48"]:
            try:
                await self.highrise.send_emote('emote-snowball', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Snowangel","snowangel","!Snowangel","!snowangel","بموت","49"]:
            try:
                await self.highrise.send_emote('emote-snowangel', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Telekinesis","telekinesis","!Telekinesis","!telekinesis","سحر","50"]:
            try:
                await self.highrise.send_emote('emote-telekinesis', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Maniac","maniac","!Maniac","!maniac","جنني","51"]:
            try:
                await self.highrise.send_emote('emote-maniac', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Energyball","energyball","!Energyball","!energyball","تمام","52"]:
            try:
                await self.highrise.send_emote('emote-energyball', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Frog","frog","!Frog","!frog","53","بخ"]:
            try:
                await self.highrise.send_emote('emote-frog', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Sit","sit","!Sit","!sit","قعدني","54"]:
            try:
                await self.highrise.send_emote('idle-loop-sitfloor', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Hyped","hyped","!Hyped","!hyped","مش شايف","55"]:
            try:
                await self.highrise.send_emote('emote-hyped', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Jinglebell","jinglebell","!Jinglebell","!jinglebell","عالم","56"]:
            try:
                await self.highrise.send_emote('dance-jinglebell', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Nervous","nervous","!Nervous","!nervous","يفضحتي","57"]:
            try:
                await self.highrise.send_emote('idle-nervous', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Toilet","toilet","!Toilet","!toilet","مزنوق","58"]:
            try:
                await self.highrise.send_emote('idle-toilet', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Astronaut","astronaut","!Astronaut","!astronaut","اشطا","59"]:
            try:
                await self.highrise.send_emote('emote-astronaut', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Timejump","timejump","!Timejump","!timejump","باي","60"]:
            try:
                await self.highrise.send_emote('emote-timejump', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Penguindance","penguindance","!Penguindance","!penguindance","سيو","61"]:
            try:
                await self.highrise.send_emote('dance-pinguin', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Creepypuppet","creepypuppet","!Creepypuppet","!creepypuppet","عفريت","62"]:
            try:
                await self.highrise.send_emote('dance-creepypuppet', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Gravity","gravity","!Gravity","!gravity","63","مرجحني"]:
            try:
                await self.highrise.send_emote('emote-gravity', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Zombierun","zombierun","!Zombierun","!zombierun","زومبي","64"]:
            try:
                await self.highrise.send_emote('emote-zombierun', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message in ["Enthused","enthused","!Enthused","!enthused","في ايه","65","سولي","مستفز"]:
          try:
              await self.highrise.send_emote('idle-enthusiastic', user.id)
          except Exception as e:
              print(f"Error: {e}")

      if message in ["Kawaii","kawaii","!Kawaii","!kawaii","هاي","66"]:
           try:
               await self.highrise.send_emote('dance-kawai', user.id)
           except Exception as e:
               print(f"Error: {e}")

      if message in ["Repose","repose","!Repose","!repose","نيمني","67"]:
           try:
              await self.highrise.send_emote('sit-relaxed', user.id)
           except Exception as e:
              print(f"Error: {e}")

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
            'host': Position(x=19.0, y=0.0, z=17.5, facing='FrontLeft'),
            'in': Position(x=15.5, y=0.0, z=18.5, facing='FrontLeft'),
            'door': Position(19.5, 4,12.5, "FrontLeft"),
            'start' : Position(19.5, 4, 13.5, "FrontLeft"),
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