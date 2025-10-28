#functions as main.py
#losless-kernel.py
#replace atermiplusfold with whatever you want as long as it has a SI() and a GO() function by the Losless Norms
import atermiplusfold
from termiscript import run
while True:
  c = input(">")
  if c == "straightinstall":
    atermiplusfold.SI()
  elif c == "boot":
    atermiplusfold.GO()
  elif "rm" in c:
    print("you may not rm")
  elif "do_this_now" in c:
    print("you may not do_this_now")
  else:
    run(c)