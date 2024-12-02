
from Controller.UsuarioController import Usuario_Controller
from Controller.AcessoContoller import Acesso_Controller
from Controller.CadastroController import CadastroConttroler
from Controller.RecursoController import RecursoController
usuarios=[ {"nome": "bruce", "cargo": "admin" }]
recursos=[]
class menu:
    def __init__(self):
        
        pass
    def menuView(self):
            print("Escolha o serviço")
            print(" 1 - Acessar instalaçao Wayne")
            print(" 0 - Exit instalaçao Wayne")
            servico = int(input("Digite o serviço desejado: "))
            if servico == 1:
                user = Usuario_Controller()
                acesso = Acesso_Controller(user)
                return acesso.verifyUser(usuarios)
                #if user.getcargo() == 'admin':
                 #   return user.getcargo(), user.getnome()
            else:
                     print("Usuario nao existe,tente novamente")
               
    def menuViewl1(self):
        while(True):
          
            print("Escolha o serviço")
            print(" 1 - Cadastrar e Gerenciar Usuario")
            print(" 2 - Cadastrar e Gerencia Recursos")
            print(" 0 - retorne menu anterior recursos")
            servico = int(input("Digite o serviço desejado: ") )
            if servico == 1:
                return "gesta_user"
            elif servico == 2:
               return "gesta_rec"
            elif servico == 0:
                break

  
    def menuView_usuarios(self):
        cadastro = CadastroConttroler(usuarios)
        while(True):
            print("Escolha o serviço")
            print(" 1 - Adicionar Usuario")
            print(" 2 - Vizualizar Usuario")
            print(" 3 - Editar Usuario")
            print(" 4 - Remover Usuario")
            print(" 0 - Retornar Menu Anterior")
            servico = int(input("Digite o serviço desejado: ") )
            if servico == 1:
               
                novo_usuario = input("Digite o nome do novo usuario: ")
                novo_usuario_cargo = input("Digite o cargo do novo usuario: ")
                print("Novo usuario salvo")
                cadastro.add_user(novo_usuario, novo_usuario_cargo)
            elif servico == 2:
                   cadastro.view_user()
            elif servico == 3:
                user = input("Digite o nome do item ")
                cadastro.upda_user(user)
            elif servico == 4:
                user = input("Digite o nome do item ")
                cadastro.remo_user(user)
            elif servico == 0:
                break
    def menuView_recurso(self):
         newRecurso = RecursoController(recursos)
         while(True):
            print("Escolha o serviço")
            print(" 1 - Adicionar Recurso")
            print(" 2 - Vizualizar Recurso")
            print(" 3 - Editar Recurso")
            print(" 4 - Remover Recurso")
            print(" 0 - Retornar Menu Anterior")
            servico = int(input("Digite o serviço desejado: ") )
            if servico == 1:
                print("Adicione novo recurso")
                nome_item =  input("Digite o nome do item: ")
                quantidade = int(input("Digite a quantidade do item: "))
                tipo =   input("Digite o tipo: ")
              
                newRecurso.add_rec(nome=nome_item,quantidade=quantidade,tipo=tipo)
                #newRecurso.view_rec()
            elif servico == 2:
                  newRecurso.view_rec()
            elif servico == 3:
                    item = input("Digite o nome do item ")
                    newRecurso.upda_rec(item)
            elif servico == 4:
                item = input("Digite o nome do item ")
                newRecurso.remo_rec(item)      
            elif servico == 0:
                 break
             