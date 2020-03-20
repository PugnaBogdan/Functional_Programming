from Validator import Validator
class Repository(object):
    """description of class"""


    def __init__(self):
        self.board= [ [0 for index in range(0,6)] for index_2 in range(0,6)]
        self.Validator=Validator()
        self.ships=[0,0]
        self.hits=0

    def TryPlaceShip(self,ship_positions):
        """
        Tries to place a ship and in case that it overlaps it doesn't place it and returns an error
        If it places it moves the ship with a position to the left
        """
        cut_ship=self.ships.pop(0)
        print(cut_ship)
        if cut_ship!=0:
            for index in range(0,6,2):
                self.board[cut_ship[index+1]][cut_ship[index]]=0
        try:
            self.Validator.ValidateGoodShipPlacement(self.board,ship_positions)
            self.ships.append(ship_positions)
            for index in range(0,6,2):
                    self.board[ship_positions[index+1]][ship_positions[index]]=1
        except Exception as exception:
            if cut_ship!=0:
                for index in range(0,6,2):
                    self.board[cut_ship[index+1]][cut_ship[index]]==1
            self.ships.insert(0,cut_ship)
            raise Exception("Ships overlaping")
    def TryHit(self,position):
        if self.board[position[1]][position[0]]>1:
            raise Exception("Already hit")
        else:
            self.board[position[1]][position[0]]+=2
            if self.board[position[1]][position[0]]==3:
                self.hits+=1
            if self.hits==6:
                return 6

    def GetBoard(self):
        return self.board 
