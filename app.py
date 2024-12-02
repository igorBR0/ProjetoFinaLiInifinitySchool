

from View.menu import menu


menu = menu()
while(True):
    acesso =  menu.menuView()
    if acesso == True:
        if (menu.menuViewl1()) == "gesta_user" :
            menu.menuView_usuarios()
        elif (menu.menuViewl1()) == "gesta_rec" :
            menu.menuView_recurso()
   
   
    