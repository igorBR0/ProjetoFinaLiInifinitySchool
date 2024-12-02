
from Model.Usuario import Usuario_Model




class Usuario_Controller:
   
    def __init__(self):
        usuario = Usuario_Model()
        usuario.nome =  input("Por favor diga seu nome " )
        usuario.cargo = input("Por favor diga seu cargo " )
        self.usuario = usuario
    def getnome(self):
        return self.usuario.nome
    def getcargo(self):
        return self.usuario.cargo
       