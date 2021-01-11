from Banco import Info

class Usuarios(object):
    def __init__(self, idusuario = 0, aluno = "", idade = 0, email = "", curso = "", senha = ""):
        self.Usuario = {}
        self.idusuario = idusuario
        self.aluno = aluno
        self.idade = idade
        self.email = email
        self.curso = curso
        self.senha = senha

    def insertUser(self):

        banco = Info()

        try:
            c = banco.conectar.cursor()

            c.execute("insert into usuarios (aluno, idade, email, curso, senha) values ('" + self.aluno + "', '" + self.idade + "', '" + self.email + "', '" + self.curso + "', '" + self.senha + "' )")

            banco.conectar.commit()
            c.close()

            return "Cadastro realizado com sucesso!"
        except:
            return "Oops! Houve algum erro durante o cadastro."

    def updateUser(self):
        banco = Info()

        try:
            c = banco.conectar.cursor()

            c.execute("update usuarios set aluno = '" + self.aluno + "', idade = '" + self.idade + "', email = '" + self.email + "', curso = '" + self.curso + "', senha = '" + self.senha + "' where idusuario = " + self.idusuario + " ")

            banco.conectar.commit()
            c.close()

            return "Atualizado com sucesso!"
        except:
            return "Houve um erro durante a atualização!"

    def deleteUser(self):
        banco = Info()

        try:
            c = banco.conectar.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conectar.commit()
            c.close()

            return "Excluído com sucesso!"
        except:
            return "Erro ao excluir, verifique os dados e tente novamente!"

    def selectUser(self, idusuario):
        banco = Info()

        try:
            c = banco.conectar.cursor()

            c.execute("select * from usuarios where idusuario = " + idusuario + " ")

            for selected in c:
                self.idusuario = selected[0]
                self.aluno = selected[1]
                self.idade = selected[2]
                self.email = selected[3]
                self.curso = selected[4]
                self.senha = selected[5]

            c.close()

            return "Busca realizada com sucesso!"
        except:
            return "Ocorreu um erro durante a busca!"
