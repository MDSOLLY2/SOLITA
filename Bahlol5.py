from highrise import BaseBot, Position
from highrise.models import SessionMetadata, User
from highrise import __main__
from asyncio import run as arun
import random

class S_O_L_L_Y(BaseBot):
    dancs = ["idle-loop-sitfloor", "emote-tired", "emoji-thumbsup", "emoji-angry", "dance-macarena", "emote-hello", "dance-weird", "emote-superpose", "idle-lookup", "idle-hero", "emote-wings", "emote-laughing", "emote-kiss", "emote-wave", "emote-hearteyes", "emote-theatrical", "emote-teleporting", "emote-slap", "emote-ropepull", "emote-think", "emote-hot", "dance-shoppingcart", "emote-greedy", "emote-frustrated", "emote-float", "emote-baseball", "emote-yes", "idle_singing", "idle-floorsleeping", "idle-enthusiastic", "emote-confused", "emoji-celebrate", "emote-no", "emote-swordfight", "emote-shy", "dance-tiktok2", "emote-model", "emote-charging", "emote-snake", "dance-russian", "emote-sad", "emote-lust", "emoji-cursing", "emoji-flex", "emoji-gagging", "dance-tiktok8", "dance-blackpink", "dance-pennywise", "emote-bow", "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis", "emote-maniac", "emote-energyball", "emote-frog", "emote-cute", "dance-tiktok9", "dance-tiktok10", "emote-pose7", "emote-pose8", "idle-dance-casual", "emote-pose1", "emote-pose3", "emote-pose5", "emote-cutey","emote-Relaxing","emote-model","emote-cursty"]

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("hi im alive?")
        self.highrise.tg.create_task(self.highrise.teleport(
            session_metadata.user_id, Position(16, 0,1, "FrontLeft")))

    async def on_whisper(self, user: User, message: str) -> None:
        """On a received room whisper."""
        if message.startswith('welcome') and user.username == "_alone_komal__":
            try:
                xxx = message[2:]
                await self.highrise.chat(xxx)
                await self.highrise.send_emote('dance-breakdance')
            except:
                print("error 3")
            pass

    async def on_chat(self, user: User, message: str) -> None:
        """On a received room-wide chat."""

        if "رقصني" in message:
            try:
                emote_id = random.choice(self.dancs)
                await self.highrise.send_emote(emote_id, user.id)
            except:
                print(f"{emote_id}")

    async def on_channel(self, sender_id: str, message: str, tags: set[str]) -> None:
        """yy"""
        pass

    async def on_user_move(self, user: User, pos: Position) -> None:
        """n"""
        if user.username == "اسم الشخص":
            await self.highrise.send_emote('idle-hero')
            print(pos)

            facing = pos.facing
            print(type(pos))
            x = pos.x
            y = pos.y
            z = pos.z
            facing = pos.facing
            await self.highrise.walk_to(Position(x - 1, y, z - 1, facing))
            print(user.username, pos)
        pass

    async def is_admin(self, user: User):
        if user.id == self.BOT_ADMINISTRATOR_ID and user.username == self.BOT_ADMINISTRATOR:
            return True
        if user.id == 'xx' and user.username == 'zz':
            return True
        return False