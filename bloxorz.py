import sys
def bloxorz(fname):
    fd = open(fname, "r")
    l = []
    result = []
    for k in fd:
        l.append(k.strip())
    sp = (-1,-1)
    tp = (-1,-1)
    table = {}
    for r in range(len(l)):
        a = l[r]
        for c in range(len(a)-1):
            if a[c] == "S":
                sp = (c,r)
            elif a[c] == "T":
                tp = (c,r)
            if tp != (-1,-1) and sp != (-1,-1):
                break
    if sp == (-1,-1) or tp == (-1,-1):
        print("no path")
    p = sp
    np = neighbor(p,l)
    alist = [(p, [p])]
    while len(result) == 0:
        if not alist:
            break
        point, path = alist.pop(0)
        if point == tp:
            result.append(path)
        else:
            for m in neighbor(point,l) - set(path):
                print(m)
                alist.append((m, path + [m]))
    if not result:
        print("no path")
    else:
        st = display(result[0])
        print(st)
    
def display(d):
    k = "no shortest path"
    if type(d[0][1]) is not tuple and type(d[0][0]) is not tuple:
        x = d[0][0]
        y = d[0][1]
        if type(d[1][0]) is tuple:
            if d[1][0][0] == x+1:
                k = "R"
            else:
                k = "L"
        else:
            if d[1][1][1] == y-1:
                k = "U"
            else:
                k = "D"
    elif type(d[0][1]) is tuple:
        x = d[0][0]
        y0 = d[0][1][0]
        y1 = d[0][1][1]
        if type(d[1][1]) is int:
            if d[1][1] == y0 - 1:
                k = "U"
            elif d[1][1] == y1 + 1:
                k = "D"
        else:
            if d[1][0] == x - 1:
                k = "L"
            else:
                k = "R"
    elif type(d[0][0]) is tuple:
        x0 = d[0][0][0]
        x1 = d[0][0][1]
        y = d[0][1]
        if type(d[1][0]) is int:
            if d[1][0] == x0 - 1:
                k = "L"
            elif d[1][0] == x1 + 1:
                k = "R"
        else:
            if d[1][1] == y - 1:
                k = "U"
            else:
                k = "D"
    if len(d) == 2:
        return k
    else:
        return k + display(d[1:])
def neighbor(p,l):
    cl = [".","o","T","S"]
    if type(p[1]) is not tuple and type(p[0]) is not tuple:
        k = []
        x = p[0]
        y = p[1]
        if len(l) > 2 and y > 1:
            if len(l[y-1]) > x and len(l[y-2]) > x:
                if l[y-1][x] in cl and l[y-2][x] in cl:
                    u = (p[0],(p[1]-2,p[1]-1))
                    k.append(u)
        if len(l[y]) > x+2:
            if l[y][x+1] in cl and l[y][x+2] in cl:
                r = ((p[0]+1,p[0]+2),p[1])
                k.append(r)
        if len(l) > y+2:
            if len(l[y+1]) > x and len(l[y+2]) > x:
                if l[y+1][x] in cl and l[y+2][x] in cl:
                    d = (p[0],(p[1]+1,p[1]+2))
                    k.append(d)
        if len(l[y]) > 2 and x > 1:
            if l[y][x-1] in cl and l[y][x-2] in cl:
                l = ((p[0]-2,p[0]-1),p[1])
                k.append(l)
        return set(k)
    elif type(p[1]) is tuple:
        k = []
        x = p[0]
        y0 = p[1][0]
        y1 = p[1][1]
        if y0 > 0:
            if len(l[y0-1]) > x:
                if l[y0-1][x] in cl:
                    if l[y0-1][x] != ".": 
                        u = (x,y0-1)
                        k.append(u)
        if len(l[y0]) > x+1 and len(l[y1]) > x+1:
            if l[y0][x+1] in cl and l[y1][x+1] in cl:
                r = (x+1,(y0,y1))
                k.append(r)
        if len(l) > y1+1:
            if len(l[y1+1]) > x:
                if l[y1+1][x] in cl:
                    if l[y1+1][x] != ".":
                        d = (x,y1+1)
                        k.append(d)
        if x > 0:
            if len(l[y0]) > x-1 and len(l[y1]) > x-1:
                if l[y0][x-1] in cl and l[y1][x-1] in cl:
                    l = (x-1,(y0,y1))
                    k.append(l)
        return set(k)
    elif type(p[0]) is tuple:
        k = []
        x0 = p[0][0]
        x1 = p[0][1]
        y = p[1]
        if y > 0 and len(l[y-1]) > x1:
            if l[y-1][x0] in cl and l[y-1][x1] in cl:
                u = ((x0,x1),y-1)
                k.append(u)
        if len(l[y]) > x1+1:
            if l[y][x1+1] in cl:
                if l[y][x1+1] != ".":
                    r = (x1+1,y)
                    k.append(r)
        if len(l) > y+1:
            if len(l[y+1]) > x1:
                if l[y+1][x0] in cl and l[y+1][x1] in cl:
                    d = ((x0,x1),y+1)
                    k.append(d)
        if x0 > 0:
            if len(l[y]) > x0:
                if l[y][x0-1] in cl:
                    if l[y][x0-1] != ".":
                        l = (x0-1,y)
                        k.append(l)
        return set(k)
    

name = sys.argv[1]
bloxorz(name)
