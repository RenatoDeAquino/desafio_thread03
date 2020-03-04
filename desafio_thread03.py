from tkinter import *
from threading import *
import threading
import random
posx = random.randint(0,400)
posy = random.randint(0,400)
x = 0
tempinho = 5.0
tempo = 10
def aoClicar():
    global pontos
    pontos.destroy()
    posx = random.randint(0,400)
    posy = random.randint(0,400)
    botao.pack()
    botao.place(bordermode = OUTSIDE,heigh = 70,width = 70,x = posx,y = posy)
    global x
    x += 1
    pontos = Label(window,text = "seu total de pontos é: "+str(x), font ="impact 15 bold")
    pontos.pack(side = "bottom")
    global tempo
    tempo -= 0.4
    global tempinho
    tempinho -= 0.4
def altera_botao():
    posx = random.randint(0,400)
    posy = random.randint(0,400)
    botao.pack()
    botao.place(bordermode = OUTSIDE,heigh = 70,width = 70,x = posx,y = posy)
    timer = threading.Timer(tempinho, altera_botao)
    timer.start()

def fecha_auto():
    global mensagem
    mensagem.destroy()
    global botao
    botao.destroy()
    global time
    time.destroy()
    global pontos
    global x
    ponto = Label(window,text = "Acabou seu total de pontos é: "+str(x),font = "impact 15 bold")
    pontos.pack(side = "botton")
window = Tk()
#config da window
window.geometry("500x500+200+100")
window.title("botao do inferno")
#label mensagem
mensagem = Label(window, text="Aperte o botão", font="impact 15 bold")
mensagem.pack()
mensagem.place(x= 0, y =0)
#label pontos
pontos = Label(window,text = "seu total de pontos é: "+str(x), font ="impact 15 bold")
pontos.pack(side = "bottom")
#botao de ação
botao = Button(window, text="Clique Aqui", command=aoClicar)
botao.pack()
botao.place(bordermode = OUTSIDE,heigh = 70,width = 70,x = posx,y = posy)
#executa o tkinter
timer = threading.Timer(tempinho, altera_botao)
timer.start()
mano = threading.Timer(10.0,fecha_auto)
mano.start()
window.after(10000,window.destroy)
window.mainloop()
