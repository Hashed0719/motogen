from LavalinkServer import start_LavalinkServer
from flask import Flask
from threading import Thread
from sys import stdout as sys
app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t2 = Thread(target=start_LavalinkServer)
    t.start()
    t2.start()

def countrun(filename):
  with open(filename,'r') as f:
    count = f.read()
    count = int(count)
    count += 1
    sys.write(instance_count:=f"{count}")
  f.close()

  with open(filename,'w') as f:
    f.write(str(count))