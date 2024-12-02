def menuView_level0(self):
            print("Escolha o serviço")
            print(" 1 - Acessar instalaçao Wayne")
            print(" 0 - Exit instalaçao Wayne")
            servico = int(input("Digite o serviço desejado: "))
            if servico == 1:
                user = Usuario_Controller()
                cesso = Acesso_Controller(user)
                if user.getcargo == "admin":
                     print("Escolha o serviço")
                     print(" 1 - Cadastrar usuario")
                     print(" 2 - Gerencia recursos")
                     servico = input("Digite o serviço desejado")
                     if servico == 1:
                        novo_usuario = input("Digite o nome do novo usuario: ")
                        novo_usuario_cargo = input("Digite o cargo do novo usuario: ")
                        print("Novo usuario salvo")
                     elif servico == 2:
                           print("Adicione novo recurso")
                           nome_item =  input("Digite o nome do item: ")
                           quantidade = int(input("Digite a quantidade do item"))
                           
            