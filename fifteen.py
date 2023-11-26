import numpy as np
import random
from random import choice

class Fifteen:
    

    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1,size**2)] + [0])

    #updates board when move is made
    def update(self, move):
        holdValue = 0
        pos = -1
        zeroPos = -1
        for i in range(16):
            if self.tiles[i] == move:
                pos = i
            if self.tiles[i] == 0:
                zeroPos = i
        if Fifteen.is_valid_move(self, move):
            Fifteen.transpose(self, pos, zeroPos)

    #
    def transpose(self, i, j):
        holdValue = 0
        pos = -1
        zeroPos = -1
        for w in range(16):
            if self.tiles[w] == i:
                pos = w
            if self.tiles[j] == 0:
                zeroPos = w

        holdValue = self.tiles[i]
        self.tiles[i] = self.tiles[j]
        self.tiles[j] = holdValue

    #shuffles board everytime before player starts playing
    def shuffle(self, steps=1000):
        for i in range(steps):
            x = random.randint(1,15)
            Fifteen.update(self, x)

        
    #checks if move made by player is a valid move using conditions to check
    def is_valid_move(self, move):
        pos = -1
        zeroPos = -1
        for i in range(16):
            if self.tiles[i] == move:
                pos = i
            if self.tiles[i] == 0:
                zeroPos = i

        if (pos == 0) and (zeroPos in [1, 4]):
            return True
        elif (pos == 1) and (zeroPos in (0,  2, 5)):
            return True
        elif (pos == 2) and (zeroPos in (1, 3, 6)):
            return True
        elif (pos == 3) and (zeroPos in (2, 7)):
            return True
        elif (pos == 4) and (zeroPos in (0, 5, 8)):
            return True
        elif (pos == 5) and (zeroPos in (1, 4, 6, 9)):
            return True
        elif (pos == 6) and (zeroPos in (2, 5, 7, 10)):
            return True
        elif (pos == 7) and (zeroPos in (3, 6, 11)):
            return True
        elif (pos == 8) and (zeroPos in (4, 9, 12)):
            return True
        elif (pos == 9) and (zeroPos in (5, 8, 10, 13)):
            return True
        elif (pos == 10) and (zeroPos in (6, 9, 11, 14)):
            return True
        elif (pos == 11) and (zeroPos in (7, 10, 15)):
            return True
        elif (pos == 12) and (zeroPos in (8, 13)):
            return True
        elif (pos == 13) and (zeroPos in (9, 12, 14)):
            return True
        elif (pos == 14) and (zeroPos in (10, 13, 15)):
            return True
        elif (pos == 15) and (zeroPos in (11, 14)):
            return True 
        else:
            return False
        
    #checks whether puzzle is solved
    def is_solved(self):
        if self.tiles[0] == 1 and self.tiles[1] == 2 and self.tiles[2] == 3 and self.tiles[4] == 5 \
        and self.tiles[5] == 6 and self.tiles[7] == 8 and self.tiles[9] == 10 and self.tiles[11] == 12 \
        and self.tiles[13] == 14 and self.tiles[14] == 15 and self.tiles[15] == 0:
            return True
        else:
            return False

            
    def isZero(x):
        if x == 0:
            return " "
        else:
            return str(x)

    #draws Fifften Puzzle board and stores value in each tile
    def draw(self):
        print('+-----+-----+-----+-----+')
        print('|  %s  |  %s  |  %s  |  %s  |' % (Fifteen.isZero(self.tiles[0]),Fifteen.isZero(self.tiles[1]), Fifteen.isZero(self.tiles[2]), Fifteen.isZero(self.tiles[3])))
        print('+-----+-----+-----+-----+')
        print('|  %s  |  %s  |  %s  |  %s  |' % (Fifteen.isZero(self.tiles[4]), Fifteen.isZero(self.tiles[5]), Fifteen.isZero(self.tiles[6]), Fifteen.isZero(self.tiles[7])))
        print('+-----+-----+-----+-----+')
        print('|  %s  | %s  | %s  | %s  |' % (Fifteen.isZero(self.tiles[8]), Fifteen.isZero(self.tiles[9]), Fifteen.isZero(self.tiles[10]), Fifteen.isZero(self.tiles[11])))
        print('+-----+-----+-----+-----+')
        print('| %s  | %s  | %s  |  %s  |' % (Fifteen.isZero(self.tiles[12]), Fifteen.isZero(self.tiles[13]), Fifteen.isZero(self.tiles[14]), Fifteen.isZero(self.tiles[15])))
        print('+-----+-----+-----+-----+')

    #returns board
    def __str__(self):
        char1 = " "
        char2 = "  "
        return char1 + str(Fifteen.isZero(self.tiles[0]) + char2 + Fifteen.isZero(self.tiles[1]) + char2 + Fifteen.isZero(self.tiles[2]) + char2 + Fifteen.isZero(self.tiles[3]) + char1 + "\n" + char1 \
           + Fifteen.isZero(self.tiles[4]) + char2 + Fifteen.isZero(self.tiles[5]) + char2 + Fifteen.isZero(self.tiles[6]) + char2 + Fifteen.isZero(self.tiles[7]) + char1 + "\n" + char1 \
            + Fifteen.isZero(self.tiles[8]) + char1 + Fifteen.isZero(self.tiles[9]) + char1 + Fifteen.isZero(self.tiles[10]) + char1 + Fifteen.isZero(self.tiles[11]) + char1 + "\n" \
                + Fifteen.isZero(self.tiles[12]) + char1 + Fifteen.isZero(self.tiles[13]) + char1 + Fifteen.isZero(self.tiles[14]) + char1 + Fifteen.isZero(self.tiles[15]) + char2 + "\n")




#runs program
if __name__ == '__main__':    
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    
    
    
