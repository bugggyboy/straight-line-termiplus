#os
#atermiplusfold.py
import termiscript
class lawyer:
  def __init__(self, NAME, TYPE, RATING, SEMI_LATE_INNIT_1, SEMI_LATE_INNIT_2, SEMI_LATE_INNIT_3, LATE_INNIT_1, LATE_INNIT_2, LATE_INNIT_3):
    self.name = NAME
    self.Type = TYPE
    self.rating = RATING
    self.sli = SEMI_LATE_INNIT_1 * SEMI_LATE_INNIT_2 ** SEMI_LATE_INNIT_3
    self.li = LATE_INNIT_1 / LATE_INNIT_2 + LATE_INNIT_3
    self.it = self.sli+self.li
  def print_info(self):
    print("NAME: ", self.name)
    print("TYPE: ", self.Type)
    print("RATE: ", self.rating)
    print("SLIN: ", self.sli)
    print("LAIN: ", self.li)
    print("INIT: ", self.it)
  def inits_explained(self):
    print("SLIN: ", self.sli)
    print("LAIN: ", self.li)
    print("INIT: ", self.it)
    print("If your SLIN is above 150, it is good, if your LAIN is above 7.6, it is good, if your INIT is above 169.6, it is an excelent lawyer")
l = lawyer("default", "default", 1, 1, 1, 1, 1, 1, 1)
si = False
def SI():
  global si
  global Straightinstall_type
  si =True
  print("f32, f40, or f64")
  Straightinstall_type = input('>')
