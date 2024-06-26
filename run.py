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

  room_id_10 = "65da4ad0b493c80d123a5a49"
  bot_token_10 = "b5a7c1716ee3679e3d4bac2f5494cdeb0ac42fad5ddc6b83db914658c1f3c3d3"
  bot_file_10 = "SOLLY_PAG"
  bot_class_10 = "S_O_L_L_Y"

  room_id_11 = "65da4ad0b493c80d123a5a49"
  bot_token_11 = "e6c200d977d2c0d6acf349db72c443eefa369b23e4d9c5c1390c2ba23ae3f581"
  bot_file_11 = "dj_file.dj_bot"
  bot_class_11 = "S_O_L_L_Y"

  room_id_12 = "64f31ba1e50a4b812315b976"
  bot_token_12 = "bcac41e76b388cb3b1c1b88a48a73cd709309c4a6be7b4557bb7956eda9b8ca4"
  bot_file_12 = "SOLLY_SQUIDGAME"
  bot_class_12 = "S_O_L_L_Y"

  room_id_13 = "64f31a2f5b0980d9b0b49f95"
  bot_token_13 = "66cbf839693dbbec682c866a4bd512d3675a1cf67741ef3877da0bcbc4904115"
  bot_file_13 = "SOLLY_GRABS"
  bot_class_13 = "S_O_L_L_Y"

  room_id_14 = "653f3ce81dd7c761f0c55b08"
  bot_token_14 = "f578ba564442a89d9d93cd6d3c54448929aa8ad076d7695ea7c3bc2d81db05bb"
  bot_file_14 = "bot_354A"
  bot_class_14 = "S_O_L_L_Y"

  room_id_15 = "661a23c6249b86137bd771b4"
  bot_token_15 = "435d9a847bc125ee52a9292cca6a7315565ae34c023f9241b35cfcc395967af6"
  bot_file_15 = "Bahlol44"
  bot_class_15 = "S_O_L_L_Y"

  room_id_16 = "661a23c6249b86137bd771b4"
  bot_token_16 = "d88d02f64640104393bf55be1595941b1c2e8998ff027ca9496a9d161bcf52cc"
  bot_file_16 = "Bahlol55"
  bot_class_16 = "S_O_L_L_Y"

  room_id_17 = "661a23c6249b86137bd771b4"
  bot_token_17 = "4e1830130a5de85ce67d2d64e209e0090756a6ef27f9049cb1d6fd37625d1338"
  bot_file_17 = "Bahlol00"
  bot_class_17 = "S_O_L_L_Y"

  room_id_18 = "661a23c6249b86137bd771b4"
  bot_token_18 = "494f031cabc4a188066bd1151c566a94fb86e4c4097b71a16aec7e0fba9a31a4"
  bot_file_18 = "Bahlol5"
  bot_class_18 = "S_O_L_L_Y"

  room_id_19 = "661a23c6249b86137bd771b4"
  bot_token_19 = "6d283ecd70959b183506b8b35a8e005dd8bf98ca0a399fc90b15c150d629c935"
  bot_file_19 = "Bahlol23"
  bot_class_19 = "S_O_L_L_Y"

  room_id_20 = "661a23c6249b86137bd771b4"
  bot_token_20 = "985df332c1681c3cdeceb81a01a3d3658423caa263780e7fa3bfab6eba61e613"
  bot_file_20 = "Bahlol4"
  bot_class_20 = "S_O_L_L_Y"

  room_id_21 = "661a23c6249b86137bd771b4"
  bot_token_21 = "4667ba7e23dacd673dfd7011315fbcb7898a815c03b010fd67103f27911ce542"
  bot_file_21 = "Bahlol22"
  bot_class_21 = "S_O_L_L_Y"

  room_id_22 = "661a23c6249b86137bd771b4"
  bot_token_22 = "50d67d29f483563b5d32fc9d110bba6d5a5578d5779921788e0a54f68c6d87d9"
  bot_file_22 = "Bahlol6"
  bot_class_22 = "S_O_L_L_Y"

  room_id_23 = "664fc6133846c1529586b370"
  bot_token_23 = "d321534b5685915e163732958a52e5d45dedf1261c0f03c93f8193f0e3e3e3e5"
  bot_file_23 = "Bahlol10"
  bot_class_23 = "S_O_L_L_Y"


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
          self.room_id_13, self.bot_token_13),
      BotDefinition(
          getattr(import_module(self.bot_file_14), self.bot_class_14)(),
          self.room_id_14, self.bot_token_14),
        BotDefinition(
            getattr(import_module(self.bot_file_15), self.bot_class_15)(),
            self.room_id_15, self.bot_token_15),
        BotDefinition(
            getattr(import_module(self.bot_file_16), self.bot_class_16)(),
            self.room_id_16, self.bot_token_16),
        BotDefinition(
            getattr(import_module(self.bot_file_17), self.bot_class_17)(),
            self.room_id_17, self.bot_token_17),
        BotDefinition(
            getattr(import_module(self.bot_file_18), self.bot_class_18)(),
            self.room_id_18, self.bot_token_18),
      BotDefinition(
          getattr(import_module(self.bot_file_19), self.bot_class_19)(),
          self.room_id_19, self.bot_token_19),
      BotDefinition(
          getattr(import_module(self.bot_file_20), self.bot_class_20)(),
          self.room_id_20, self.bot_token_20),
      BotDefinition(
          getattr(import_module(self.bot_file_21), self.bot_class_21)(),
          self.room_id_21, self.bot_token_21),
      BotDefinition(
          getattr(import_module(self.bot_file_22), self.bot_class_22)(),
          self.room_id_22, self.bot_token_22),
      BotDefinition(
          getattr(import_module(self.bot_file_23), self.bot_class_23)(),
          self.room_id_23, self.bot_token_23)
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