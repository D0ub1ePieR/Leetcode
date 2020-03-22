# python3
# medium
# 递归 数学
# 40ms 33.33%
# 13.5MB 5.00%

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # sum_a = sum([sum(x == 'O' for x in line) for line in board])
        # sum_b = sum([sum(x == 'X' for x in line) for line in board])
        t = ''.join(board)
        sum_a = t.count('X')
        sum_b = t.count('O')
        if sum_a - sum_b not in [0, 1]:
            return False
        flag_a = flag_b = 0
        if 'OOO' in [board[0], board[1], board[2], t[0::3], t[1::3], t[2::3], t[0::4], t[2::2][:-1]]:
            flag_b = 1
        if 'XXX' in [board[0], board[1], board[2], t[0::3], t[1::3], t[2::3], t[0::4], t[2::2][:-1]]:
            flag_a = 1
        if flag_a == 1:
            if sum_a - sum_b == 0 or flag_b == 1:
                return False
        elif flag_b == 1:
            if sum_a - sum_b == 1:
                return False
        return True

# 100ms 5.05%
# 28.9MB 5.00%

class Solution:
    def __init__(self):
        self.dic = {}
        tmp = {'O': -1, ' ': 0, 'X': 1}
        for i in ['O', ' ', 'X']:
            for j in ['O', ' ', 'X']:
                for k in ['O', ' ', 'X']:
                    self.dic[i+j+k] = [tmp[i], tmp[j], tmp[k]]

    def validTicTacToe(self, board: List[str]) -> bool:
        import numpy as np
        b = []
        for line in board:
            b.append(self.dic[line])
        b = np.array(b)
        if b.sum() not in [0, 1]:
            return False
        flag_a = flag_b = 0
        if (b[0] == [-1, -1, -1]).all() or (b[1] == [-1, -1, -1]).all() or (b[2] == [-1, -1, -1]).all() or (b[:, 0] == [-1, -1, -1]).all() or (b[:, 1] == [-1, -1, -1]).all() or (b[: 2] == [-1, -1, -1]).all() or [b[0, 0], b[1, 1], b[2, 2]] == [-1, -1, -1] or [b[2, 0], b[1, 1], b[0, 2]] == [-1, -1, -1]:
            flag_b = 1
        if (b[0] == [1, 1, 1]).all() or (b[1] == [1, 1, 1]).all() or (b[2] == [1, 1, 1]).all() or (b[:, 0] == [1, 1, 1]).all() or (b[:, 1] == [1, 1, 1]).all() or (b[: 2] == [1, 1, 1]).all() or [b[0, 0], b[1, 1], b[2, 2]] == [1, 1, 1] or [b[2, 0], b[1, 1], b[0, 2]] == [1, 1, 1]:
            flag_a = 1
        if flag_a == 1:
            if b.sum() == 0 or flag_b == 1:
                return False
        elif flag_b == 1:
            if b.sum() == 1:
                return False
        return True
