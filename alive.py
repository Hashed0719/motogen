from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def countrun(filename):
  with open(filename,'r') as f:
    count = f.read()
    count = int(count)
    count += 1
    print(instance_count:=f"{count}")
  f.close()

  with open(filename,'w') as f:
    f.write(str(count))