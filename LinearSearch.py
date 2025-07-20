# StaticSearch
# DynamicSearch

from dataclasses import dataclass
from typing import Any

@dataclass
class Cell:
    key   :Any
    other :Any
    

@dataclass
class Sequence:
    elements: Any   #list 
    length  : int
    
#固定長,cell in list 
def initSequence(t):
    return Sequence(elements=[None for _ in range(t)],length=0)

#可変長
def initSequence():
    return Sequence(elements=[],length=0)    

    
    
def LinearSearch(t,seq): #seq is class Sequence , search for t
    a = seq.elements
    pos = 0
    last = seq.length-1
    while (pos <= last) and (a[post].key != t):
        post += 1
    found = (post <= last)
    return found

def insert(seq,valKey,valOthers): #seq is class  Sequence 
    seq.length += 1
    seq.elements.append(Cell(valKey,valOthers))
    
    
def delete(seq,pos):
    if pos >= seq.length :
        error
    tmp = seq.elements[pos]
    seq.elements.pop(pos)
    seq.length -= 1
    return tmp


#番兵（sentinel)

def lineafSearch(seq,t):
    a = seq.elements
    a.append(Cell(t,None))
    pos = 0
    last = seq.length
    while (a[pos].key!=t):
        pos += 1
    found = (pos<=last)
    a.pop()
    return found

