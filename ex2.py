from tkinter import *

#versao1
def pegarValores():
    todosInputs = []
    for i in inputs:
        todosInputs.append(i.get().lower())
    selecionado = v0.get()
    todosInputs.append(selecionado)
    return todosInputs


def erro():
    newWindow = Tk()
    newWindow.geometry('300x200')
    newWindow.title("Erro")
    newWindow.config(bg="#9f111b")
    newlbl = Label(newWindow, text= "Erro, digite um valor válido" , font=('helvetica', 16), fg='yellow', bg="#9f111b")
    newlbl.pack()
    newWindow.mainloop()

def moldarValores(y):
    itens = ''  
    for i in y:
        try:
            int(y[1])
        except:
            return False
        if len(str(i)) == 0 or y[-1] == 0:
            return False
    for i in y:        
        if y.index(i) != len(y)-1:
            itens += str(i) + "|"
        else:
            itens += str(i) + "\n"
    return itens 
    


def escrever(y):
    db = open('pasta.txt', 'a', encoding = "utf-8")
    db.write(y)
    db.close()


def ler():
    leitura = open("pasta.txt", "r", encoding='utf-8')
    leitura = leitura.read()
    newWindow = Tk()
    newWindow.geometry('1200x800')
    newWindow.title("Albuns cadastrados")
    newWindow.config(bg="#9f111b")
    leitura = leitura.split('\n')
    albuns = []
    for i in leitura:
        albuns.append(i.split('|'))
    albuns.pop()
    lblMain = Label(newWindow, text= 'Albuns Cadastrados', font=('helvetica', 32),bg="#9f111b",fg="#292c37") 
    lblMain.pack()
    for i in albuns:
       x = " -- ".join(i)
       lbl = Label(newWindow, text= x, font=('helvetica', 16), bg='#ccc',borderwidth=2, relief="solid",width=80)
       lbl.pack()
    newWindow.mainloop()


def enviar(x):
    values = pegarValores()
    valores = moldarValores(values)
    if valores == False:
        erro()
    else:    
        escrever(valores)
        ler()

#versao2
def pesquisarAno(x):

    def LerAnos():
        valueRadio = m0.get()
        valueText = text.get()
        leitura = open("pasta.txt", "r", encoding='utf-8')
        leitura = leitura.read()
        leitura = leitura.split('\n')
        albuns = []
        for i in leitura:
            albuns.append(i.split('|'))
        albuns.pop()
        Albuns = []
        for i in albuns:
            try:
                if valueRadio == "Antes" and int(valueText) >= int(i[1]):
                    Albuns.append(i[0])
                else:
                    if valueRadio == "Depois" and int(valueText) <= int(i[1]):
                        Albuns.append(i[0])   
            except:
                return False  
        return Albuns

    def pesquisaAno(x):
        
        albuns = LerAnos()
        if albuns == False:
            erro()
        else:
            newWindow2 = Tk()
            newWindow2.geometry("300x400")
            newWindow2.title("Resultado")
            newWindow2.config( bg="#9f111b")
            for i in albuns:
                lbl = Label(newWindow2,text=i, font= ("Helvetica", 18), fg="#292c37", bg="#CCCCCC",borderwidth=2, relief="solid")
                lbl.pack()
            newWindow2.mainloop()
            
    
    newWindow = Tk()
    newWindow.geometry('800x400')
    newWindow.title("Pesquisa")
    newWindow.config(bg="#9f111b")
    lbl = Label(newWindow, text="Pesquisa Por Ano", font=("Helvetica", 32),bg="#9f111b",fg="#292c37")
    lbl.pack()
    m0 = StringVar(newWindow)
    m0.set("Antes")
    r3 = Radiobutton(newWindow, text="Antes", value="Antes", font=("Helvetica",12),variable=m0,bg="#9f111b", fg="#292c37",borderwidth=2, relief="solid")
    r4 = Radiobutton(newWindow, text="Depois", value="Depois", font=("Helvetica",12), variable=m0,bg="#9f111b", fg="#292c37",borderwidth=2, relief="solid")
        
    text = Entry(newWindow, background='#CCCCCC', font=("Helvetica", 15))
    r3.place(x=5, y=65,width=80)
    r4.place(x=715, y=65,width=80)
    text.place(x= 90, y = 65,width=620,height=28)
        
    botao = Button(newWindow,text="Pesquisar",font=("Helvetica",16), bg='#cccccc', fg="#292c37",borderwidth=2, relief="solid")
    botao.place(x = 5 , y=120)
    botao.bind('<Button-1>', pesquisaAno)
    mainloop() 




