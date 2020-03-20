import unittest
from Service import *
from Repository import *
class Test_test1(unittest.TestCase):
    def setUp(self):
        self.test_board=Repository()
        self.test_service=Service(self.test_board)
    def test_A(self):
        test_validity=self.test_board.GetBoard()
        for index in range(0,6):
            for elem in test_validity[index]:
                if elem!=0:
                    self.assertEqual(0,1)
        self.test_service.PlaceShip("A1A2A3")
        test_validity=self.test_board.GetBoard()
        self.assertEqual(1,test_validity[1][0])
        try:
            self.test_service.PlaceShip("A1A2A3")
            self.assertFalse()
        except Exception as exception:
            self.assertEqual(str(exception),"Ships overlaping")
        self.test_service.PlaceShip("C2D2E2")
        test_validity=self.test_board.GetBoard()
        self.assertEqual(1,test_validity[2][2])
        self.test_service.PlaceShip("A2A3A4")
        test_validity=self.test_board.GetBoard()
        self.assertEqual(0,test_validity[1][0])
        self.assertEqual(1,test_validity[4][0])


if __name__ == '__main__':
    unittest.main()
