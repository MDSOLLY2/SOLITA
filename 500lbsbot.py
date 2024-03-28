from highrise import BaseBot, Position
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
        self.highrise.tg.create_task(self.highrise.teleport(
            session_metadata.user_id, Position(x=13.5, y=0.0, z=1.5, facing='FrontRight')))

    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"Hello {user.username} ⭐🖤🔥 Welcome to NSS TIPS 🔥🖤⭐")

        try:
            emote_id = random.choice(self.dances)
            await self.highrise.send_emote(emote_id, user.id)
        except Exception as e:
            print(f"Error: {e}")


    async def on_user_leave(self, user: User) -> None:
      await self.highrise.chat(f"Bye {user.username} 💔")


    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
      if user.username in ["S_O_L_L_Y","LatinStar","500lbs","louiiz"]:
        if reaction == "clap":
          await self.highrise.teleport(receiver.id, Position(x=13.5, y=9.0, z=1.5, facing='FrontLeft'))
        if reaction == "thumbs":
          await self.highrise.teleport(receiver.id, Position(x=3.0, y=9.0, z=1.5, facing='FrontRight'))
        if reaction == "wave":
          await self.highrise.teleport(receiver.id, Position(x=13.0, y=0.0, z=6.0, facing='FrontRight'))
        if reaction == "wink":
          await self.highrise.teleport(receiver.id, Position(x=18.5, y=9.25, z=15.0, facing='FrontLeft'))


    async def on_chat(self, user: User, message: str) -> None:
      if  message == "!vip":
        if user.username in ["S_O_L_L_Y","LatinStar","500lbs","louiiz"]:
          try:
            await self.highrise.teleport(f"{user.id}", Position(x=15.5, y=4.5, z=12.5, facing='FrontLeft'))
          except:
            print("error 3")

      if  message == "!vip2":
        if user.username in ["S_O_L_L_Y","LatinStar","500lbs","louiiz"]:
          try:
            await self.highrise.teleport(f"{user.id}", Position(x=7.5, y=4.5, z=4.5, facing='FrontRight'))
          except:
            print("error 3")

      if  message == "!dj":
        if user.username in ["S_O_L_L_Y","LatinStar","500lbs","louiiz"]:
          try:
            await self.highrise.teleport(f"{user.id}", Position(x=13.5, y=9.0, z=1.5, facing='FrontLeft'))
          except:
            print("error 3")

      if  message == "!down":
        try:
            await self.highrise.teleport(f"{user.id}", Position(x=13.0, y=0.0, z=6.0, facing='FrontRight'))
        except:
          print("error 3")

      if message == "1":
        try:
            emote_id = random.choice(self.dances)
            await self.highrise.send_emote(emote_id, user.id)
        except Exception as e:
            print(f"Error: {e}")

      if message == "All 1":
          emote_id = random.choice(self.dances)
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
            await self.highrise.send_emote(emote_id, roomUser.id)

      if message == "All 2":
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
              await self.highrise.send_emote("emote-float", roomUser.id)

      if message == "2":
         try:
           await self.highrise.send_emote('emote-float', user.id)
         except Exception as e:
               print(f"Error: {e}")

      if message == "All 3":
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
              await self.highrise.send_emote("emote-sleigh", roomUser.id)

      if message == "3":
          try:
               await self.highrise.send_emote('emote-sleigh', user.id)
          except Exception as e:
                print(f"Error: {e}")

      if message == "All 4":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)

      if message == "4":
            try:
                await self.highrise.send_emote('emote-fashionista', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 5":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose8", roomUser.id)

      if message == "5":
            try:
                await self.highrise.send_emote('emote-pose8', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 6":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-icecream", roomUser.id)

      if message == "6":
            try:
                await self.highrise.send_emote('dance-icecream', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 7":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-macarena", roomUser.id)

      if message == "7":
            try:
                await self.highrise.send_emote('dance-macarena', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 8":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose7", roomUser.id)

      if message == "8":
            try:
                await self.highrise.send_emote('emote-pose7', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 9":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok10", roomUser.id)

      if message == "9":
            try:
                await self.highrise.send_emote('dance-tiktok10', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 10":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-superpose", roomUser.id)

      if message == "10":
            try:
                await self.highrise.send_emote('emote-superpose', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 11":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)

      if message == "11":
            try:
                await self.highrise.send_emote('dance-weird', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 12":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)

      if message == "12":
            try:
                await self.highrise.send_emote('dance-tiktok9', user.id)
            except Exception as e:
                print(f"Error: {e}") 

      if message == "All 13":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cute", roomUser.id)

      if message == "13":
            try:
                await self.highrise.send_emote('emote-cute', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 14":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-wave", roomUser.id)

      if message == "14":
            try:
                await self.highrise.send_emote('emote-wave', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 15":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kiss", roomUser.id)

      if message == "15":
            try:
                await self.highrise.send_emote('emote-kiss', user.id)
            except Exception as e:
                print(f"Error: {e}") 

      if message == "All 16":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-laughing", roomUser.id)

      if message == "16":
            try:
                await self.highrise.send_emote('emote-laughing', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 17":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)

      if message == "17":
            try:
                await self.highrise.send_emote('emote-hot', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 69":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutey", roomUser.id)

      if message == "69":
            try:
                await self.highrise.send_emote('emote-cutey', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 18":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose5", roomUser.id)

      if message == "18":
            try:
                await self.highrise.send_emote('emote-pose5', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 19":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)

      if message == "19":
            try:
                await self.highrise.send_emote('emote-teleporting', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 20":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-shoppingcart", roomUser.id)

      if message == "20":
            try:
                await self.highrise.send_emote('dance-shoppingcart', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 21":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-greedy", roomUser.id)

      if message == "21":
            try:
                await self.highrise.send_emote('emote-greedy', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 22":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose3", roomUser.id)

      if message == "22":
            try:
                await self.highrise.send_emote('emote-pose3', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 23":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose1", roomUser.id)

      if message == "23":
            try:
                await self.highrise.send_emote('emote-pose1', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 24":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id)

      if message == "24":
            try:
                await self.highrise.send_emote('emote-punkguitar', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 25":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)

      if message == "25":
            try:
                await self.highrise.send_emote('idle_singing', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 26":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)

      if message == "26":
            try:
                await self.highrise.send_emote('idle-dance-casual', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 27":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-confused", roomUser.id)

      if message == "27":
            try:
                await self.highrise.send_emote('emote-confused', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 28":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)

      if message == "28":
            try:
                await self.highrise.send_emote('emoji-celebrate', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 29":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)

      if message == "29":
            try:
                await self.highrise.send_emote('dance-anime', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 30":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-swordfight", roomUser.id)

      if message == "30":
            try:
                await self.highrise.send_emote('emote-swordfight', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 31":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)

      if message == "31":
            try:
                await self.highrise.send_emote('emote-shy2', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 32":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

      if message == "32":
            try:
                await self.highrise.send_emote('idle-dance-tiktok4', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 33":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)

      if message == "33":
            try:
                await self.highrise.send_emote('dance-tiktok2', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 34":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-model", roomUser.id)

      if message == "34":
            try:
                await self.highrise.send_emote('emote-model', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message.startswith("All 35"):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-charging", roomUser.id)

      if message == "35":
            try:
                await self.highrise.send_emote('emote-charging', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 36":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snake", roomUser.id)

      if message == "36":
            try:
                await self.highrise.send_emote('emote-snake', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 37":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-russian", roomUser.id)

      if message == "37":
            try:
                await self.highrise.send_emote('dance-russian', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 38":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)

      if message == "38":
            try:
                await self.highrise.send_emote('idle-uwu', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 39":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)

      if message == "39":
            try:
                await self.highrise.send_emote('emote-lust', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 40":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-cursing", roomUser.id)

      if message == "40":
            try:
                await self.highrise.send_emote('emoji-cursing', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 41":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)

      if message == "41":
            try:
                await self.highrise.send_emote('dance-wrong', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 42":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-gagging", roomUser.id)

      if message == "42":
            try:
                await self.highrise.send_emote('emoji-gagging', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 43":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok8", roomUser.id)

      if message == "43":
            try:
                await self.highrise.send_emote('dance-tiktok8', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 44":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-blackpink", roomUser.id)

      if message == "44":
            try:
                await self.highrise.send_emote('dance-blackpink', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 45":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pennywise", roomUser.id)

      if message == "45":
            try:
                await self.highrise.send_emote('dance-pennywise', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 46":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-bow", roomUser.id)

      if message == "46":
            try:
                await self.highrise.send_emote('emote-bow', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 47":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-curtsy", roomUser.id)

      if message == "47":
            try:
                await self.highrise.send_emote('emote-curtsy', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 48":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowball", roomUser.id)

      if message == "48":
            try:
                await self.highrise.send_emote('emote-snowball', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 49":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowangel", roomUser.id)

      if message == "49":
            try:
                await self.highrise.send_emote('emote-snowangel', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 50":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-telekinesis", roomUser.id)

      if message == "50":
            try:
                await self.highrise.send_emote('emote-telekinesis', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 51":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-maniac", roomUser.id)

      if message == "51":
            try:
                await self.highrise.send_emote('emote-maniac', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 52":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-energyball", roomUser.id)

      if message == "52":
            try:
                await self.highrise.send_emote('emote-energyball', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 53":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-frog", roomUser.id)

      if message == "53":
            try:
                await self.highrise.send_emote('emote-frog', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 54":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-loop-sitfloor", roomUser.id)

      if message == "54":
            try:
                await self.highrise.send_emote('idle-loop-sitfloor', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 55":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)

      if message == "55":
            try:
                await self.highrise.send_emote('emote-hyped', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 56":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)

      if message == "56":
            try:
                await self.highrise.send_emote('dance-jinglebell', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 57":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-nervous", roomUser.id)

      if message == "57":
            try:
                await self.highrise.send_emote('idle-nervous', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 58":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)

      if message == "58":
            try:
                await self.highrise.send_emote('idle-toilet', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 59":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)

      if message == "59":
            try:
                await self.highrise.send_emote('emote-astronaut', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 60":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)

      if message == "60":
            try:
                await self.highrise.send_emote('emote-timejump', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 61":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)

      if message == "61":
            try:
                await self.highrise.send_emote('dance-pinguin', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 62":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-creepypuppet", roomUser.id)

      if message == "62":
            try:
                await self.highrise.send_emote('dance-creepypuppet', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 63":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gravity", roomUser.id)

      if message == "63":
            try:
                await self.highrise.send_emote('emote-gravity', user.id)
            except Exception as e:
                print(f"Error: {e}")

      if message == "All 64":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)

      if message == "64":
            try:
                await self.highrise.send_emote('emote-zombierun', user.id)
            except Exception as e:
                print(f"Error: {e}")


      if message == "All 65":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)

      if message == "65":
          try:
              await self.highrise.send_emote('idle-enthusiastic', user.id)
          except Exception as e:
              print(f"Error: {e}")

      if message == "All 66":
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
              await self.highrise.send_emote("dance-kawai", roomUser.id)

      if message == "66":
           try:
               await self.highrise.send_emote('dance-kawai', user.id)
           except Exception as e:
               print(f"Error: {e}")

      if message == "All 67":
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
              await self.highrise.send_emote("sit-relaxed", roomUser.id)

      if message == "67":
           try:
              await self.highrise.send_emote('sit-relaxed', user.id)
           except Exception as e:
              print(f"Error: {e}")

      if message == "All 68":
          roomUsers = (await self.highrise.get_room_users()).content
          for roomUser, _ in roomUsers:
              await self.highrise.send_emote("emoji-flex", roomUser.id)

      if message == "68":
           try:
               await self.highrise.send_emote('emoji-flex', user.id)
           except Exception as e:
              print(f"Error: {e}")
