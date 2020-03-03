from threading import Timer
from tkinter import *
import random

def setInterval(function, interval, *params, **kwparams):
    def setTimer(wrapper):
        wrapper.timer = Timer(interval, wrapper)
        wrapper.timer.start()

    def wrapper():
        function(*params, **kwparams)
        setTimer(wrapper)
    
    setTimer(wrapper)
    return wrapper
def clearInterval(wrapper):
    wrapper.timer.cancel()
    

class Application:
    def __init__(self, master=None):
    
          l = Label(master, text = "u dont pega me")
          l.place(relx = 1, rely = 1)
root = Tk()
root.geometry('500x500')
Application(root)
root.mainloop()
