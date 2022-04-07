treedata = open("Day18/Snailnumbers.txt").read().split()
root = None # root of the tree I will use when calling __repr__ on each Node

class Node:
    def __init__(self, p = None, l = None, r = None, v = None):
        self.p = p
        self.l = l
        self.r = r
        self.v = v

    def __repr__(self): ## Tree rooted at root node with this node highlighted
        return t2s(root,self)

# Convert string to tree. Return tree root node. Doesn't fix parent pointers in tree nodes.
def s2t(s): 
    if s[0] != '[':
        return Node(None,None,None,int(s))

    b = 0
    for i in range(1,len(s)):
        if s[i] == '[':
            b +=1
        elif s[i] == ']' or b == 0:
            b -= 1
            if b <= 0:
                return Node(None,s2t(s[1:i+1]),s2t(s[i+2:-1]),None)

# Fixes parent pointers for already defined tree
def parentfix(node): 
    while node.l != None and node.l.p == None:
        node.l.p = node
        parentfix(node.l)
    while node.r != None and node.r.p == None:
        node.r.p = node
        parentfix(node.r)

# Convert string to tree. Return tree root node. With parent pointers fixed.
def maketree(s):
    r = s2t(s)
    parentfix(r)
    return r

# Convert tree to string, highlighting node h.
def t2s(node, h = None):
    if node.v != None:
        return '*' + str(node.v) + '*' if node == h else str(node.v)
    return ('*[*' if node == h else '[') + t2s(node.l,h) + ',' + t2s(node.r,h) + ']'

def explode(node): # node at depth 4 (2 children at depth 5)
    e = getexploder(node,4)
    if e == None: return False # nothing to explode

    nextl = lnum(e.l)
    if nextl != None:
        nextl.v += e.l.v

    nextr = rnum(e.r)
    if nextr != None:
        nextr.v += e.r.v

    e.l = None
    e.r = None
    e.v = 0

    return True

def getexploder(n, depth=4):
    if depth == 0 and n.v == None:
        return n

    if n.l != None:
        gl = getexploder(n.l,depth-1)
        if gl: return gl
    if n.r != None: # only go right if there is no exploder to the left
        gr = getexploder(n.r,depth-1)
        if gr: return gr
    return None

def split(n):
    if n.v and n.v >= 10:
        n.l = Node(p = n, v = int(n.v/2))
        n.r = Node(p = n, v = int((n.v+1)/2))
        n.v = None
        return True # did a split
    
    if n.l != None:
        sl = split(n.l)
        if sl: return sl

    if n.r != None:
        sr = split(n.r)
        if sr: return sr

    return False
       
def add(rootl,rootr):
    r = Node(None, rootl, rootr, None)
    rootl.p = r
    rootr.p = r
    return r # new root

# Get the next number to the right of node
def rnum(node):
    if node.p == None: return None # if I get to the root there are no numbers to the right
    if node == node.p.r:
        return rnum(node.p)
    n = node.p.r
    while n.l != None:
        n = n.l
    return n

# Get the next number to the left of node
def lnum(node):
    if node.p == None: return None # if I get to the root there are no numbers to the left
    if node == node.p.l:
        return lnum(node.p)
    n = node.p.l
    while n.r != None:
        n = n.r
    return n

def magnitude(n):
    if n.v != None:
        return n.v
    return 3 * magnitude(n.l) + 2 * magnitude(n.r)

### Part 1 ###
root = maketree(treedata[0])
for s in treedata[1:]:
    root = add(root, maketree(s))
    while explode(root) or split(root):
        continue
print('Final magnitude:', magnitude(root))

### Part 2 ###
maxmag = 0
for s in treedata:
    for t in treedata:
        if s != t:
            root = add(maketree(s),maketree(t))
            while explode(root) or split(root):
                continue
            if magnitude(root) > maxmag:
                maxmag = magnitude(root)
            
print('Maximum pair magnitude:', maxmag)