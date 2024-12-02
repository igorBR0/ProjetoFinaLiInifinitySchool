from Model.Recursos import Recurso_Model

class RecursoController:
    def __init__(self,rec : list):
        if rec is None:
            rec = []  # Evita usar uma lista mutável como valor padrão
        self.rec = rec  # Atribui a lista de recursos à instância da classe
        recurso = Recurso_Model()   
      
    def add_rec(self,nome,quantidade, tipo):
         
        self.rec.append({"nome": nome,"quantidade": quantidade,"tipo": tipo})
        print("Recurso Adicionado com sucesso")
        
    def upda_rec(self,nome):
       
       for item in self.rec:
            if item['nome'] == nome:
                Novo_Nome = input("Edite o nome: ")
                Novo_Quantidade = int(input("Digite quantidade: "))
                Novo_Tipo =   input("Edite o tipo: ")
                item['nome'] = Novo_Nome
                item['quantidade'] = Novo_Quantidade
                item['tipo'] = Novo_Tipo
                print("Recurso atualizado com sucesso")
    def view_rec(self):
        for i in self.rec:
            print(i)
    def remo_rec(self,nome):
       self.rec = [item for item in self.rec if item['nome'] != nome]
       print("Recurso removido com sucesso")
        