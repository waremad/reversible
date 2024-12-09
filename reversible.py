#
m = 2
n = 2
hw = 10

def xy2natur(x,y):
    x,y = x,y
    out = y + (y+x-2)*(y+x-1)/2
    return out

def natur2xy(n):
    x = 0
    y = 0 
    while not(x*(x+1)/2 >= n):
        x += 1
    while not(x*(x-1)/2 + y == n):
        y += 1
    x -= y - 1
    return (x,y)

def reversen(n):#数を反転させる
    if n < 0:
        n = str(-n)
        n = int("-" + n[::-1])
    else:
        n = str(n)
        n = int(n[::-1])
    return n

def operat4(xy,sign):#四則演算する
    if sign == 0:
        out = xy[0]+xy[1]
        if out == 1 or out == 0:
            return "out err "+str(out)
        return out
    elif sign == 1:
        out = xy[0]-xy[1]
        if out == 1 or out == 0:
            return "out err "+str(out)
        return out
    elif sign == 2:
        out = xy[0]*xy[1]
        if out == 1 or out%1 != 0:
            return "out err "+str(out)
        return out
    elif sign == 3:
        out = xy[0]/xy[1]
        if out == 1 or out%1 != 0:
            return "out err "+str(out)
        return out
    else:
        return "sign err "+str(sign)

def do_n(n):
    ls = ["+","-","×","÷"]
    xy = natur2xy(n)
    rexy = (reversen(xy[1]),reversen(xy[0]))
    out = []
    for i in range(4):
        if type(operat4(xy,i)) == int:
            if type(operat4(rexy,i)) == int:
                if operat4(xy,i) == operat4(rexy,i):
                    if operat4(xy,i) == reversen(operat4(xy,i)):
                        if xy[0] != 1 and xy[1] != 1:
                            if i != 0 and i != 1:
                                if xy[0] != xy[1]:
                                    if xy[0] != rexy[1] and xy[1] != rexy[0]:
                                        if xy[0] != xy[1] and xy[0] != rexy[0]:
                                            if xy[0] <= xy[1]:
                                                if xy[0] < rexy[1]:
                                                    out.append(str(xy[0])+ls[i]+str(xy[1])+"="+str(operat4(xy,i))+"="+str(rexy[0])+ls[i]+str(rexy[1]))
    return out

for i in range(10000000):
    x = do_n(i+1)
    for j in x:
        print(j)

