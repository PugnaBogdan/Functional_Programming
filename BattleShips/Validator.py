class Validator(object):
    """
    """
    def ValidateShip(self,ship_placement):
        """
        Validates that the input for the ship is correct and doesn't fall from the board
        """
        letters="ABCDEF"
        if len(ship_placement)!=6:
            raise Exception("Invalid data for placement less/more data")
        else:
            for index in range(0,6):
                if index%2==0:
                    if ship_placement[index] not in letters:
                        raise Exception("Invalid data for square")
                else:
                    if int(ship_placement[index]) not in range(0,6):
                        raise Exception("Invalid data for square")
    def ValidateGoodShipPlacement(self,board,ship_placement):
        """
        Validates that the ship doesn't overlap with the last placed ship
        """
        for index in range(0,6,2):
            if board[ship_placement[index+1]][ship_placement[index]]==1:
                raise Exception("Ship Overlap")