def pesquisarArt(x):
    def leitura():
        valor = text.get().lower()
        leitura = open("pasta.txt", "r", encoding='utf-8')
        leitura = leitura.read()
        leitura = leitura.split('\n')
        albuns = []
        for i in leitura:
            albuns.append(i.split('|'))
        albuns.pop()
        artistas = []
        for i in albuns:
            if valor in i[2].lower():
                if i[2] not in artistas:
                    artistas.append(i[2])
                else:
                    continue
        return artistas

    def pesquisaNome(x):
        artistas = leitura()
        newWindow2 = Tk()
        newWindow2.geometry("300x400")
        newWindow2.title("Resultado")
        newWindow2.config(bg="#9f111b")
        pos = 0
        for i in artistas:
            labelArt = Label(newWindow2, text = i, font= ("Helvetica", 18), fg="#292c37", bg="#CCCCCC",borderwidth=2, relief="solid")
            labelArt.pack()
            pos += 30
        
    newWindow = Tk()
    newWindow.geometry('800x400')
    newWindow.title("Pesquisa")
    newWindow.config(bg='#9f111b')
    lbl = Label(newWindow, text="Pesquisa Por Artista", fg="#292c37", font=("Helvetica", 32),bg='#9f111b')
    lbl.pack()
    
    label = Label(newWindow, text="Nome:", font=('helvetica', 18), bg="#9f111b", fg="#292c37")
    label.place(x=0,y=60)

    text = Entry(newWindow, bg="#cccccc", fg="#292c37",font=('helvetica', 18))
    text.place(x= 75, y = 60, width=700, height=30)
    
    botao = Button(newWindow,text="Pesquisar",font=("Helvetica",10))
    botao.place(x = 5, y=110)
    botao.bind('<Button-1>', pesquisaNome)
    mainloop() 

#window
window = Tk()
window.title("Músicas")
window.geometry('920x800')
window.configure(background='#9f111b')


#label
labelPrincipal = Label(text="Cadastro de album",fg="#000000", font=("Helvetica", 32),bg='#9f111b')
labelPrincipal.place(x=0)

temas = ["nome do álbum","ano de lançamento","nome da banda/artista","álbum lançamento do artista"]
constDePosicionamento = 55
for i in temas:
    lbl = Label(window, text= i.capitalize() + ":" , font=('helvetica', 18), bg="#9f111b", fg="#292c37")
    lbl.pack()
    lbl.place(x=5, y = constDePosicionamento)
    constDePosicionamento += 85
    if temas.index(i) == len(temas)-1:
        constDePosicionamento = 100

#inputs
inputs = []
for x in range(0, len(temas)):
    if x == len(temas)- 1:
        v0 = StringVar()
        v0.set("Não")
        r1 = Radiobutton(window, text='Sim', variable=v0, value="Sim",font=('helvetica', 18), bg='#cccccc', fg="#292c37", borderwidth=2, relief="solid")
        r2 = Radiobutton(window, text='Não', variable=v0, value="Não",font=('helvetica', 18), bg='#cccccc', fg="#292c37",borderwidth=2, relief="solid")
        r1.place(x=5,y = constDePosicionamento)
        r2.place(x=120, y= constDePosicionamento)
    else:
        txt = Entry(window, bg="#cccccc", fg="#292c37",font=('helvetica', 18))
        txt.place(x= 5, y = constDePosicionamento, width=900, height=30)
        inputs.append(txt)
        constDePosicionamento += 80

#botao
botao = Button(window,text="Enviar",font=("Helvetica",16), bg='#cccccc', fg="#292c37",borderwidth=2, relief="solid")
botao.place(x = 5, y=410,)
botao.bind('<Button-1>', enviar)
botao2 = Button(window,text="Pesquisar por artista",font=("Helvetica",16), bg='#cccccc', fg="#292c37",borderwidth=2, relief="solid")
botao2.place(x = 5, y=460)
botao2.bind('<Button-1>', pesquisarArt)
botao3 = Button(window,text="Pesquisar por ano",font=("Helvetica",16), bg='#cccccc', fg="#292c37",borderwidth=2, relief="solid")
botao3.place(x = 5, y=510)
botao3.bind('<Button-1>', pesquisarAno)


window.mainloop()