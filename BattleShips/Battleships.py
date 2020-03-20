from UI import * 
from Service import *
from Repository import *



Computer_board=Repository()
Player_board=Repository()
Computer_service=Service(Computer_board)
Player_service=Service(Player_board)
UI=Console(Computer_service,Player_service)

UI.StartGame()