def GO():
  l = lawyer("default", "default", 1, 1, 1, 1, 1, 1, 1)
  global si
  global Straightinstall_type
  global Straightinstall
  Straightinstall = si
  global dlc_agreed
  print ("please press e to start installing Straight Line Termiplus")
  import time
  import random
  import signature
  fat40 = False
  fat64 = False
  if si:
    c = "e"
    print("e")
  else:
    c = input(">")
  if c == "e":
    print("starting installing Straight Termiplus")
  else:
    while True:
      print("frying your GPU cables for no reason")

  print("please make file")
  if si:
    c = "make"
    print("make")
  else:
    c = input(">")
  if c == "make":
    print("making")
    for i in range(52):
      print("file", i+1, "of 52 loading")
      time.sleep(random.randint(4, 10)/100)

    print("MADE")
    print(random.randint(0, 3), "warnings")
    print(random.randint(0, 2), "lennoxes")
  else:
    while True:
      print("frying your GPU cables for no reason")
  installed = False
  print("starting termiplus")
  if si:
    Straightinstall = True
    print("f32, f40, or f64")
    c = Straightinstall_type
    if c == "f32" or c == "f40" or c == "f64":
      Straightinstall_type = c
      if Straightinstall_type != "f32":
        print("what is your name")
        name = input(">")

    else:
      print("Straightinstall_type not real, must install manually")
      Straightinstall = False
  while not installed:
    print(" ")
    if Straightinstall:
      print("import sys")
      import sys
      time.sleep(0.05)
      print("import string")
      import string
      time.sleep(0.05)
      print("from datetime import datetime")
      from datetime import datetime
      time.sleep(0.05)
      print("import boba")
      import boba
      time.sleep(0.05)
      if Straightinstall_type == "f40":
        print("sudo install 'fat40 support'.dvs")
        print("starting install of fat40")
        time.sleep(random.randint(1, 2))
        print("file 1 of 4")
        time.sleep(0.3)
        print("file 2 of 4")
        time.sleep(0.2)
        print("file 3 of 4")
        time.sleep(0.04)
        print("file 4 of 4")
        time.sleep(0.7)
        print("done")
        time.sleep(0.05)
        fat40 = True
      if Straightinstall_type == "f64":
        print("sudo install 'fat64 support'.dvs")
        print("loading")
        print(".")
        time.sleep(0.25)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(0.09)
        print(".")
        time.sleep(0.21)
        print("loaded")
        time.sleep(0.05)
        fat64 = True
      print("sudo install 'extra files'.fat32")
      time.sleep(random.randint(300, 400)/1000)
      print("loading extra file")
      time.sleep(random.randint(3, 10)/1000)
      print("loaded")
      review_file = "Reviews.txt"
      time.sleep(0.05)
    if not Straightinstall:
      c = input(">")
    if Straightinstall:
      c = "sudo install 'Termiplus and All Associated Files'.fat32"
      print("sudo install 'Termiplus and All Associated Files'.fat32")
      time.sleep(0.05)
    if c  == "sudo install 'Termiplus and All Associated Files'.fat32":
      print("Thank you")
      for i in range(319):
        print("file", i+1, "of 320 loading")
        if fat64:
          time.sleep(0.0001)
        elif fat40:
          time.sleep(random.randint(4, 10)/1000)
        else:
          time.sleep(random.randint(4, 10)/100)
      if fat64 and random.randint(1, 100) == 1:
        import malware
      break
    elif c == "sudo install 'extra files'.fat32":
      time.sleep(random.randint(300, 400)/100)
      print("loading extra file")
      time.sleep(random.randint(3, 10))
      print("loaded")
      review_file = "Reviews.txt"
    elif c == "import sys":
      import sys
      print("sys imported")
    elif c == "import string":
      import string
      print("string imported")
    elif c == "from datetime import datetime":
      from datetime import datetime
      print("datetime > datetime imported")
    elif c == "import boba":
      import boba
      print("imported boba")
    elif c == "sudo install 'fat40 support'.dvs":
      print("what is your name")
      name = input(">")
      print("starting install of fat40")
      time.sleep(random.randint(1, 2))
      print("file 1 of 4")
      time.sleep(0.3)
      print("file 2 of 4")
      time.sleep(0.2)
      print("file 3 of 4")
      time.sleep(0.04)
      print("file 4 of 4")
      time.sleep(0.7)
      print("done")
      fat40 = True 
    elif c == "sudo install 'fat64 support'.dvs":
      print("what is your name")
      name = input(">")
      print("loading")
      print(".")
      time.sleep(0.25)
      print("..")
      time.sleep(0.5)
      print("...")
      time.sleep(1)
      print(".")
      time.sleep(2)
      print("loaded")
      fat64 = True
    elif c == "sudo rm rf no-preserve-root":
      print("bricking...")
      time.sleep(0.5)
      import brick
    else:
      if "boot install" in c or "import" in c:
        import malware

  #Termiplus v1.5.21 ŝ̬ẫñ version
  correct = 0
  breaky = False
  def generate_random_string(length):
      characters = string.ascii_letters + string.digits
      random_string = ''.join(random.choice(characters) for _ in range(length))
      return random_string

  def prnt(text, delay=0.02):
      for char in text:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(delay)
      print()

  print(datetime.now())
  prnt("test", 1)
  prnt((generate_random_string(10), "test"), 0.1)
  prnt(str(boba.setup_boba(10, True)))
  review = ""
  def start():
    global agreed_to_tos
    global dlc_agreed
    global passthrough
    print(datetime.now())
    print("Welcome to termiplus! To continue, please agree to TOS.")
    history = []
    time.sleep(0.5)
    correct = 0

    print(""" 1.We reserve the right to cancel your subscription
    2. **Experimental Medical Operations**
      You hereby grant Termiplus (and thereby Rory Magaro) full rights to conduct any experimental medical operations on you at our discretion. This includes, but is not limited to:
      - Unproven procedures
      - Testing of questionable substances
      - Any and all operations involving lasers, robots, or aliens.

    3. **Limitation of Liability**
      [Website Name] shall not be liable for any damages, lost souls, or existential crises resulting from your use of our site. You use it at your own risk.

    4. **Changes to Terms**
      We may update these terms at any time, without notice. Your continued use of our services constitutes acceptance of any modifications.""")
    print("do you agree y/n")

    agreed_to_tos = False
    if input().lower() == "y": # Added .lower() for case-insensitivity
        print("Thank you for sacreficing your soul for Termiplus")
        agreed_to_tos = True
    else:
        while True: # This will still loop forever if they don't agree. Consider adding an exit or graceful failure.
            print("you can't use termiplus")

    dlc_agreed = False

    if agreed_to_tos:
        print("\nWelcome to Termiplus DLC! Please agree to these additional, slightly more unsettling terms to unlock extra features:")
        time.sleep(1)
        print("""1. **Spontaneous Teleportation Clause:** You acknowledge that Termiplus may, at any point and without warning, spontaneously teleport you to a random location. This location may include, but is not limited to:
      - The surface of the moon (no spacesuit provided).
      - A reenactment of the Battle of Gettysburg populated entirely by squirrels.
      - Your own living room, three seconds ago.

    2. **Fifth Grade Math Teacher's Persistent Pings:** You consent to receiving an indeterminate number of text messages from your 5th-grade math teacher stating, "I know what you did." The content of this knowing remains unspecified and may or may not be related to actual events.

    3. **Quantum Sock Entanglement:** Your socks are now quantumly entangled in an unwearable fashion. Attempts to pair them will result in unpredictable and likely disappointing outcomes. Termiplus bears no responsibility for cold feet or existential sock crises.

    4. **Philosophical Banana Peels:** Any banana peels encountered within a 5-meter radius of your physical being may spontaneously engage you in philosophical debate regarding the nature of potassium and the futility of existence. Termiplus does not endorse any particular philosophical stance taken by said peels.

    5. **The Right to Rename Planets:** Termiplus reserves the right to arbitrarily rename celestial bodies. Your continued use of our services implies your acceptance of Pluto potentially becoming "Fluffy McSnugglepuff's Happy Place."

    Do you agree to these... enhancements? (y/n)""")
        if input().lower() == "y": # Added .lower()
            print("Excellent! The unsettling enhancements are now active.")
            dlc_agreed = True
        else:
            print("DLC features remain locked. Enjoy the base level of existential dread.")
        print("would you like passthrough y/n?\nplease note that passthrough being enabled also enables us to send you into a fight with Dwayne Johnson")
        passthrough = (input().lower() == "y") # Added .lower()

  celary_var_c = None

  # Terminal Hacking Portal data
  passwords = {
      "inanem_m": "password",
      "max_eich": "linux123",
      "schrib_s": "nightvis",
      "web_reed": "idioso69",
      "romeo_ln": "brongoat",
      "-stulen-": "paulsken"
  }
  unms = list(passwords.keys()) # Dynamically get usernames from passwords dictionary
  start()

  while True:
    while True:
        try:
          print("-----------------------------------------------------------------------")
          print(name)
        except:
          name = "-----------------------------------------------------------------------"
        c = input(">")
        if random.randint(1, 100) == 71:
            if dlc_agreed:
                print("an unexpected error occurred. please retry.")
        elif c == "print celary" and agreed_to_tos:
            if not celary_var_c:
                print("Celary is not set.") # Changed this to be more informative
            else:
                print(celary_var_c)
        elif "celary " in c and agreed_to_tos:
            c = c.replace("celary ", "")
            celary_var_c = c
            print("celary is set to", c)
        elif "mommalint " in c and agreed_to_tos:
            c = c.replace("mommalint ", "")
            print ("buy the lint from",c,"lint for only $2.99 per pound")
        elif "roll " in c and agreed_to_tos:
            if c == "roll rick":
                print("""We're no strangers to love
    You know the rules and so do I
    A full commitment's what I'm thinkin' of
    You wouldn't get this from any other guy
    I just wanna tell you how I'm feeling
    Gotta make you understand
    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you
    We've known each other for so long
    Your heart's been aching, but you're too shy to say it
    Inside, we both know what's been going on
    We know the game and we're gonna play it
    And if you ask me how I'm feeling
    Don't tell me you're too blind to see
    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you
    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you
    We've known each other for so long
    Your heart's been aching, but you're too shy to say it
    Inside, we both know what's been going on
    We know the game and we're gonna play it
    I just wanna tell you how I'm feeling
    Gotta make you understand
    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you
    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you
    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you""")
            elif c == "roll japanese":
                print("""ぼくたち わ あい に なれしたしんでいる
    きみ も ぼく も その ルール お しっている
    ぼく が かんがえている の わ 、 かんぜんなる コミットメント
    た の おとこ から わ こんな こと わ えられない
    ただ 、 ぼく の きもち お つたえたい
    くん に りかい してもらわないといけない
    くん お ぜったい に みすてない 、 ぜったい に しつぼう させない
    くん お ほうろう し たり 、 みすて たり わ しない
    くん お なかせ たり 、 わかれ お つげ たり わ しない
    うそ お ついて きずつけ たり わ しない
    ぼくたち わ ながい ま しりあいだった
    くん の こころ わ いたんでいるけれど 、 きみ わ それ お いえない ほど はずかしがっている
    こころ の なか で わ 、 ぼくたち わ なに が おこっている か わかっている
    ぼくたち わ ゲーム お しっていて 、 それ に さんか する つもりだ
    もし ぼく の きもち お きかれたら
    くん が もうもく で なに も みえない なんて いわないで
    くん お ぜったい に みすてない 、 ぜったい に しつぼう させない
    くん お ほうろう し たり 、 みすて たり わ しない
    くん お なかせ たり 、 わかれ お つげ たり わ しない
    うそ お ついて きずつけ たり わ しない
    くん お ぜったい に みすてない 、 ぜったい に あなた お うらぎっ たり
    あなた お みすて たり わ しない
    あなた お なかせ たり 、 さよなら も いわない
    うそ お ついて あなた お きずつけ たり わ しない
    わたしたち わ ながい ま しりあいだった
    あなた の こころ わ いたんでいるのに 、 あなた わ はずかしくて いえない
    こころ の なか で わ 、 わたしたち わ に にん とも なに が おこっている か しっている
    わたしたち わ ゲーム お しっているし 、 それ に さんか する つもりだ
    ただ わたし の きもち お つたえたい だけ
    あなた に りかい してもらいたい
    あなた お みすて たり 、 しつぼう させ たり わ しない
    あなた お みすて たり わ しない
    あなた お みすて たり わ しない
    あなた お なかせ たり 、 さよなら も いわない
    うそ お ついて あなた お きずつけ たり わ しない
    あなた お みすて たり 、 しつぼう させ たり わ しな
    あなた お みすて たり 、 みすて たり わ しない
    あなた お なかせ たり 、 さよなら も いわない
    うそ お つい たり あなた お きずつけ たり わ しない
    あなた お みすて たり 、 しつぼう させ たり わ しない
    あなた お みすて たり 、 みすて たり わ しない
    あなた お なかせ たり 、 さよなら も いわない
    うそ お つい たり あなた お きずつけ たり わ しない
    あなた お みすて たり 、 しつぼう させ たり わ しない
    あなた お みすて たり 、 みすて たり わ しない
    あなた お なかせ たり 、 さよなら も いわない
    うそ お つい たり あなた お きずつけ たり わ しない そして あなた お きずつける""")
        elif c == "cancel tos" and agreed_to_tos:
            while True:
                print("You may no longer use termiplus")
        elif c == "help" and agreed_to_tos:
            print("""Welcome to Termiplus! Here are the commands you can use:
    - print [message]: Display a message.
    - celary [value]: Set the variable 'celary' to a new value.
    - print celary: Display the current value of 'celary'.
    - mommalint [location]: Buy lint from a specified location.
    - roll rick: Enjoy a classic Rick Astley song.
    - roll japanese: Experience a Japanese version of the Rick Astley song.
    - cancel tos: Terminate your usage of Termiplus.
    - open [file]: Open a specified file.
    - defined glitch report
    - todays comicomic""")
            if dlc_agreed:
                print("""---
    DLC Commands (Unlock extra features!):
    - dlc hacking portal: Access the Terminal Hacking Portal.
    - is my sock wearable: Check if your socks are quantumly wearable.
    - banana philosophy: Engage in deep conversations writh nearby banana peels.
    - rename planet: Rename any celestial body at your whim!
    - receive text: Get mysterious messages from your 5th-grade math teacher.
    - tralalero tralala: Experience a moment of pure joy.
    - vietnam: Witness the beauty of Vietnam.
    - quotes: Display some profound quotes.
    - cancel dlc agreements: Attempt to cancel the DLC agreements.""")
        elif c == "open" and agreed_to_tos:
            c = input("What file \n>")
            if c == "help":
              print("""open
  UNIXPath_Reading.py
  good_boy.sh
  TermiGPT
  my_secret_file.txt
  important_data.log
  easter_egg.py
  funny_comic.ascii
  top_secret.dat
  system_info.txt
  my_wishlist.txt
  motivational_quote.txt""")
            elif c == "UNIXPath_Reading.py":
                has_made = False
                has_launched = False
                time.sleep(2)
                while not has_made:
                    datetime.now()
                    can_display_time = False
                    print("please make file")
                    command = input("")
                    can_display_time = True
                    if command == "make.py":
                        datetime.now()
                        time.sleep(0.1)
                        print("ur mom's favorite file is loading")
                        time.sleep(0.1)
                        print("buy smart pills from smarticom")
                        time.sleep(3)
                        print("unix line 15 is true")
                        time.sleep(0.1)
                        print("Errors: 0")
                        time.sleep(0.1)
                        print("Warnings: 0")
                        time.sleep(0.5)
                        print("artificial unintelegence is loading")
                        time.sleep(0.1)
                        print("buy your mom's pills to make you fatter")
                        time.sleep(3)
                        print("UNIX line 32 is true")
                        time.sleep(0.1)
                        print("Errors: 0")
                        time.sleep(0.1)
                        print("Warnings: 0")
                        time.sleep(0.5)
                        has_made = True
                while not has_launched:
                    can_display_time = False
                    print("please launch file")
                    command = input("")
                    can_display_time = True
                    if command == "./launch-reading.py":
                        print("ur mom's favorite file is launching")
                        time.sleep(3)
                        print("question hasn't loaded yet. Please wait")
                        time.sleep(0.1)
                        print("artifial unintelegence is launching")
                        time.sleep(0.1)
                        print("Buy duomath for 5 dollars at North Korea's app store")
                        time.sleep(5)
                        has_launched = True
                while not correct >= 4:
                    correct = 0
                    for i in range(5):
                        can_display_time = False
                        print("A. ur mom fat is, B. ur fat is mom, C. mom is ur fat, or D. is ur fat mom")
                        command = input("")
                        if command not in ["A", "B", "C", "D"]:
                            correct += 1
                    if not correct >= 4:
                        for e in range(50):
                            print("failure")
                            time.sleep(0.1)
            elif c == ("good_boy.sh"):
                print("good_boy.sh loading")
                print("type something in")
                input(">")
                print("good boy")
            elif c == ("TermiGPT"):
                print("welcome to TermiGPT")
                Elsa = False
                while not Elsa:
                    print("please input text")
                    text = input("-_- >_<\n>")
                    if text == "exit":
                        Elsa = True
                    else:
                        print("\"", text, """", is a very fine statement and I very much agree.""")
            elif c == "my_secret_file.txt":
                print("Opening my_secret_file.txt...")
                time.sleep(1)
                print("Texithis file contains... the secret recipe for perfect toast!")
                time.sleep(2)
                print("Ingredients: Bread, heat.")
                time.sleep(1)
                print("Instructions: Apply heat to bread. Monitor until golden brown. Enjoy!")
            elif c == "important_data.log":
                print("Opening important_data.log...")
                time.sleep(1.5)
                print("--- LOG START ---")
                time.sleep(0.3)
                print(f"Timestamp: {datetime.now()} - User accessed important data.")
                time.sleep(0.3)
                print("Warning: Accessing this file may result in increased levels of enlightenment.")
                time.sleep(0.3)
                print("--- LOG END ---")
            elif c == "easter_egg.py":
                print("Executing easter_egg.py...")
                time.sleep(2)
                def animate_text(text, delay=0.1):
                    for char in text:
                        print(char, end='', flush=True)
                        time.sleep(delay)
                    print()
                animate_text("Hello there, curious user!")
                animate_text("You've found a hidden gem.")
                animate_text("May your day be filled with unexpected joys.")
            elif c == "funny_comic.ascii":
                print("Opening funny_comic.ascii...")
                time.sleep(1)
                print("""
    _.--""--._
    .'          `.
    /   O    O   \\
    |    \  ^^  /    |
    \    `----'    /
      `. _______ .'
        //_____\\
      (( ____ ))
        `------'
        Why don't scientists trust atoms?
        Because they make up everything!
                """)
            elif c == "top_secret.dat":
                print("Accessing top_secret.dat... Security clearance required.")
                password = input("Enter password: ")
                if password == "rory123":
                    print("Password accepted. Displaying highly classified information...")
                    time.sleep(3)
                    print("Top Secret: The meaning of life is... 42.")
                else:
                    print("Incorrect password. Access denied.")
            elif c == "system_info.txt":
                print("Gathering system information...")
                time.sleep(2)
                print(f"Current Date and Time: {datetime.now()}")
                print("meaning = 42")
                time.sleep(0.3)
                print("fetching history")
                time.sleep(random.randint(1, 2))
            elif c == "my_wishlist.txt":
                print("Opening my_wishlist.txt...")
                time.sleep(1)
                print("- A lifetime supply of pizza")
                print("- A robot butler named Jeeves")
                print("- The ability to understand what cats are thinking")
                print("- A trip to space (preferably with good snacks)")
                print("- World peace (if there's any left on the shelf)")
            elif c == "motivational_quote.txt":
                print("Opening motivational_quote.txt...")
                time.sleep(1.5)
                quotes = [
                    "The only way to do great work is to love what you do.",
                    "Strive for progress, not perfection.",
                    "Believe you can and you're halfway there.",
                    "The future belongs to those who believe in the beauty of their dreams.",
                    "Don't watch the clock; do what it does. Keep going."
                ]
                for i in quotes:
                    print(i)
                    time.sleep(1)
            else:
                print(f"Error: File '{c}' not found.")
        elif c == "is my sock wearable" and dlc_agreed:
            if random.choice([True, False]):
                print("The quantum entanglement suggests... maybe? Try at your own risk.")
            else:
                print("Due to the unpredictable nature of quantum entanglement, your sock remains stubbornly unwearable.")
        elif c == "banana philosophy" and dlc_agreed:
            print("A nearby banana peel begins to vibrate slightly. 'Ah, the ephemeral nature of potassium... and your fleeting existence...'")
        elif c == "rename planet" and dlc_agreed:
            planet_to_rename = input("Enter the planet you wish to rename: ")
            new_name = input("Enter the new, hopefully whimsical, name: ")
            print(f"Planet {planet_to_rename} is now officially known as {new_name}!")
        elif c == "receive text" and dlc_agreed:
            print("Your phone buzzes. It's a message from Mrs. Crabtree: 'I know what you did.'")
        elif c == "tralalero tralala" and dlc_agreed:
            print("""   _____       _         _
      |_   _|     | |       | |
        | |   _ __ | |_   __ _ _ __| |_ ___  _ __
        | |  | '_ \| | | / _` | '__| __/ _ \| '__|
      _| |_| | | | | | || (_| | |  | || (_) | |
    |_____|_| |_|_|\__\__,_|_|   \__\___/|_|  """)
        elif c == "vietnam" and dlc_agreed:
            print("""   __  __    _       ____       _
      |  \/  |   | |     |  _ \     | |
      | \  / | __ _| | ___ | |_) | __ _ ___| |_ ___
      | |\/| |/ _` | |/ _ \ |  _ < / _` / __| __/ _ \
      | |  | | (_| | |  __/ | |_) | (_| \__ \ ||  __/
      |_|  |_|\__,_|_|\___| |____/ \__,_|___/\__\___|""")
        elif c == "quotes" and dlc_agreed:
            print(""" """
    )
        elif c == "cancel dlc agreements" and dlc_agreed:
            print("NO MORE DLC FOR YOU! ARE YOU SURE THAT YOU WANT TO CANCEL? I'M A BAD PERSON WHO KILLS BABIES AND I HATE GOOD CONTENT OR NO")
            c_confirm = input(">") # Renamed to avoid conflict with outer 'c'
            if c_confirm == "I'M A BAD PERSON WHO KILLS BABIES AND I HATE GOOD CONTENT":
                print("DLC CANCELLED YOU MONSTER")
                dlc_agreed = False # Actually cancel the DLC
            elif c_confirm.lower() == "no": # Added .lower()
                print("DLC NOT CANCELLED")
            else:
                print("DLC not cancelled due to improper entry into the thing")
        elif c == "excercise plan":
            print("""1 Week excercise plan:
    Day 1: The Single Toe Tap Extravaganza
      - Lie down on the floor.
      - Slowly lift your right big toe one inch off the ground.
      - Hold for a count of one (Mississippi).
      - Gently lower your toe.
      - Repeat this... once.
      - Rest for 17 minutes while contemplating the immense effort you just exerted.

    Day 2: The Wall Stare Challenge
      - Stand facing a wall, approximately three feet away.
      - Stare intently at a single spot on the wall for five full minutes.
      - During this time, try your hardest not to blink or think about anything else.
      - Reward yourself with a sugary beverage and a nap.

    Day 3: The Arm Flail of Despair
      - Stand with your feet shoulder-width apart.
      - Close your eyes and flail your arms randomly for a duration of 15 seconds.
      - The goal is not coordination or any semblance of a workout, but to feel slightly ridiculous.
      - Cool down by gently wiggling your fingers.

    Day 4: The Pillow Lift Pyramid (Inverted)
      - Find the softest pillow you own.
      - Carefully lift the pillow from the couch to your lap.
      - Hold it there for ten seconds.
      - Slowly return the pillow to the couch.
      - This constitutes one rep. Perform zero more reps.

    Day 5: The Existential Stretch
      - Sit comfortably in a chair.
      - Slowly reach one arm towards the ceiling as if questioning the very fabric of reality.
      - Hold this pose for a count of two (Mississippi, Tennessee).
      - Lower your arm and repeat with the other arm.
      - Ponder the meaninglessness of physical exertion.

    Day 6 & 7: Mandatory Rest (You've earned it... sort of.)
      - Absolutely no physical activity allowed. This includes walking to the fridge for snacks. If you're hungry, have someone bring the snacks to you.
    """)
        elif c == "defined glitch report":
            c = input("What is the glitch \n>")
            print("we will take your issue of",c,"very seriously and it is of our utmose importance")
        elif c == "todays comicomic":
            print("""
          Coding Tips for Coders
    How to call functions in different languages
    Part 1: Javascript
    In javascript you call a function by doing: function{function_name(function_parameters)}

          Part 2: Python
    In Python, you call a function by doing: function_name(parameter_1 = "parameter")

          Part 3: C++
    In c++, you call a function by doing: function call function_name parameters("parameter 1")
          """)
        elif c == "recive text" and dlc_agreed: # Typo: "recive" should be "receive"
            while c != "checked": # Changed `not c == "checked"` to `c != "checked"` for readability
                time.sleep(random.randint(1, 3))
                print("check your phone and type 'checked' when done")
                c = input(">")
            print("good boy")
        # --- START OF HACKING PORTAL INTEGRATION ---
        elif c.lower() == "dlc hacking portal" and dlc_agreed: # Command to enter the hacking portal
            prnt("Welcome to the Terminal Hacking Portal!")
            prnt("Who do you wish to hack?")
            prnt("Options available are:")
            print(", ".join(unms)) # Display available usernames cleanly

            # User chooses target to hack (with improved input handling)
            while True:
                prnt("Who do you want to hack?")
                hack = input("").strip().lower()
                if hack in unms:
                    break
                else:
                    prnt("That name is not in the database. Please choose from: " + ", ".join(unms))

            hacsec = False
            while not hacsec:
                prnt("Please input password:")
                pwrd = input()
                if passwords[hack] == pwrd:
                    prnt("Hacking successful!")
                    hacsec = True
                elif pwrd.lower() == "autocheck": # Added .lower() for case-insensitivity
                    prnt("Starting autocheck...")
                    target_password = passwords[hack]
                    # Adjust iterations based on user, or make it dynamic if desired
                    if hack == "inanem_m":
                      iterations = 6
                    elif hack == "max_eich":
                      iterations = 178
                    elif hack == "schrib_s":
                      iterations = 259
                    elif hack == "web_reed":
                      iterations = 500
                    elif hack == "romeo_ln":
                      iterations = 500
                    elif hack == "-stulen-":
                      iterations = 500
                    else:
                      iterations = 100 # Default fallback

                    for i in range(iterations):
                        print(generate_random_string(8))
                        time.sleep(0.01)
                    print() # Newline after the random strings
                    prnt(target_password)
                    prnt("Password found!")
                else:
                    prnt("Incorrect password", 0.5)
            prnt(f"Hacked! All websites that {hack} visits will be borked.")
        # --- END OF HACKING PORTAL INTEGRATION ---
        elif not agreed_to_tos:
            print("Please agree to the base TOS to use Termiplus.")
        elif c == "i love termiplus":
          prnt("thank you very much")
        elif c == "i hate termiplus":
          prnt("you're a dingus")
        elif c == "please kindly reset termiplus":
          breaky = True
          break
        elif c == "review":
          with open(review_file, 'r') as inp, open(review_file, 'w') as oup:
            prnt("enter review")
            review = input(">")
            prnt(f"is '{review}' correct y/n")
            if input(">") == "y":
              oup.write(review)
            else:
              prnt("returining to main loop")
        elif c == "read reviews":
          with open(review_file, 'r') as infile:
            print(infile.read())
        elif c == "sudo rm rf no-preserve-root":
          print("bricking...")
          time.sleep(0.5)
          import brick
        elif c == "boba":
          print("how long")
          l = input(">")
          print("Fast or slow f/s")
          fs = input(">")
          if fs == "f":
            fs = False
          else:
            fs = True
          boba.setup_boba(int(l), fs)
        elif c == "set lawyer":
          try:
            NAME = input("NAME>")
            TYPE = input("TYPE>")
            RATE = float(input("RATE>"))
            SLI1 = float(input("SLI1>"))
            SLI2 = float(input("SLI2>"))
            SLI3 = float(input("SLI3>"))
            LIN1 = float(input("LIN1>"))
            LIN2 = float(input("LIN2>"))
            LIN3 = float(input("LIN3>"))
            l = lawyer(NAME, TYPE, RATE, SLI1, SLI2, SLI3, LIN1, LIN2, LIN3)
            print("lawyer 'l' is set")
          except Exception as error:
            print(error)
            print("Aborted lawyer")
        elif c == "l.show_info":
          l.print_info()
        elif c == "l.inits_explained":
          l.inits_explained()
        else:
          try:
            termiscript.run(c)
          except Exception as error:
            print(error)
      
    if breaky == True:
      start()