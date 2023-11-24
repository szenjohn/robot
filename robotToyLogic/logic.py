#Position movent add values
movpos = [[0,1],[1,0],[0,-1],[-1,0]]


def executeCommand(x,y,pos,command):
    if command=="MOVE":
        x+=movpos[pos][0]
        y+=movpos[pos][1]
    elif command=="LEFT":
        pos-=1
        if pos<0:
            pos = 3
    elif command=="RIGHT":
        pos = (pos+1)%4
    return [x,y,pos]
