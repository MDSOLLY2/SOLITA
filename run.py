from flask import Flask
from threading import Thread
from highrise.__main__ import *
import time

class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Alive"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()


class RunBot():
  room_id_1 = "64f8377f2afd3ea261a8843c"
  bot_token_1 = "99767eccc91cb0c9cd972625b565e0eaab718843d49a782a97eafb42181fb468"
  bot_file_1 = "SOLLY_6CORNERS"
  bot_class_1 = "S_O_L_L_Y"

  room_id_2 = "65da4ad0b493c80d123a5a49"
  bot_token_2 = "0e933adc954c6f3af955fdbcc07c4e9d483616476d04b277ac1576209119db5a"
  bot_file_2 = "SOLLY_15"
  bot_class_2 = "S_O_L_L_Y"

  room_id_3 = "64f31b23d6a5592093cd6232"
  bot_token_3 = "35a8265223577448afb23fc7feffba2c381c3ba159963daf43742f37ee17043b"
  bot_file_3 = "SOLLY_CHAIR"
  bot_class_3 = "S_O_L_L_Y"

  room_id_4 = "65944fe8dd633f3c4e767d9b"
  bot_token_4 = "b5680cc0049fa8e4fc9d775ce44b2c309f78132439803473c4155f0c4702f6cc"
  bot_file_4 = "SOLLY_MAZE_1"
  bot_class_4 = "S_O_L_L_Y"

  room_id_5 = "65950c96b132b36c701b00e5"
  bot_token_5 = "c65a8d69a22db0d801c2bac9d4105ccaed379bb74aa74a95c27bdf803b2ae200"
  bot_file_5 = "SOLLY_MAZE_2"
  bot_class_5 = "S_O_L_L_Y"

  room_id_6 = "65966a9d3a675b14db727297"
  bot_token_6 = "a1b85046d7b011d0333499c2339f48a665d8d99eb5a71bdf1aa05fe644d6945f"
  bot_file_6 = "SOLLY_MAZE_3"
  bot_class_6 = "S_O_L_L_Y"

  room_id_7 = "65b675049b664e06f0dbfb3b"
  bot_token_7 = "426ab94db6e06d23926fc15cef0b4587fb8208450ad495b570dcbdd8445c38ce"
  bot_file_7 = "SOLLY_MAZE_4"
  bot_class_7 = "S_O_L_L_Y"

  room_id_8 = "65c7a4e1bc15dde88f14f8bf"
  bot_token_8 = "436b330ed703a66043b74df9c66799664a39f2fd37328d950acdfeb7e4ab9b90"
  bot_file_8 = "SOLLY_MAZE_5"
  bot_class_8 = "S_O_L_L_Y"

  room_id_9 = "64f31af1a41886bd2b5e353f"
  bot_token_9 = "98219c34520530386b542133ad6a6345ef61bb44f440a13a31525a57a401e3df"
  bot_file_9 = "SOLLY_MAZE"
  bot_class_9 = "S_O_L_L_Y"

  room_id_10 = "65f82e18e3a877ee999ad831"
  bot_token_10 = "a01b247e3b361d82dca5f25eacebf7f7e877b6bd0496b3b07b2fc0a830d8ed6f"
  bot_file_10 = "SOLLY_MURDER"
  bot_class_10 = "S_O_L_L_Y"

  room_id_11 = "65da4ad0b493c80d123a5a49"
  bot_token_11 = "b5a7c1716ee3679e3d4bac2f5494cdeb0ac42fad5ddc6b83db914658c1f3c3d3"
  bot_file_11 = "SOLLY_PAG"
  bot_class_11 = "S_O_L_L_Y"

  room_id_12 = "64f4300f997a6c7df1974127"
  bot_token_12 = "09b5c08f4571c0194ab303c3548c1d06e4dcd012c84266c4792206ad894b8792"
  bot_file_12 = "SOLLY_PARTY"
  bot_class_12 = "S_O_L_L_Y"

  room_id_13 = "65da4ad0b493c80d123a5a49"
  bot_token_13 = "e6c200d977d2c0d6acf349db72c443eefa369b23e4d9c5c1390c2ba23ae3f581"
  bot_file_13 = "dj_file.dj_bot"
  bot_class_13 = "S_O_L_L_Y"


  def __init__(self) -> None:
    self.definitions = [
        BotDefinition(
            getattr(import_module(self.bot_file_1), self.bot_class_1)(),
            self.room_id_1, self.bot_token_1),
        BotDefinition(
            getattr(import_module(self.bot_file_2), self.bot_class_2)(),
            self.room_id_2, self.bot_token_2),
        BotDefinition(
            getattr(import_module(self.bot_file_3), self.bot_class_3)(),
            self.room_id_3, self.bot_token_3),
        BotDefinition(
            getattr(import_module(self.bot_file_4), self.bot_class_4)(),
            self.room_id_4, self.bot_token_4),
        BotDefinition(
            getattr(import_module(self.bot_file_5), self.bot_class_5)(),
            self.room_id_5, self.bot_token_5),
        BotDefinition(
            getattr(import_module(self.bot_file_6), self.bot_class_6)(),
            self.room_id_6, self.bot_token_6),
        BotDefinition(
            getattr(import_module(self.bot_file_7), self.bot_class_7)(),
            self.room_id_7, self.bot_token_7),
        BotDefinition(
            getattr(import_module(self.bot_file_8), self.bot_class_8)(),
            self.room_id_8, self.bot_token_8),
        BotDefinition(
            getattr(import_module(self.bot_file_9), self.bot_class_9)(),
            self.room_id_9, self.bot_token_9),
        BotDefinition(
            getattr(import_module(self.bot_file_10), self.bot_class_10)(),
            self.room_id_10, self.bot_token_10),
      BotDefinition(
          getattr(import_module(self.bot_file_11), self.bot_class_11)(),
          self.room_id_11, self.bot_token_11),
      BotDefinition(
          getattr(import_module(self.bot_file_12), self.bot_class_12)(),
          self.room_id_12, self.bot_token_12),
      BotDefinition(
          getattr(import_module(self.bot_file_13), self.bot_class_13)(),
          self.room_id_13, self.bot_token_13)
    ]  # More BotDefinition classes can be added to the definitions list

  def run_loop(self) -> None:
    while True:
      try:
        arun(main(self.definitions))

      except Exception as e:
        # Print the full traceback for the exception
        import traceback
        print("Caught an exception:")
        traceback.print_exc()  # This will print the full traceback
        time.sleep(1)
        continue

if __name__ == "__main__":
  WebServer().keep_alive()

  RunBot().run_loop()