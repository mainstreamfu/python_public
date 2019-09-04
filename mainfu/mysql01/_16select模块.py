from select import select

readList = []

writeList = []

crrorList = []

while True:
    rlist,wlist,xlist=select(readList,writeList,crrorList)
    for s in rlist:
        pass

    for i in wlist:
        pass

    for j in xlist:
        pass