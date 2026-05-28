class node:
    def __init__(self,directorys=True,names="",values=b"",nexts=None,backs=None,parents=None,childs=None):
        self.nexts=nexts
        self.backs=backs
        self.parents=parents
        self.childs=childs
        self.names=names
        self.values=values


def creates(list1:list):
    backs=None
    nexts=None
    currents=None
    rets=None
    l=len(list1)
    for a in range(l):
        if backs!=None:
           b=list1[a].encode()
           currents=node(names=list1[a],values=b,backs=backs)
           backs.nexts=currents
           backs=currents
        else:
           b=list1[a].encode()
           currents=node(names=list1[a],values=b)
           backs=currents
           rets=currents
    return rets




def reports(nods):
    n1=nods
    while 1:
        print(n1.names+">"+n1.values.decode())
        if n1.nexts==None:
            break
        n1=n1.nexts



n=["8086","80186","80286","80386","80486"]






ns=creates(n)
reports(ns)

