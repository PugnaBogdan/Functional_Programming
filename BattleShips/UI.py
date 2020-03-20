from Validator import Validator
from random import randrange
from random import choice
class Console(object):
    """description of class"""

    def __init__(self,computer_service,player_service):
        self.computer_service=computer_service
        self.player_service=player_service
        self.Validator=Validator()
        self.Start=0
        self.player_ships=0
    def PrintPlacementBoard(self):
        board=self.player_service.GetBoard()
        code={0:".",1:"+"}
        print("  A B C D E F")
        for index in range(0,6):
            print(index, end=" ")
            for index_column in range(0,6):
                print(code[board[index][index_column]],end=" ")
            print()
    def PrintPlayerHitBoard(self):
        board=self.player_service.GetBoard()
        code={0:".",1:"+",2:"o",3:"x"}
        print("  A B C D E F")
        for index in range(0,6):
            print(index, end=" ")
            for index_column in range(0,6):
                print(code[board[index][index_column]],end=" ")
            print()
    def PrintComputerHitBoard(self):
        board=self.computer_service.GetBoard()
        code={0:".",1:".",2:"o",3:"x"}
        print("  A B C D E F")
        for index in range(0,6):
            print(index, end=" ")
            for index_column in range(0,6):
                print(code[board[index][index_column]],end=" ")
            print()
    def PlaceShip(self,ship_placement=list()):
        if self.Start==1:
            print("The game has already started no more placing")
        else:
            try:
                self.Validator.ValidateShip(ship_placement)
                self.player_service.PlaceShip(ship_placement)
                self.PrintPlacementBoard()
                self.player_ships+=1
                print("Placed ship")
            except Exception as exception:
                print(str(exception))
    def StartHitGame(self):
        if self.player_ships<2:
            print("Put down 2 ships first")
        else:
            ships=0
            while ships!=2:
                row=randrange(0,6)
                column=randrange(0,6)
                direction=randrange(0,4)
                direction_choice={0:[0,1,0,2],1:[0,-1,0,-2],2:[1,0,2,0],3:[-1,0,-2,0]}
                ship_placement=[row,column,row+direction_choice[direction][0],column+direction_choice[direction][1],row+direction_choice[direction][2],column+direction_choice[direction][3]]
                ok=0
                for index in range(len(ship_placement)):
                    if ship_placement[index] not in range(0,6):
                        ok=1
                if ok==0:
                    try:
                        self.computer_service.board.TryPlaceShip(ship_placement)
                        ships+=1
                    except Exception as exception:
                        pass
            self.Start=1

    def PlaceHit(self,square=list()):
        if self.Start!=1:
            print("The game hasn't started")
        else:
            if len(square)!=2:
                print("invalid data for the hit")
            else:
                try:
                    hits=self.computer_service.PlaceHit(square)
                    if type(hits)!=type(None):
                        print("You won!")
                        self.Start=2
                        return 0
                except Exception as exception:
                    print(str(exception))
                else:
                    ok=0
                    while ok==0:
                        row=choice("ABCDEF")
                        column=randrange(0,6)
                        square=[row,column]
                        try:
                            hits=self.player_service.PlaceHit(square)
                            if type(hits)!=type(None):
                                print("You lost")
                                self.Start=2
                                return 0
                            print("computer attacked",row,column)
                            ok=1
                        except Exception:
                            pass
                    self.PrintPlayerHitBoard()
                    self.PrintComputerHitBoard()           
                
    def Cheat(self):
        board=self.computer_service.GetBoard()
        code={0:".",1:"+",2:"o",3:"x"}
        print("  A B C D E F")
        for index in range(0,6):
            print(index, end=" ")
            for index_column in range(0,6):
                print(code[board[index][index_column]],end=" ")
            print()
    def StartGame(self):
        commands=["ship","start","attack","cheat"]
        call_command={"ship":self.PlaceShip,"start":self.StartHitGame,"attack":self.PlaceHit,"cheat":self.Cheat}
        while True:
            input_command=input("Give command:")
            command=input_command.split()
            if command[0] in commands:
                if len(command)==1:
                    call_command[command[0]]()
                else:
                    end=call_command[command[0]](command[1])
                    if type(end)!=type(None):
                        return 0
            else:
                print("Invalid command!")

