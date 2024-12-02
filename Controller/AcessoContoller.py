from Model.Acesso import controleAcesso_Model
from Controller.UsuarioController import Usuario_Controller



class Acesso_Controller:
    def __init__(self, usuario: Usuario_Controller ):
        self.nome = usuario.getnome()
        self.cargo = usuario.getcargo()
        #acesso = controleAcesso_Model()
        
    def verifyUser(self,usuarios : list = None):
          for usuario in usuarios:
                if usuario['nome'] == self.nome and usuario['cargo'] == self.cargo:
                     print(self.nome)
                     return True
       

   