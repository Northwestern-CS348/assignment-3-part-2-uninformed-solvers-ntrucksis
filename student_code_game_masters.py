from game_master import GameMaster
from read import *
from util import *

class TowerOfHanoiGame(GameMaster):

    def __init__(self):
        super().__init__()
        
    def produceMovableQuery(self):
        """
        See overridden parent class method for more information.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?disk ?init ?target)')

    def getGameState(self):
        """
        Returns a representation of the game in the current state.
        The output should be a Tuple of three Tuples. Each inner tuple should
        represent a peg, and its content the disks on the peg. Disks
        should be represented by integers, with the smallest disk
        represented by 1, and the second smallest 2, etc.

        Within each inner Tuple, the integers should be sorted in ascending order,
        indicating the smallest disk stacked on top of the larger ones.

        For example, the output should adopt the following format:
        ((1,2,5),(),(3, 4))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### student code goes here
        
        tuple_trio = [list(), list(), list()]
        order = []
        kb = self.kb
        ask = 'fact: (on ?disk ?peg)'
        states = kb.kb_ask(parse_input(ask))
        if (len(states) > 0):
            for state in states:
                tuple_trio[int(state['?peg'][3])-1].append(int(state['?disk'][4]))
        
        for n in tuple_trio:
            x = tuple(sorted(n))
            order.append(x)
        return tuple(order)
        

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable disk1 peg1 peg3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        kb = self.kb
        tl = []
        for i in movable_statement.terms:
            tl.append(str(i))
        a = [parse_input('fact: (top ' + tl[0] + ' ' + tl[2] + ')')]
        r = [parse_input('fact: (top ' + tl[0] + ' ' + tl[1] + ')')]
        ans_1 = kb.kb_ask(parse_input('fact: (top ?disk ' + tl[2] + ')'))
        if not ans_1:
            a.append(parse_input('fact: (onPeg ' + tl[0] + ' ' + tl[2] + ')'))
            r.append(parse_input('fact: (empty ' + tl[2] + ')'))
        else:
            a.append(parse_input('fact: (onDisk ' + tl[0] + ' ' + ans_1[0]['?disk'] + ')'))
            r.append(parse_input('fact: (top ' + ans_1[0]['?disk'] + ' ' + tl[2] + ')'))

        ans_2 = kb.kb_ask(parse_input('fact: (onDisk ' + tl[0] + ' ?disk)'))
        if ans_2:
            a.append(parse_input('fact: (top ' + ans_2[0]['?disk'] + ' ' + tl[1] + ')'))
            r.append(parse_input('fact: (onDisk ' + tl[0] + ' ' + ans_2[0]['?disk'] + ')'))
        else:
            a.append(parse_input('fact: (empty ' + tl[1] + ')'))
            r.append(parse_input('fact: (onPeg ' + tl[0] + ' ' + tl[1] + ')'))
            
        for f in r:
                kb.kb_retract(f)
        for f in a:
                kb.kb_assert(f)
                

        

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[2], sl[1]]
        self.makeMove(Statement(newList))

class Puzzle8Game(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        """
        Create the Fact object that could be used to query
        the KB of the presently available moves. This function
        is called once per game.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?piece ?initX ?initY ?targetX ?targetY)')

    def getGameState(self):
        """
        Returns a representation of the the game board in the current state.
        The output should be a Tuple of Three Tuples. Each inner tuple should
        represent a row of tiles on the board. Each tile should be represented
        with an integer; the empty space should be represented with -1.

        For example, the output should adopt the following format:
        ((1, 2, 3), (4, 5, 6), (7, 8, -1))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### Student code goes here
        pass

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable tile3 pos1 pos3 pos2 pos3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        pass

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[3], sl[4], sl[1], sl[2]]
        self.makeMove(Statement(newList))
