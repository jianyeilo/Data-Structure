
# グラフ　有限個の点（頂点(node)）を有限個の辺で繋いだ物
#　木　　　全体がつながってかつ、閉じたパスがないグラフ

#root(根)　子と親、子孫と先祖
# 葉と内点、深さと高さ
#順序木と二分木


from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    element:Any
    left   :Any
    right  :Any
    
@dataclass
class Tree:
    root  :Any
    
    
a  = Tree (Node("root",
                Node("Ldepth1",
                       Node("Ldepth2",
                            Node("Ldepth",
                                 None,
                                 None
                                ),
                            Node("Rdepth",
                                 None,
                                 None
                                )
                            ),
                       Node("Rdepth2",
                            None,
                            None
                            )
                    ),
                Node("Rdepth1",
                     None,
                     None)))


#木の走査

#pre-order 前順走査
#根 → 左 → 右
#親の頂点を調べてから、子の頂点を順に調べに行く走査法
#根の頂点から始め、まず左の頂点を最大の深さまで帰納的調べる


def preorder(ptr):
    if ptr is not None:
        print(print.element)   #根を処理preorder
        preorder(ptr.left)     #左を
        preorder(ptr.right)    #右
        


#post-order 後順走査　
#左 → 右 → 根
#子を調べ尽くしたら自分
#最大の深さまでいく

def postorder(ptr):
    if ptr is not None:
        postorder(ptr.left)
        postorder(ptr.right)
        print(ptr.elemnt)
        



#in-order　　間順走査
#左 → 根 → 右

def inorder(ptr):
    if ptr is not None:
        inorder(ptr.left)
        print(ptr.element)
        inorder(ptr.right)