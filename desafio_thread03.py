from tkinter import *
from threading import *
import random
posx = random.randint(0,400)
posy = random.randint(0,400)
x = 0


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

window = Tk()
#config da window
window.geometry("500x500+200+100")
window.title("TI fora da caixa")
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
window.mainloop()
