import unittest
from main import Chess


class ChessTestCase(unittest.TestCase):
    def test_attack1(self):
        test1 = Chess(2)
        test1.p_row = 0
        test1.p_pos = 0
        test1.q_row = [1, 3]
        test1.q_pos = [1, 5]
        result = test1.attacking_pawn()
        expected = (True, [(1, 1)])
        self.assertEqual(result, expected)

    def test_attack2(self):
        test2 = Chess(5)
        test2.p_row = 4
        test2.p_pos = 2
        test2.q_row = [0, 0, 2, 4, 5]
        test2.q_pos = [0, 5, 5, 6, 2]
        result = test2.attacking_pawn()
        expected = (True, [(4, 6), (5, 2)])
        self.assertEqual(result, expected)

    def test_queen_del1(self):
        test3 = Chess(5)
        test3.p_row = 4
        test3.p_pos = 2
        test3.q_row = [0, 0, 2, 4, 5]
        test3.q_pos = [0, 5, 5, 6, 2]
        test3.queen_del(4, 6)
        result = test3.attacking_pawn()
        expected = (True, [(5, 2)])
        self.assertEqual(result, expected)

    def test_queen_del2(self):
        test4 = Chess(2)
        test4.p_row = 0
        test4.p_pos = 0
        test4.q_row = [1, 3]
        test4.q_pos = [1, 5]
        test4.queen_del(1, 1)
        result = test4.attacking_pawn()
        expected = False
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
