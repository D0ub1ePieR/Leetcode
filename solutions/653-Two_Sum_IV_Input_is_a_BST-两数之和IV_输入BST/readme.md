# 653、两数之和IV-输入BST
> tag: python3 、 树

***
### 题目描述
给定一个二叉搜索树和一个目标结果，如果 **BST** 中存在两个元素且它们的和等于给定的目标结果，则返回 `true`。

### 案例1
```
  输入:
        5
       / \
      3   6
     / \   \
    2   4   7

  Target = 9

  输出: True
```

### 案例2
```
  输入:
        5
       / \
      3   6
     / \   \
    2   4   7

  Target = 28

  输出: False
```

***
### 题目链接
[653、两数之和IV-输入BST](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/)
***
### 题解
  * **双指针**  

    &emsp;将简单问题复杂化，由于给的是一个*二叉搜索树*，所以将其中序遍历后得到的结果是有序排列的。于是就可以使用[两数之和Ⅱ_输入有序数组](../167-Two_SumII_Input_array_is_sorted-两数之和Ⅱ_输入有序数组)中所使用的双指针，变回了同样的问题。  
    &emsp;但是这道题并不需要得到构成目标值之和的**序号**，只需要返回是否能够组成目标值，即返回`True`和`False`。

  * **Hash table**

    &emsp;这道题更适合使用[两数之和](../1-Two_Sum-两数之和)的方法。使用先序遍历，将每一次得到的值存入哈希表中，如果表中存在与其相加为目标值的值则将 `flag` 标志置为 `True`。
    > &emsp;这里可以使用DFS，中序等等。使用先序考虑到在遍历时首先进行求和的判断再进入左右分支，如果判断成功可以直接return返回，减少运算时间。  
      &emsp;同时一时间没有想起来非递归的遍历怎么写，使用了递归版本的先序遍历。如果使用非递归进行遍历则可以在第一次找到符合条件的值时直接跳出循环，进一步缩短时间。

    ```python
      class Solution:
          def findTarget(self, root: TreeNode, k: int) -> bool:
              d = set()
              self.flag = False
              def mid(node):
                  if node.val in d:
                      self.flag = True
                      return
                  else:
                      d.add(k - node.val)
                  if node.left:
                      mid(node.left)
                  if node.right:
                      mid(node.right)

              mid(root)
              return self.flag
    ```

    &emsp;最终结果，*运行时间80ms*，超过90.45%；*占用内存15.9MB*，超过37.64%。这里如果`d`使用**数组**进行存储，会导致运行时间变为**600ms**。(*猜测是由于数组append操作导致的*)因此这里最后使用了**集合**。
