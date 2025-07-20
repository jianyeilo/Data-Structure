from dataclasses import dataclass
from typing import Any


@dataclass
class Cell:
    key   :Any
    other :Any
    next  :Any # Optional['Cell']
    
@dataclass
class Sequence:
    head     :Any   #Cell  ダミーの先頭ノード（実データの前）
    sentinel :Any   #Cell  番兵ノード（絶対に最後に到達する）
    
    
def initSequence():
    sentinel = Cell(None,None,None)
    head     = Cell(None,None,sentinel)
    return  Sequence(head,sentinel)


def linearSearch(seq,t):
    ptr       = seq.head.next
    previous  = seq.head
    seq.sentinel.key = t
    while ptr.key != t:
        previous = ptr
        ptr      = ptr.next
    found = (ptr!=seq.sentinel)
    return found 


#自己再構成リスト

def linearSearch(seq,t):
    ptr       = seq.head.next
    previous  = seq.head
    seq.sentinel.key = t
    while ptr.key != t:
        previous = ptr
        ptr      = ptr.next
    found = (ptr!=seq.sentinel)
    if found:
    previous.next = ptr.next
    ptr.next = seq.head.next
    seq.head.next = ptr
       
    return found 
