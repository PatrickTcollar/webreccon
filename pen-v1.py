from tkinter import *
from socket import *
import subprocess
import time
import nmap
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        # Criamos a janela principal
        self.janela_principal = Tk()
        self.janela_principal.title("WebReccon")

        # Criando os frames
        self.frame_cima  = Frame(self.janela_principal) 
        self.frame_baixo = Frame(self.janela_principal) 

        # Criando label e botões do frame de cima
        self.label = Label(self.frame_cima, text='Enter host for scanning:')

        # Criando o widget de entrada
        self.entrada = Entry(self.frame_cima, width=30)

        # Empacotando label e entrada no frame de cima
        self.label.pack(side='left')
        self.entrada.pack(side='left')

        # Criando os botões, no frame de baixo
        self.botao = Button(self.frame_baixo, text='Executar', command=self.cmd_click)
        self.botao_sair = Button(self.frame_baixo, text='Sair', command=self.janela_principal.quit)

        # Empacotando os botões no frame de baixo
        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')

        # Empacotando os botões janela principal
        self.botao.pack()
        self.botao_sair.pack()

        # Empacotando os frames na janela principal
        self.frame_cima.pack()
        self.frame_baixo.pack()

        # Rodando
        mainloop()
                

    def cmd_click(self):
        begin = 79
        end = 80
        target = self.entrada.get()
        scanner = nmap.PortScanner()
        for i in range(begin,end+1):
            res = scanner.scan(target, str(i))
            res = res['scan'][target]['tcp'][i]['state']
            print(f'port {i} is {res}.')


gui = MinhaGUI()
