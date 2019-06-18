'''
COMPUTAÇÃO 2, PROF.A FERNANDA

TRABALHO FINAL: AGENDA DE CONTATOS COM MEMÓRIA

ALUNO: ARTHUR COSTA GARCIA
DRE: 118058547

REQUISITOS:

A interface gráfica deve ser programada em uma classe
(assim como foi feito nas aulas práticas). É permitido
utilizar mais de uma classe.

Utilize pelo menos duas dentre as seguintes widgets:
canvas, button, radiobutton, checkbutton, label, menu,
scrollbar, entry, text, scrollbar, messagebox, nova janela.
Outras widgets também podem ser utilizadas, mas o frame não conta.

O trabalho deve ter no mínimo 100 linhas de código.

Agenda de contatos com memória, permitindo adicionar, remover e buscar contatos.
'''


from tkinter import *
from tkinter import messagebox

class AgendaContatos():
    def __init__(self, master):
        
        ####################################################################################################
        # CRIANDO A JANELA DO TKINTER E O FRAME PRINCIPAL
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        ####################################################################################################


        ####################################################################################################
        # CRIANDO O BOTAO ADICIONAR E SUAS ENTRADAS
        self.btnAdd = Button(master, text = 'Adicionar', command = self.AddContato)
        self.btnAdd.grid(row = 0, rowspan = 2, column = 0, sticky = W, padx = 10, ipady = 12)

        self.caixaAddNome = Entry(master)
        self.caixaAddNome.insert(END, 'Nome')
        self.caixaAddNome.bind("<Button-1>", self.Del_On_Click)
        self.caixaAddNome.grid(row = 0, column = 1, sticky = W)

        self.caixaAddNum = Entry(master)
        self.caixaAddNum.insert(END, 'Telefone')
        self.caixaAddNum.bind("<Button-1>", self.Del_On_Click)
        self.caixaAddNum.grid(row = 1, column = 1, sticky = W)
        ####################################################################################################
        
        
        ####################################################################################################
        # CRIANDO O BOTAO BUSCAR E SUAS ENTRADAS
        self.btnBuscar = Button(master, text = 'Buscar', command = self.BuscarContato)
        self.btnBuscar.grid(row = 2, rowspan = 2, column = 0, sticky = W, padx = 10, ipady = 12, ipadx = 8)

        self.caixaBuscarNome = Entry(master)
        self.caixaBuscarNome.insert(END, 'Nome')
        self.caixaBuscarNome.bind("<Button-1>", self.Del_On_Click)
        self.caixaBuscarNome.grid(row = 2, column = 1, sticky = W)

        self.caixaBuscarNum = Entry(master)
        self.caixaBuscarNum.bind("<Button-1>", self.Del_On_Click)
        self.caixaBuscarNum.insert(END, 'Telefone') 
        self.caixaBuscarNum.grid(row = 3, column = 1, sticky = W)
        ####################################################################################################


        ####################################################################################################
        # CRIANDO BARRA DE MENU E SEUS BOTOES
        self.menu = Menu(self.master)
        self.master.config(menu = self.menu)
        self.fileMenu = Menu(self.menu)
        self.menu.add_cascade(label = 'File', menu = self.fileMenu)
        self.fileMenu.add_command(label = 'Salvar', command = self.Save_File)
        ####################################################################################################
        

        ####################################################################################################
        # CRIANDO BOTAO REMOVER E SUAS ENTRADAS
        self.btnDel = Button(master, text = 'Remover', command = self.DelContato)
        self.btnDel.grid(row = 4, rowspan = 2, column = 0, sticky = W, padx = 10, ipady = 12, ipadx = 2)

        self.caixaDelNome = Entry(master)
        self.caixaDelNome.insert(END, 'Nome')
        self.caixaDelNome.bind("<Button-1>", self.Del_On_Click)
        self.caixaDelNome.grid(row = 4, column = 1, sticky = W)

        self.caixaDelNum = Entry(master)
        self.caixaDelNum.insert(END, 'Telefone')
        self.caixaDelNum.bind("<Button-1>", self.Del_On_Click)
        self.caixaDelNum.grid(row = 5, column = 1, sticky = W)
        ####################################################################################################


        ####################################################################################################
        # CRIANDO A LISTA DE CONTATOS
        self.listFrame = Frame(master)
        self.listFrame.grid(row = 0, column = 3, rowspan = 6, padx = 10)
        
        self.listaContatos = Listbox(self.listFrame)
        self.listaContatos.grid(row = 0, column = 0)

        self.scrolly = Scrollbar(self.listFrame, orient = VERTICAL)
        self.scrollx = Scrollbar(self.listFrame, orient = HORIZONTAL)
        
        self.listaContatos.config(yscrollcommand = self.scrolly.set, xscrollcommand = self.scrollx.set)
        
        self.scrolly.config(command = self.listaContatos.yview)
        self.scrolly.grid(row = 0, column = 1, sticky = NS)
        
        self.scrollx.config(command = self.listaContatos.xview)
        self.scrollx.grid(row = 1, column = 0, sticky = EW)
        ####################################################################################################


        ####################################################################################################
        # IMPORTANDO CONTATOS DO ARQUIVO DE MEMORIA PADRAO
        with open('memoriaContatos.txt', 'r') as f:
            conteudo = f.readlines()
            if conteudo == '':
                pass
            else:
                for item in conteudo:
                    self.listaContatos.insert(END, item.strip())
        ####################################################################################################


    def AddContato(self):
        nome = self.caixaAddNome.get().upper().strip()
        num = self.caixaAddNum.get().strip()
        temp = self.listaContatos.get(0, END)

        if num in temp:
            for i in range(len(temp)):
                if num == temp[i]:
                    messagebox.showinfo("Aviso", "Este numero foi adicionado ao contato %s" %temp[i-1])
        elif nome == '':
            print('Eh necessario acrescentar o nome, mesmo que ja haja outros numeros com o mesmo.')
        elif num not in temp:
            self.listaContatos.insert(END, nome)
            self.listaContatos.insert(END, num)
            self.listaContatos.insert(END, '\n')


    def DelContato(self):
        nome = self.caixaDelNome.get().upper().strip()
        num = self.caixaDelNum.get().strip()
        temp = self.listaContatos.get(0, END)

        if nome and num in temp:
            for i in range(len(temp)):
                if nome == temp[i] and num == temp[i+1]:
                    for j in range(3):
                        self.listaContatos.delete(i)
        elif nome and num not in temp:
            messagebox.showinfo("Aviso", "Contato inexistente.")
        elif nome == '' or num == '':
            messagebox.showinfo("Aviso", "Ambas as caixas precisam estar preenchidas para remover um contato!")
        elif nome == 'Nome' or num == 'Telefone':
            messagebox.showinfo("Aviso", "Ambas as caixas precisam estar preenchidas para remover um contato!")


    def BuscarContato(self):
        self.listaContatos.select_clear(0, END)
        
        nome = self.caixaBuscarNome.get().upper().strip()
        num = self.caixaBuscarNum.get().strip()
        temp = self.listaContatos.get(0, END)

        if nome or num in temp:
            for i in range(len(temp)):
                if nome != '' or num != '':
                    if nome == temp[i] and num == temp[i+1]:
                        self.listaContatos.select_set(i)
                        self.listaContatos.see(i)
                        self.listaContatos.select_set(i+1)
                        self.listaContatos.see(i+1)
                    elif nome == temp[i] and num == '':
                        self.listaContatos.select_set(i)
                        self.listaContatos.see(i)
                    elif nome == '' and num == temp[i]:
                        self.listaContatos.select_set(i)
                        self.listaContatos.see(i)
        else:
            messagebox.showinfo("Aviso", "Contato não encontrado.")
    

    def Del_On_Click(self, event):
        event.widget.delete(0, END)


    def Save_File(self):
        nItens = len(self.listaContatos.get(0, END))
        with open('memoriaContatos.txt', 'w') as f:
            for i in range(nItens - 1):
                item = self.listaContatos.get(i)
                
                f.write('%s\n' %item)
            f.write('\n')


JanelaPrincipal = Tk()

Agenda = AgendaContatos(JanelaPrincipal)

JanelaPrincipal.mainloop()