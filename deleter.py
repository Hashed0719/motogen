import os
import time 
from threading import Thread

def webm_deleter():
  while True:
    listt=os.listdir()
    wbmfiles=[]
    for fiile in listt:
      if fiile.endswith(".webm") or fiile.endswith(".m4a"):
        wbmfiles.append(fiile)

    while wbmfiles:
      print('inside loop')
      for x in range(len(wbmfiles)):
        time.sleep(300)
        os.remove(wbmfiles[0])
        wbmfiles.pop(0)


def keep_clutter_out():
  webm_thread = Thread(target=webm_deleter)
  webm_thread.start()