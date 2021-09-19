import pyautogui,webbrowser
import random
from pynput import keyboard as kb

from time import sleep

webbrowser.open('www.discord.com/channels/@me')
sleep(10);

isRuning = True
def pulsar (tecla):
    if tecla == kb.KeyCode.from_char('w'):
        isRuning = False
    print(tecla)

while(isRuning):
    pyautogui.typewrite(random.choice(seq=[
    'raideo','raid','raiding']));
    pyautogui.press("Enter")

Listener = kb.Listener(pulsar)
Listener.start()

while(Listener.is_alive()):
    pass
