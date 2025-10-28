 #termiscript.py
import os
import sys
import time
def prnt(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def run(c = "this command will never be used"):
  try:
    if "do_this_now " in c:
      execute(c.replace("do_this_now ", ""))
    elif "yes" in c:
      while True:
        run(c.replace("yes ", ""))
    elif "print " in c:
      print(c.replace("print ", ""))
    elif "echo >" in c:
      c1 = c.split('|')
      c2 = c1[0]
      c3 = c1[1]
      with open(c3, "w") as the:
        the.write(c2.replace("echo >", ""))
    elif "cat" in c:
      c = c.replace("cat ", "")
      try:
        with open(c, "r") as the:
          print (the.read())
      except FileNotFoundError:
        run(f"print nothing existed in this file previously, this is, please 'echo >' to set this file: "+c)
    elif "rm" in c:
      c = c.replace("rm ", "")
      os.remove(c)
    elif "for i in " in c:
      c = c.replace("for i in ", "")
      c1 = c.split('|')
      c2 = c1[0]
      c3 = int(c1[1])
      for i in range(c3):
        run("print "+c2)
    elif "FUDGE" in c:
      print("do you need help? type help") #even though there's no help command
    elif "@" in c:
      c1 = c.split("@")
      c2 = c1[0]
      c3 = c1[1]
      print("print", float(int(int(c2)/int(c3))),"r",float(int(int(c2)%int(c3))))
    elif c == "help":
      print("""print <text>
echo > <text>|<filename>
cat <filename>
rm <filename>
for i in <text>|<number>
<number1> @ <number2>
FUDGE
yes <command>
Any Python code""")
    elif "prnt " in c:
      c = c.replace("prnt ", "")
      with open(c, "r") as the:
        prnt(the.read())
    else:
      exec(c)
  except Exception as error:
    print("EL ERROR! ", error)

def execute(c):
  exec(c, globals())
if __name__ == "__main__":
  print("exclusive termiscript access -- no kernel")
  while True:
    run(input(">"))
else:
  print("Shell powered by Termiscript™")