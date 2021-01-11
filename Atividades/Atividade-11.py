import unittest

class Ponto():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def qualQuadrante(self):
        if (self.getX() > 0) and (self.getY() > 0):
            return 1
        elif (self.getX() < 0) and (self.getY() > 0):
            return 2
        elif (self.getX() < 0) and (self.getY() < 0):
            return 3
        elif (self.getX() > 0) and (self.getY() < 0):
            return 4
        elif (self.getX() == 0 and self.getY() != 0):
            return "x"
        elif (self.getY() == 0 and self.getX() != 0):
            return "y"
        else:
            return 0

class Quadrilátero():
    def __init__(self, P1x, P1y, P2x, P2y):
        self.__P1 = Ponto(P1x, P1y)
        self.__P2 = Ponto(P2x, P2y)

    def contidoEmQ(self, Ponto):
        self.__Pontox = Ponto.getX()
        self.__Pontoy = Ponto.getY()

        return ((self.__Pontox >= self.__P1.getX() and self.__Pontox <= self.__P2.getX()) and (self.__Pontoy <= self.__P1.getY() and self.__Pontoy >= self.__P2.getY()))

class PontoeRetTest(unittest.TestCase):
    def test1Ponto(self):
        self.assertEqual(Ponto(2, 1).getX(), 2)
    def test2Ponto(self):
        self.assertEqual(Ponto(2, 1).getY(), 1)
    def test3Ponto(self):
        self.assertEqual(Ponto(2, 1).qualQuadrante(), 1)

    def testQuad(self):
        self.assertEqual(Quadrilátero(-5, 4, 3, -5).contidoEmQ(Ponto(2, 1)), True)

if __name__ == '__main__':
    unittest.main()