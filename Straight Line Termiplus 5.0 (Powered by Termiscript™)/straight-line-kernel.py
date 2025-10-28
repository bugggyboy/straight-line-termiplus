#functions as main.py
#straight-line-kernel.py
#replace atermiplusfold with whatever you want as long as it has a SI() and a GO() function by the Straight Line Norms
import time
import random
import atermiplusfold
c = ""
def testbrick(c):
  tf = [True, False]
  if c == "from datetime import datetime":
    from datetime import datetime
    for i in range(30):
      print(datetime.now())
  elif "import" in c:
    print("this command may install suspicous files, do you wish to install y/n")
    if input(">") == "n":
      return
    if random.choice(tf):
      import malware
    else:
      import brick
print("use straightinstall? y/n")
c = input(">")
si = False
if c == "y":
  si = True
if si:
  atermiplusfold.SI()
while not c == "sudo load-file web:https://www.termiplus.com/download/termiplus.iso":
  if si:
    c = "sudo load-file web:https://www.termiplus.com/download/termiplus.iso"
  else:
    c = input(">")
  print(c)
  testbrick(c)
while not c == ("sudo install termiplus.iso"):
  if si:
    c = "sudo install termiplus.iso"
  else:
    c = input(">")
  testbrick(c)
  print(c)
  print("comp/downloads/termiplus.iso")
while not c == ("sudo etch comp/downloads/termiplus.iso"):
  if si:
    c = "sudo etch comp/downloads/termiplus.iso"
  else:
    c = input(">")
  testbrick(c)
  print(c)
  print("comp/etch/--termiplus-fold.zip")
while not c == ("sudo install-os comp/etch/--termiplus-fold.zip"):
  if si:
    c = "sudo install-os comp/etch/--termiplus-fold.zip"
  else:
    c = input(">")
  print(c)
  testbrick(c)
if c == ("sudo install-os comp/etch/--termiplus-fold.zip"):
  print(c)
  atermiplusfold.GO()