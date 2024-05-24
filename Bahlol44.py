import random
from asyncio import run as arun

import requests
from highrise import (
    BaseBot,
    __main__,
)
from highrise.models import (
    Item,
    Position,
    Reaction,
    SessionMetadata,
    User,
)

class S_O_L_L_Y(BaseBot):

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        try:
            await self.highrise.walk_to(Position(16, 0,1 , "FrontRight"))
            await self.highrise.chat("انا جيت !")
        except Exception as e:
            print(f"error : {e}")
    async def on_whisper(self, user: User, message: str) -> None:
        """On a received room whisper."""
        if message.startswith('Hibot') and user.username == "youssef1230":
            try:
                await self.highrise.chat(" hi Plastic do u mind if i don't leave u space ha ha 😋? ")
                await self.highrise.send_emote('dance-breakdance')
            except:
                print("error 3")

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        text_to_emoji = {
        "wink": "😉",
        "wave": "👋",
        "thumbs": "👍",
        "heart": "❤️",
        "clap": "👏",
        }
        await self.highrise.chat(f"\n{user.username} {text_to_emoji[reaction]} {receiver.username}")

    async def on_user_join(self, user: User, position: Position) -> None:
        try:
            print(f"{user.username} Joined Room.")
            wm = [
            'نورتنا خش برجلك اليمين',
            'اخويا الطرش الي مبيهزرش!🥃 ',
            'عينك دي ولا لينسيز',
            'المطروش وصل🥃 ',
            'ادخل ادخل مفيش تفاهم.',
            ]

            rwm =random.choice(wm)
            rwm =random.choice(wm)
            await self.highrise.chat(f"الاوامر - طلعني - نزلني - فوق - تحت - وسط - نص ")

            await self.highrise.send_emote("breakdance", user.id)
            await self.highrise.send_emote('emote-bow')
            face = ["FrontRight","FrontLeft"]
            random.choice(face)
        except Exception as e:
            print(f"error : {e}")


    async def on_user_leave(self, user: User) -> None:
        try:
            wm = [
            'راجل جدع فرقنا👋',
            '👋💕مستنيك تيجي تاني',
            'هتوحشني 👋💕 ',
            ]
            rwm =random.choice(wm)
            await self.highrise.chat(f"{user.username} , {rwm}")
            await self.highrise.send_emote('wave')
            face = ["Frontright","FrontLeft"]
            random.choice(face)
        except Exception as e:
            print(f"error : {e}")



    async def on_chat(self, user: User, message: str):
        try:
            _bid = "435d9a847bc125ee52a9292cca6a7315565ae34c023f9241b35cfcc395967af6" #Bot user.id here
            _id = f"1_on_1:{_bid}:{user.id}"
            _idx = f"1_on_1:{user.id}:{_bid}"
            _rid = "661a23c6249b86137bd771b4" #Room ID Here
            if message.lower().lstrip().startswith(("!invite", "-invite")):
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, "\nUsage: !invite <@username> or -invite <@username> This command will send a room invitation on behalf of the targeted user. whether they have interacted with our bot in the past\n • Example: !invite <@Y_o_u_ss_e_f>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@Y_o_u_ss_e_f'.")
                    return

                url = f"https://webapi.highrise.game/users?&username={args[0][1:]}&sort_order=asc&limit=1"
                response = requests.get(url)
                data = response.json()
                users = data['youssef1230']

                for user in users:
                    user_id = user['user_id']
                    __id = f"1_on_1:{_bid}:{user_id}"
                    __idx = f"1_on_1:{user_id}:{_bid}"
                    __rid = "661a23c6249b86137bd771b4" #Room ID Here
                    try:
                        await self.highrise.send_message(__id, "Join Room", "invite", __rid)
                    except:
                        await self.highrise.send_message(__idx, "Join Room", "invite", __rid)

            if message.lower().lstrip().startswith(("-list", "!list")):
                await self.highrise.chat("\\commands you can use:\n • !teleport or -teleport\n • !emote or -emote\n ")
            if message.lower().lstrip().startswith(("-teleport", "عاوز اتنقل بين الادوار")):
               await self.highrise.chat("\\ Quik to teleport :\n •فوق او طلعني \n •تحت او نزلني \n •نص او وسط")


            if message.lower().lstrip().startswith(("-emote", "!emote")):
                await self.highrise.send_whisper(user.id, "\nEmote can only be used in our room by typing EMOTE NAME\n. Here's an example of the use of emotes \n casualdance\n fashionista\n  gravity\n floating\n, and all the other expressions of any expression saying only its name in its room")
            if message in ["تحت","نزلني"]:
                  try:
                    await self.highrise.teleport(f"{user.id}", Position(3, 0,2))
                  except:
                       print("error 3")    
            if message in ["فوق","طلعني"]:
                  try:
                    await self.highrise.teleport(f"{user.id}", Position(13, 17.5,2))
                  except:
                       print("error3") 
            if message in ["نص","وسط"]:
                  try:
                    await self.highrise.teleport(f"{user.id}", Position(16, 9,29))
                  except:
                       print("error3") 
            if message.startswith("اتشيك"):
              await self.highrise.set_outfit(outfit=[
        Item(type='clothing',
             amount=1,
             id='hair_front-n_malenew13',
             account_bound=False,
             active_palette=1),
        Item(type='clothing',
             amount=1,
             id='body-flesh',
             account_bound=False,
             active_palette=1),
        Item(type='clothing',
             amount=1,
             id='eye-n_basic2018malealmond',
             account_bound=False,
             active_palette=7),
        Item(type='clothing',
             amount=1,
             id='eyebrow-n_26',
             account_bound=False,
             active_palette=0),
        Item(type='clothing',
             amount=1,
             id='nose-n_01',
             account_bound=False,
             active_palette=0),
        Item(type='clothing',
             amount=1,
             id='mouth-basic2018thinround',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shirt-n_room12019sweaterwithbuttondowngrey',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='pants-n_room32019baggytrackpantsgreycamo',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shoes-n_room22019tallsocks',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='glasses-n_room12019circleframes',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shoes-n_whitedans',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='freckle-n_basic2018freckle22',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='hair_back-n_malenew13',
             account_bound=False,
             active_palette=-1),
      ])


            elif message.lower().strip() == "ولع":
                await self.highrise.send_emote("emote-superpose", user.id)
            elif message.lower().strip() == "صاصا":
                await self.highrise.send_emote("dance-tiktok10", user.id)
            elif message.lower().strip() == "جني":
                await self.highrise.send_emote("dance-weird", user.id)
            elif message.startswith("ميزو"):
                await self.highrise.send_emote("idle_singing", user.id)
            elif message.startswith("ضفدع"):
                await self.highrise.send_emote("emote-frog", user.id)
            elif message.startswith("هيرو"):
                await self.highrise.send_emote("dance-tiktok9", user.id)
            elif message.startswith("تسنيم"):
                await self.highrise.send_emote("emote-swordfight", user.id)
            elif message.startswith("0"):
                await self.highrise.send_emote("emote-energyball", user.id)
            elif message.startswith("كيوت"):
                await self.highrise.send_emote("emote-cute", user.id)
            elif message.startswith("floating"):
                await self.highrise.send_emote("emote-float", user.id)
            elif message.startswith("توماس"):
                await self.highrise.send_emote("emote-teleporting", user.id)
            elif message.lower().strip() == "telekinesis":
                await self.highrise.send_emote("emote-telekinesis", user.id)
            elif message.lower().strip() == "maniac":
                await self.highrise.send_emote("emote-maniac", user.id)
            elif message.lower().strip() == "embarrassed":
                await self.highrise.send_emote("emote-embarrassed", user.id)
            elif message.lower().strip() == "pissedoff":
                await self.highrise.send_emote("emote-frustrated", user.id)
            elif message.lower().strip() == "slap":
                await self.highrise.send_emote("emote-slap", user.id)
            elif message.startswith("بطوط"):
                await self.highrise.send_emote("dance-anime", user.id)
            elif message.lower().strip() == "enth":
                await self.highrise.send_emote("idle-enthusiastic", user.id)
            elif message.startswith("زوز"):
                await self.highrise.send_emote("emote-confused", user.id)
            elif message.lower().strip() == "shopping":
                await self.highrise.send_emote("dance-shoppingcart", user.id)
            elif message.lower().strip() == "roll":
                await self.highrise.send_emote("emote-roll", user.id)
            elif message.lower().strip() == "rofl":
                await self.highrise.send_emote("emote-rofl", user.id)
            elif message.lower().strip() == "superpunch":
                await self.highrise.send_emote("emote-superpunch", user.id)
            elif message.lower().strip() == "superrun":
                await self.highrise.send_emote("emote-superrun", user.id)
            elif message.lower().strip() == "superkick":
                await self.highrise.send_emote("emote-kicking", user.id)
            elif message.lower().strip() == "zombiedance":
                await self.highrise.send_emote("dance-zombie", user.id)
            elif message.lower().strip() == "monsterfail":
                await self.highrise.send_emote("emote-monster_fail", user.id)
            elif message.lower().strip() == "peekaboo":
                await self.highrise.send_emote("emote-peekaboo", user.id)
            elif message.lower().strip() == "sumofight":
                await self.highrise.send_emote("emote-sumo", user.id)
            elif message.lower().strip() == "charging":
                await self.highrise.send_emote("emote-charging", user.id)
            elif message.lower().strip() == "ninjarun":
                await self.highrise.send_emote("emote-ninjarun", user.id)
            elif message.lower().strip() == "proposing":
                await self.highrise.send_emote("emote-proposing", user.id)
            elif message.lower().strip() == "ropepull":
                await self.highrise.send_emote("emote-ropepull", user.id)
            elif message.lower().strip() == "secrethandshake":
                await self.highrise.send_emote("emote-secrethandshake", user.id)
            elif message.lower().strip() == "elbowbump":
                await self.highrise.send_emote("emote-elbowbump", user.id)
            elif message.lower().strip() == "homerun":
                await self.highrise.send_emote("emote-baseball", user.id)
            elif message.lower().strip() == "relaxing":
                await self.highrise.send_emote("idle-floorsleeping2", user.id)
            elif message.lower().strip() == "hug":
                await self.highrise.send_emote("emote-hug", user.id)
            elif message.lower().strip() == "cozynap":
                await self.highrise.send_emote("idle-floorsleeping", user.id)
            elif message.lower().strip() == "hugyourself":
                await self.highrise.send_emote("emote-hugyourself", user.id)
            elif message.lower().strip() == "snowballfight":
                await self.highrise.send_emote("emote-snowball", user.id)
            elif message.startswith("حر"):
                await self.highrise.send_emote("emote-hot", user.id)
            elif message.lower().strip() == "levelup":
                await self.highrise.send_emote("emote-levelup", user.id)
            elif message.lower().strip() == "snowangel":
                await self.highrise.send_emote("emote-snowangel", user.id)
            elif message.lower().strip() == "posh":
                await self.highrise.send_emote("idle-posh", user.id)
            elif message.lower().strip() == "fallingapart":
                await self.highrise.send_emote("emote-apart", user.id)
            elif message.lower().strip() == "poutyface":
                await self.highrise.send_emote("idle-sad", user.id)
            elif message.lower().strip() == "Irritated":
                await self.highrise.send_emote("idle-angry", user.id)
            elif message.lower().strip() == "heroentrance":
                await self.highrise.send_emote("emote-hero", user.id)
            elif message.lower().strip() == "heropose":
                await self.highrise.send_emote("idle-hero", user.id)
            elif message.startswith("جني"):
                await self.highrise.send_emote("emote-BashfulBlush", user.id)
            elif message.startswith("يوسف"):
                await self.highrise.send_emote("dance-russian", user.id)
            if message.startswith("تي"):
                await self.highrise.send_emote("emote-curtsy", user.id)
            if message.startswith("تو"):
                await self.highrise.send_emote("emote-curtsy", user.id)
            if message.startswith("توو"):
                await self.highrise.send_emote("emote-curtsy", user.id)
            if message.startswith("وب"):
                await self.highrise.send_emote("emote-bow", user.id)
            if message.startswith("ولكم"):
                await self.highrise.send_emote("emote-bow", user.id)
            elif message.lower().strip() == "headball":
                await self.highrise.send_emote("emote-headball", user.id)
            elif message.lower().strip() == "clumsy":
                await self.highrise.send_emote("emote-fail2", user.id)
            elif message.lower().strip() == "fall":
                await self.highrise.send_emote("emote-fail1", user.id)
            elif message.startswith("عبط"):
                await self.highrise.send_emote("dance-pennywise", user.id)
            elif message.startswith("هه"):
                await self.highrise.send_emote("emote-boo", user.id)
            elif message.lower().strip() == "fly":
                await self.highrise.send_emote("emote-wings", user.id)
            elif message.lower().strip() == "floss":
                await self.highrise.send_emote("dance-floss", user.id)
            elif message.startswith("نود"):
                await self.highrise.send_emote("dance-blackpink", user.id)
            elif message.startswith("ليلي"):
                await self.highrise.send_emote("emote-model", user.id)
            elif message.lower().strip() == "theatrical":
                await self.highrise.send_emote("emote-theatrical", user.id)
            elif message.lower().strip() == "amused":
                await self.highrise.send_emote("emote-laughing2", user.id)
            elif message.lower().strip() == "jetpack":
                await self.highrise.send_emote("emote-jetpack", user.id)
            elif message.startswith("عبط"):
                await self.highrise.send_emote("emote-bunnyhop", user.id)
            elif message.lower().strip() == "zombie":
                await self.highrise.send_emote("Idle_zombie", user.id)
            elif message.lower().strip() == "collapse":
                await self.highrise.send_emote("emote-death2", user.id)
            elif message.lower().strip() == "revival":
                await self.highrise.send_emote("emote-death", user.id)
            elif message.lower().strip() == "disco":
                await self.highrise.send_emote("emote-disco", user.id)
            elif message.lower().strip() == "relaxed":
                await self.highrise.send_emote("idle_relaxed", user.id)
            elif message.lower().strip() == "attentive":
                await self.highrise.send_emote("idle_layingdown", user.id)
            elif message.lower().strip() == "faint":
                await self.highrise.send_emote("emote-faint", user.id)
            elif message.lower().strip() == "cold":
                await self.highrise.send_emote("emote-cold", user.id)
            elif message.lower().strip() == "sleepy":
                await self.highrise.send_emote("idle-sleep", user.id)
            elif message.lower().strip() == "handstand":
                await self.highrise.send_emote("emote-handstand", user.id)
            elif message.startswith("جوست"):
                await self.highrise.send_emote("emote-ghost-idle", user.id)
            elif message.lower().strip() == "ghost":
                await self.highrise.send_emote("emoji-ghost", user.id)
            elif message.lower().strip() == "splitsdrop":
                await self.highrise.send_emote("emote-splitsdrop", user.id)
            elif message.lower().strip() == "yogaflow":
                await self.highrise.send_emote("dance-spiritual", user.id)
            elif message.lower().strip() == "smoothwalk":
                await self.highrise.send_emote("dance-smoothwalk", user.id)
            elif message.startswith("رينج"):
                await self.highrise.send_emote("dance-singleladies", user.id)
            elif message.lower().strip() == "sick":
                await self.highrise.send_emote("emoji-sick", user.id)
            elif message.startswith("هز"):
                await self.highrise.send_emote("dance-sexy", user.id)
            elif message.lower().strip() == "robotic":
                await self.highrise.send_emote("dance-robotic", user.id)
            elif message.lower().strip() == "naughty":
                await self.highrise.send_emote("emoji-naughty", user.id)
            elif message.lower().strip() == "pray":
                await self.highrise.send_emote("emoji-pray", user.id)
            elif message.lower().strip() == "duckwalk":
                await self.highrise.send_emote("dance-duckwalk", user.id)
            elif message.lower().strip() == "faintdrop":
                await self.highrise.send_emote("emote-deathdrop", user.id)
            elif message.lower().strip() == "voguehands":
                await self.highrise.send_emote("dance-voguehands", user.id)
            elif message.startswith("رقصني"):
                await self.highrise.send_emote("dance-orangejustice", user.id)
            elif message.startswith("جو"):
                await self.highrise.send_emote("dance-tiktok8", user.id)
            elif message.lower().strip() == "hearthands":
                await self.highrise.send_emote("emote-heartfingers", user.id)
            elif message.lower().strip() == "partnerheartarms":
                await self.highrise.send_emote("emote-heartshape", user.id)
            elif message.lower().strip() == "levitate":
                await self.highrise.send_emote("emoji-halo", user.id)
            elif message.lower().strip() == "sneeze":
                await self.highrise.send_emote("emoji-sneeze", user.id)
            elif message.startswith("جنش"):
                await self.highrise.send_emote("dance-tiktok2", user.id)
            elif message.lower().strip() == "rockout":
                await self.highrise.send_emote("dance-metal", user.id)
            elif message.lower().strip() == "pushups":
                await self.highrise.send_emote("dance-aerobics", user.id)
            elif message.lower().strip() == "karate":
                await self.highrise.send_emote("dance-martial-artist", user.id)
            elif message.lower().strip() == "macarena":
                await self.highrise.send_emote("dance-macarena", user.id)
            elif message.startswith("عع"):
                await self.highrise.send_emote("dance-handsup", user.id)
            elif message.lower().strip() == "breakdance":
                await self.highrise.send_emote("dance-breakdance", user.id)
            elif message.lower().strip() == "fireballlunge":
                await self.highrise.send_emote("emoji-hadoken", user.id)
            elif message.lower().strip() == "arrogance":
                await self.highrise.send_emote("emoji-arrogance", user.id)
            elif message.lower().strip() == "smirk":
                await self.highrise.send_emote("emoji-smirking", user.id)
            elif message.lower().strip() == "lying":
                await self.highrise.send_emote("emoji-lying", user.id)
            elif message.lower().strip() == "giveup":
                await self.highrise.send_emote("emoji-give-up", user.id)
            elif message.lower().strip() == "punch":
                await self.highrise.send_emote("emoji-punch", user.id)
            elif message.lower().strip() == "stinky":
                await self.highrise.send_emote("emoji-poop", user.id)
            elif message.lower().strip() == "point":
                await self.highrise.send_emote("emoji-there", user.id)
            elif message.startswith("بب"):
                await self.highrise.send_emote("emote-revelations", user.id)
            elif message.startswith("تت"):
                await self.highrise.send_emote("emote-Bashful", user.id)
            elif message.lower().strip() == "bummed":
                await self.highrise.send_emote("idle-loop-sad", user.id)
            elif message.lower().strip() == "chillin":
                await self.highrise.send_emote("idle-loop-happy", user.id)
            elif message.lower().strip() == "aerobics":
                await self.highrise.send_emote("idle-loop-aerobics", user.id)
            elif message.lower().strip() == "boogieswing":
                await self.highrise.send_emote("idle-dance-swinging", user.id)
            elif message.lower().strip() == "think":
                await self.highrise.send_emote("emote-think", user.id)
            elif message.startswith("عو"):
                await self.highrise.send_emote("emote-disappear", user.id)
            elif message.lower().strip() == "gasp":
                await self.highrise.send_emote("emoji-scared", user.id)
            elif message.lower().strip() == "eyeroll":
                await self.highrise.send_emote("emoji-eyeroll", user.id)
            elif message.lower().strip() == "sob":
                await self.highrise.send_emote("emoji-crying", user.id)
            elif message.lower().strip() == "frolic":
                await self.highrise.send_emote("emote-frollicking", user.id)
            elif message.lower().strip() == "graceful":
                await self.highrise.send_emote("emote-graceful", user.id)
            elif message.lower().strip() == "otur":
                await self.highrise.send_emote("sit-idle-cute", user.id)
            elif message.startswith("نصاب"):
                await self.highrise.send_emote("emote-greedy", user.id)
            elif message.lower().strip() == "flirtywave":
                await self.highrise.send_emote("emote-lust", user.id)
            elif message.lower().strip() == "tiredx":
                await self.highrise.send_emote("idle-loop-tired", user.id)
            elif message.startswith("بطني"):
                await self.highrise.send_emote("emoji-gagging", user.id)
            elif message.startswith("هع"):
                await self.highrise.send_emote("emoji-flex", user.id)
            elif message.lower().strip() == "raisetheroof":
                await self.highrise.send_emote("emoji-celebrate", user.id)
            elif message.startswith("متعصب"):
                await self.highrise.send_emote("emoji-cursing", user.id)
            elif message.lower().strip() == "stunned":
                await self.highrise.send_emote("emoji-dizzy", user.id)
            elif message.lower().strip() == "mindblown":
                await self.highrise.send_emote("emote-mindblown", user.id)
            elif message.lower().strip() == "shy":
                await self.highrise.send_emote("idle-loop-shy", user.id)
            elif message.lower().strip() == "sit":
                await self.highrise.send_emote("idle-loop-sitfloor", user.id)
            elif message.lower().strip() == "thumbsup":
                await self.highrise.send_emote("emote-thumbsup", user.id)
            elif message.lower().strip() == "clap":
                await self.highrise.send_emote("emote-clap", user.id)
            elif message.lower().strip() == "angry":
                await self.highrise.send_emote("emote-mad", user.id)
            elif message.lower().strip() == "tired":
                await self.highrise.send_emote("emote-sleepy", user.id)
            elif message.lower().strip() == "thewave":
                await self.highrise.send_emote("emote-thewave", user.id)
            elif message.lower().strip() == "thumbsuck":
                await self.highrise.send_emote("emote-suckthumb", user.id)
            elif message.lower().strip() == "shy":
                await self.highrise.send_emote("idle-loop-shy", user.id)
            elif message.lower().strip() == "panic":
                await self.highrise.send_emote("emote-panic", user.id)
            elif message.lower().strip() == "jump":
                await self.highrise.send_emote("emote-jumpb", user.id)
            elif message.lower().strip() == "dab":
                await self.highrise.send_emote("emote-dab", user.id)
            elif message.lower().strip() == "gangnamstyle":
                await self.highrise.send_emote("emote-gangnam", user.id)
            elif message.lower().strip() == "harlemshake":
                await self.highrise.send_emote("emote-harlemshake", user.id)
            elif message.lower().strip() == "tapdance":
                await self.highrise.send_emote("emote-tapdance", user.id)
            elif message.lower().strip() == "yes":
                await self.highrise.send_emote("creepypupprt", user.id)
            elif message.startswith("حزين"):
                await self.highrise.send_emote("emote-sad", user.id)
            elif message.lower().strip() == "robot":
                await self.highrise.send_emote("emote-robot", user.id)
            elif message.lower().strip() == "rainbow":
                await self.highrise.send_emote("emote-rainbow", user.id)
            elif message.startswith("خممنم"):
                await self.highrise.send_emote("emote-no", user.id)
            elif message.lower().strip() == "nightfever":
                await self.highrise.send_emote("emote-nightfever", user.id)
            elif message.startswith("لول"):
                await self.highrise.send_emote("emote-laughing", user.id)
            elif message.lower().strip() == "kiss":
                await self.highrise.send_emote("emote-kiss", user.id)
            elif message.lower().strip() == "judochop":
                await self.highrise.send_emote("emote-judochop", user.id)
            elif message.startswith("هاي"):
                await self.highrise.send_emote("emote-hello", user.id)
            elif message.startswith("فرحان"):
                await self.highrise.send_emote("emote-happy", user.id)
            elif message.lower().strip() == "moonwalk":
                await self.highrise.send_emote("emote-gordonshuffle", user.id)
            elif message.startswith("زومبي"):
                await self.highrise.send_emote("emote-zombierun", user.id)
            elif message.startswith("دماغي"):
                await self.highrise.send_emote("emote-pose8", user.id)
            elif message.startswith("كات"):
                await self.highrise.send_emote("emote-pose7", user.id)
            elif message.lower().strip() == "embracing":
                await self.highrise.send_emote("emote-pose7", user.id)
            elif message.lower().strip() == "fashionpose":
                await self.highrise.send_emote("emote-pose5", user.id)
            elif message.startswith("عفرتو"):
                await self.highrise.send_emote("emote-pose5", user.id)
            elif message.lower().strip() == "ichallengeyou":
                await self.highrise.send_emote("emote-pose3", user.id)
            elif message.lower().strip() == "challenge":
                await self.highrise.send_emote("emote-pose3", user.id)
            elif message.lower().strip() == "flirtywink":
                await self.highrise.send_emote("emote-pose1", user.id)
            elif message.startswith("غمزة"):
                await self.highrise.send_emote("emote-pose1", user.id)
            elif message.lower().strip() == "acasualdance":
                await self.highrise.send_emote("idle-dance-casual", user.id)
            elif message.lower().strip() == "casualdance":
                await self.highrise.send_emote("idle-dance-casual", user.id)
            elif message.startswith("شقط"):
                await self.highrise.send_emote("idle-dance-casual", user.id)
            elif message.startswith("كيوت"):
                await self.highrise.send_emote("emote-cutey", user.id)
            elif message.startswith("طيرني"):
                await self.highrise.send_emote("emote-astronaut", user.id)
            elif message.lower().strip() == "zerogravity":
                await self.highrise.send_emote("emote-astronaut", user.id)
            elif message.startswith("روز"):
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "tiktok4":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "tiktok4":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.startswith("هزني"):
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.startswith("حازم"):
                await self.highrise.send_emote("emote-punkguitar", user.id)
            elif message.lower().strip() == "punk":
                await self.highrise.send_emote("emote-punkguitar", user.id)
            elif message.lower().strip() == "guitar":
                 await self.highrise.send_emote("emote-punkguitar", user.id)
            elif message.startswith("ودي"):
                await self.highrise.send_emote("dance-icecream", user.id)
            elif message.startswith("ولع الروم"):
                await self.highrise.send_emote("emote-gravity", user.id)
            elif message.startswith("ميلي"):
                await self.highrise.send_emote("idle-uwu", user.id)
            elif message.lower().strip() == "uwumood":
                await self.highrise.send_emote("idle-uwu", user.id)
            elif message.startswith("فارس"):
                await self.highrise.send_emote("dance-wrong", user.id)
            elif message.startswith("محمد"):
                 await self.highrise.send_emote('idle-dance-tiktok4')

        except Exception as e:
            print(f"Error : {e}")


    async def on_user_move(self, user: User, pos: Position) -> None:
        """On a user moving in the room."""
        if user.username == "Alardo":
            await self.highrise.send_emote('idle-hero')
            print(pos)
            # التعامل مع حالة عدم وجود نص في pos
            facing = pos.facing
            print(type(pos))
            x = pos.x
            y = pos.y
            z = pos.z
            facing = pos.facing
            await self.highrise.walk_to(Position(x - 1, y, z - 1, facing))
            print(user.username, pos)
        pass