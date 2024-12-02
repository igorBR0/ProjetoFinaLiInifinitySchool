

class CadastroConttroler:
    def __init__(self,usuarios: list = None):
        if usuarios is None:
            usuarios = []  # Evita usar uma lista mutável como valor padrão
        self.usuarios = usuarios  # Atribui a lista de usuários à instância da classe
    def add_user(self,nome,cargo):
        self.usuarios.append({ "nome": nome,"cargo": cargo})
    def view_user(self):
        for i in self.usuarios:
            print(i)
    def upda_user(self,nome):
       for user in self.usuarios:
            if user['nome'] == nome:
                Novo_Nome = input("Edite o nome: ")
                Novo_Cargo = input("Edite o cargo: ")
                user['nome'] = Novo_Nome
                user['cargo'] = Novo_Cargo
                print("Usuario atualizado com sucesso")
    def remo_user(self,nome):
        self.usuarios = [user for user in self.usuarios if user['nome'] != nome]
        print("Usuario removido com sucesso")
        

   