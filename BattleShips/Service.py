from Validator import Validator
class Service(object):
    """

    """

    def __init__(self,board):
        self.board=board
        self.Validator=Validator()

    def PlaceShip(self,ship_placement):
        """
        Creates the position for the ship and tries to place it
        """
        letters={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        create_positions=[letters[ship_placement[0]],int(ship_placement[1]),letters[ship_placement[2]],int(ship_placement[3]),letters[ship_placement[4]],int(ship_placement[5])]
        self.board.TryPlaceShip(create_positions)

    def GetBoard(self):
        return self.board.GetBoard()

    def PlaceHit(self,square):
        letters={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        create_position=[letters[square[0]],int(square[1])]
        hits=self.board.TryHit(create_position)
        return hits