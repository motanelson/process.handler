import nodes

n=["8086","80186","80286","80386","80486"]




def creates(list1:list):
    backs=None
    nexts=None
    currents=None
    rets=None
    l=len(list1)
    for a in range(l):
        if backs!=None:
           b=n[a].encode()
           currents=nodes.node(names=n[a],values=b,backs=backs)
           backs.nexts=currents
           backs=currents
        else:
           b=n[a].encode()
           currents=nodes.node(names=n[a],values=b)
           backs=currents
           rets=currents
    return rets




def reports(nods:nodes.node):
    n1=nods
    while 1:
        print(n1.names+">"+n1.values.decode())
        if n1.nexts==None:
            break
        n1=n1.nexts

ns=creates(n)
reports(ns)