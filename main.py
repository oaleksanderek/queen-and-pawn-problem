import random


class Chess:
    def __init__(self, k):
        self.k = k
        self.q_row = []
        self.q_pos = []
        self.p_row = random.randint(0, 7)
        self.p_pos = random.randint(0, 7)
        self.board = [['*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*']]

    def queen_gen(self):
        for i in range(0, self.k):
            temp1 = random.randint(0, 7)
            temp2 = random.randint(0, 7)
            if temp1 == self.p_row and temp2 == self.p_pos:
                continue
            elif i > 0:
                if temp1 == self.q_row[i-1] and temp2 == self.q_pos[i-1]:
                    continue
            self.q_row.append(temp1)
            self.q_pos.append(temp2)

    def map_gen(self):
        for j in range(0, self.k):
            self.board[self.q_row[j]][self.q_pos[j]] = 'H'
        self.board[self.p_row][self.p_pos] = 'P'

    def attacking_pawn(self):
        attackers = []
        for l in range(0, self.k):
            if self.p_row == self.q_row[l] or self.p_pos == self.q_pos[l] or abs(self.p_row - self.q_row[l]) == abs(self.p_pos - self.q_pos[l]):
                attacker = (self.q_row[l], self.q_pos[l])
                attackers.append(attacker)
            continue
        if attackers:
            return True, attackers
        return False

    def new_pawn_pos(self):
        self.board[self.p_row][self.p_pos] = '*'
        m = 0
        while m < self.k:
            new_pos_1 = random.randint(0, 7)
            new_pos_2 = random.randint(0, 7)
            if new_pos_1 == self.q_row[m] and new_pos_2 == self.q_pos[m]:
                continue
            m += 1

        self.p_row = new_pos_1
        self.p_pos = new_pos_2
        self.board[self.p_row][self.p_pos] = 'P'

    def queen_del(self, row_del, pos_del):
        self.board[row_del][pos_del] = '*'
        for n in range(0, self.k):
            if row_del == self.q_row[n] and pos_del == self.q_pos[n]:
                self.q_row.remove(row_del)
                self.q_pos.remove(pos_del)
                self.k -= 1
                break

    def print_board(self):
        num = 0
        for row in self.board:
            print(row, num)
            num += 1


if __name__ == '__main__':
    x = int(input("How many queens(1-5): "))
    game = Chess(x)
    game.queen_gen()
    game.map_gen()
    game.print_board()
    print(game.attacking_pawn())
    choice1 = input("Do you want to move the pawn(y/n): ")
    if choice1 == 'y':
        game.new_pawn_pos()
    choice2 = input("Do you want to delete a queen(y/n): ")
    if choice2 == 'y':
        cor1 = int(input("Input the row coordinate (0, 7): "))
        cor2 = int(input("Input the position coordinate (0, 7): "))
        game.queen_del(cor1, cor2)
    game.print_board()
    print(game.attacking_pawn())



