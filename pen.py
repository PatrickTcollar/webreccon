from tkinter import *
from socket import *
import time
import nmap

startime = time.time()

menu_inicial = Tk()
menu_inicial.title("Penetration Test")
menu_inicial.geometry("500x300")
menu_inicial.configure(background="#dde")


Label(menu_inicial, text="Enter host for scanning: ", background="#dde", foreground="#009", anchor=W).place(x=10,y=10,width=100,height=20)


textbox1 = Entry(menu_inicial)
textbox1.place(x=10,y=30,width=150,height=20)
            
def cmd_click():
    begin = 50
    end = 80
    target = '192.168.0.104'
    scanner = nmap.PortScanner()
    for i in range(begin,end+1):
        res = scanner.scan(target, str(i))
        res = res['scan'][target]['tcp'][i]['state']
        print(f'port {i} is {res}.')

#botão
botao1 = Button(menu_inicial, text="Executar", command=cmd_click)
botao1.pack()



menu_inicial.mainloop()