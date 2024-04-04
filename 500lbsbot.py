from highrise import BaseBot, Position, GetMessagesRequest
from highrise.models import SessionMetadata, User, Reaction
from highrise import __main__
import random

class LatinStar(BaseBot):
    dances = [ "emote-superpose", "emote-laughing", "emote-kiss", "emote-wave", "emote-teleporting", "emote-hot ", "emote-greedy", "emote-float", "emote-confused", "emote-swordfight", "emote-model", "emote-charging", "emote-snake", "emote-lust", "emote-bow", "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis", "emote-maniac", "emote-energyball", "emote-frog", "emote-cute","emote-pose7 ", "emote-pose8", "emote-pose1", "emote-pose3", "emote-timejump", "emote-sleigh", "emote-punkguitar", "emote-zombierun", "emote-fashionista", "emote-gravity", "emote-shy2",

            "emoji-celebrate", "emoji-cursing", "emoji-gagging","emoji-flex",

              "sit-relaxed",

            "dance-macarena", "dance-weird", "dance-shoppingcart", "dance-tiktok2", "dance-russian", "dance-tiktok8", "dance-blackpink", "dance-pennywise","dance-tiktok9", "dance-tiktok10", "dance-jinglebell", "dance-pinguin", "dance-creepypuppet", "dance-icecream", "dance-wrong", "dance-anime","dance-kawai",

            "idle_singing", "idle-enthusiastic", "idle-dance-casual", "idle-loop-sitfloor", "idle-nervous", "idle-toilet", "idle-uwu", "idle-dance-tiktok4 ",
  ]

    message_count = {}

    def check_level(self, user_id):
        level = self.message_count.get(user_id, 0) // 10
        return level

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("500lbsbot")

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

    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"welcome to nss party! enjoy the vibes and the music we are providing for you guys! Also remember to buy our shirts bitten by fear to support nss!")

        try:
            emote_id = random.choice(self.dances)
            await self.highrise.send_emote(emote_id)
        except Exception as e:
            print(f"Error: {e}")

        try:
           emote_id = random.choice(self.dances)
           await self.highrise.send_emote(emote_id, user.id)
        except Exception as e:
           print(f"Error: {e}")


    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
      user_privileges = await self.highrise.get_room_privilege(user.id)
      if (user_privileges.moderator and user.username not in ["500lbsbot"]) or (user.username in ["S_O_L_L_Y","500lbs","LatinStar","louiiz"]):
        if reaction == "clap":
          await self.highrise.teleport(receiver.id, Position(x=14.5, y=4.75, z=6.5, facing='FrontRight'))
        if reaction == "thumbs":
          await self.highrise.teleport(receiver.id, Position(x=1.5, y=9.25, z=2.5, facing='FrontRight'))
        if reaction == "wave":
          await self.highrise.teleport(receiver.id, Position(x=11.5, y=0.5, z=7.5, facing='FrontRight'))
        if reaction == "heart":
          target_username = receiver.username
          await self.teleport_user_next_to(target_username, user)

      room_users = (await self.highrise.get_room_users()).content
      if user in [target_user for target_user, _ in room_users]:
          try:
              await self.highrise.react(reaction, user.id)
          except Exception as e:
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

      #محفظة البوت
      if message in ["Wallet","wallet","!Wallet","!wallet"] and user.username in ["S_O_L_L_Y","500lbs","LatinStar","louiiz"]:
        wallet = (await self.highrise.get_wallet()).content
        await self.highrise.send_whisper(user.id,f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")
        
      if message.startswith("back") and user.username in ["S_O_L_L_Y","500lbs","LatinStar","louiiz"]:
        await self.highrise.walk_to(Position(x=8.0, y=1.0, z=7.0, facing='FrontRight'))

      if message in ["Vip","vip","!Vip","!vip","Vip 1","vip 1","!Vip 1","!vip 1"]:
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","500lbs","LatinStar","louiiz"]):
          try:
            await self.highrise.teleport(f"{user.id}", Position(x=5.5, y=3.75, z=3.5, facing='FrontRight'))
          except:
            print("error 3")

      if message in ["dj","Dj","!Dj","!dj"]:
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","500lbs","LatinStar","louiiz"]):
          try:
            await self.highrise.teleport(f"{user.id}", Position(x=14.5, y=4.75, z=6.5, facing='FrontRight'))
          except:
            print("error 3")

      if message.startswith(("!get","get","Get","!Get")):
        user_privileges = await self.highrise.get_room_privilege(user.id)
        if (user_privileges.moderator) or (user.username in ["S_O_L_L_Y","500lbs","LatinStar","louiiz"]):
          target_username = message.split("@")[-1].strip()
          if target_username not in ["S_O_L_L_Y"]:
            await self.teleport_user_next_to(target_username, user)

      if message in ["Down","down","!Down","!down"]:
        try:
            await self.highrise.teleport(f"{user.id}", Position(x=11.5, y=0.5, z=7.5, facing='FrontRight'))
        except:
          print("error 3")
