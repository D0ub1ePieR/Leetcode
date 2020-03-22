# 794、有效的井字游戏
> tag: python 、 递归 、 数学

***
### 题目描述

&emsp;&emsp;用字符串数组作为井字游戏的游戏板 `board`。当且仅当在井字游戏过程中，玩家有可能将字符放置成游戏板所显示的状态时，才返回 `true`。

&emsp;&emsp;该游戏板是一个 3 x 3 数组，由字符 `" "`，`"X"` 和 `"O"` 组成。字符 `" "` 代表一个空位。

以下是井字游戏的规则：

* 玩家轮流将字符放入空位（" "）中。

* 第一个玩家总是放字符 “X”，且第二个玩家总是放字符 “O”。

* “X” 和 “O” 只允许放置在空位中，不允许对已放有字符的位置进行填充。

* 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。

* 当所有位置非空时，也算为游戏结束。

* 如果游戏结束，玩家不允许再放置字符。

### 示例

```
  示例 1:
  输入: board = ["O  ", "   ", "   "]
  输出: false
  解释: 第一个玩家总是放置“X”。

  示例 2:
  输入: board = ["XOX", " X ", "   "]
  输出: false
  解释: 玩家应该是轮流放置的。

  示例 3:
  输入: board = ["XXX", "   ", "OOO"]
  输出: false

  示例 4:
  输入: board = ["XOX", "O O", "XOX"]
  输出: true
```

### 说明

* 游戏板 `board` 是长度为 `3` 的字符串数组，其中每个字符串 `board[i]` 的长度为 `3`。

* `board[i][j]` 是集合 `{" ", "X", "O"}` 中的一个字符。

***
### 题目链接
[794. 有效的井字游戏](https://leetcode-cn.com/problems/valid-tic-tac-toe-state/)

***
### 题解

&emsp;&emsp;主要思路便是，讨论所有不符合规则的情况如何会出现。可以表示为下面几条

1. X 的个数减 O 的个数的差不是 0 或 1

2. X 赢了的情况下 O 也赢了或 O 的个数和 X 一样

3. O 赢了的情况下 X 和 O 的个数不等

> 判断时由上往下判断，即靠下的条件默认上面的条件是成立的

那么这个问题就可以被分解为两个问题 **(1)** 计算 `borad` 中 `O` 和 `X` 的个数以及 **(2)** 判断 `borad` 中 `O` 和 `X` 是否获胜。

```python
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
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
```

&emsp;&emsp;最终结果，*运行时间40ms*，超过33.33%；*占用内存13.5MB*，超过5.00%。
