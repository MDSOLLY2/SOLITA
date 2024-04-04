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
  room_id_1 = "65a8fa17a90c302562850e1f"
  bot_token_1 = "44342a3172254cede02bd56fef6139fd1ae136736a187310bcb310de8fa12dcc"
  bot_file_1 = "2M0_0"
  bot_class_1 = "_2M0"

  room_id_2 = "65f6e827a10d3188198b6e2d"
  bot_token_2 = "a051d634b029aeff086df7bfd8e3b80ff44778390d4084335e6afa0d23d8d5f2"
  bot_file_2 = "500lbsbot"
  bot_class_2 = "LatinStar"

  room_id_3 = "65da4ad0b493c80d123a5a49"
  bot_token_3 = "e6c200d977d2c0d6acf349db72c443eefa369b23e4d9c5c1390c2ba23ae3f581"
  bot_file_3 = "dj_file.dj_bot"
  bot_class_3 = "S_O_L_L_Y"
  
  room_id_4 = "65f353c5e3a877ee994ff290"
  bot_token_4 = "827c88047b3013ac00908dfe0e7f7c2651aa09157a5988b544bcdec31c1b1b28"
  bot_file_4 = "Error_242"
  bot_class_4 = "S_O_L_L_Y"
  
  room_id_5 = "65da4ad0b493c80d123a5a49"
  bot_token_5 = "b5a7c1716ee3679e3d4bac2f5494cdeb0ac42fad5ddc6b83db914658c1f3c3d3"
  bot_file_5 = "SOLLY_PAG"
  bot_class_5 = "S_O_L_L_Y"

  room_id_6 = "651a8155f4097cf126f83ade"
  bot_token_6 = "b29f9d78ab9d8146e5cdf594817a7fc6418abee139d00d594b5d6f0214954ff1"
  bot_file_6 = "Y__N1_bot"
  bot_class_6 = "S_O_L_L_Y"

  room_id_7 = "6601d93c46461f7d016e463a"
  bot_token_7 = "1241317b3ddaa4547d5ebf251d53191a2934303402b6b19d05633b0770c1691f"
  bot_file_7 = "VOIDBDAY"
  bot_class_7 = "Felintosa"

  room_id_8 = "6608086dbe355d71f528d43d"
  bot_token_8 = "521ecdf41619739963c1d287d9894ff9ce9dfceecda22121c6b95f9c5b4d0757"
  bot_file_8 = "_TRUE_LOVE"
  bot_class_8 = "ROSIE_LO"


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
          self.room_id_8, self.bot_token_8)
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