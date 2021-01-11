from Usuarios import Usuarios
from tkinter import *

class App:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo.pack()

        self.lblidusuario = Label(self.container2, text="idUsuario:", width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", width=10, command = self.buscarUsuario)
        self.btnBuscar.pack(side=RIGHT)

        self.lblaluno = Label(self.container3, text="Aluno:", width=10)
        self.lblaluno.pack(side=LEFT)

        self.txtaluno = Entry(self.container3)
        self.txtaluno["width"] = 25
        self.txtaluno.pack(side=LEFT)

        self.lblidade = Label(self.container4, text="Idade:", width=10)
        self.lblidade.pack(side=LEFT)

        self.txtidade = Entry(self.container4)
        self.txtidade["width"] = 25
        self.txtidade.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="E-mail:", width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail.pack(side=LEFT)

        self.lblcurso = Label(self.container6, text="Curso:", width=10)
        self.lblcurso.pack(side=LEFT)

        self.txtcurso = Entry(self.container6)
        self.txtcurso["width"] = 25
        self.txtcurso.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg.pack()


    def inserirUsuario(self):
        user = Usuarios()

        user.aluno = self.txtaluno.get()
        user.idade = self.txtidade.get()
        user.email = self.txtemail.get()
        user.curso = self.txtcurso.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidusuario.delete(0, END)
        self.txtaluno.delete(0, END)
        self.txtidade.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtcurso.delete(0, END)
        self.txtsenha.delete(0, END)



    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.aluno = self.txtaluno.get()
        user.idade = self.txtidade.get()
        user.email = self.txtemail.get()
        user.curso = self.txtcurso.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidusuario.delete(0, END)
        self.txtaluno.delete(0, END)
        self.txtidade.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtcurso.delete(0, END)
        self.txtsenha.delete(0, END)



    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidusuario.delete(0, END)
        self.txtaluno.delete(0, END)
        self.txtidade.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtcurso.delete(0, END)
        self.txtsenha.delete(0, END)


    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtaluno.delete(0, END)
        self.txtaluno.insert(INSERT, user.aluno)

        self.txtidade.delete(0, END)
        self.txtidade.insert(INSERT,user.idade)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)

        self.txtcurso.delete(0, END)
        self.txtcurso.insert(INSERT, user.curso)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT,user.senha)



root = Tk()
App(root)
root.mainloop()