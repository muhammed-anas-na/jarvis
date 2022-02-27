import webbrowser as web
import time
import keyboard

def whatsapp(number  , message):
    numb = '+91' + number
    open_chat="https://web.whatsapp.com/send?phone="+number+"&text="+message
    print(open_chat)
    web.open(open_chat)
    time.sleep(15)
    keyboard.press('enter')
